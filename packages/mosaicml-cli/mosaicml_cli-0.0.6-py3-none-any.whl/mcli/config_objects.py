""" Dataclass objects used in the MCLI config for typing """
from __future__ import annotations

import json
from abc import ABC, abstractmethod
from contextlib import contextmanager
from dataclasses import dataclass, field, fields
from datetime import datetime
from enum import Enum
from typing import Any, Dict, Generator, Generic, List, Optional, Tuple, Type, TypeVar, Union, get_type_hints

import yaml

from mcli.api.typing_future import get_args, get_origin
from mcli.utils.utils_kube import base64_decode, base64_encode, create_secret, read_secret, update_secret, use_context

# pylint: disable-next=invalid-name
T_SerializableDataclass = TypeVar('T_SerializableDataclass', bound='SerializableDataclass')


@dataclass
class SerializableDataclass(Generic[T_SerializableDataclass]):
    """ A super class for Dataclasses that supports to_dict and from_dict

    Note: This super class does not support fancy typing, but does support
      - List[SerializableDataClass]
    """

    @classmethod
    def from_dict(
        cls: Type[T_SerializableDataclass],
        data: Dict[str, Any],
    ) -> T_SerializableDataclass:
        type_hints = get_type_hints(cls)

        for class_field in fields(cls):
            if class_field.name not in data:
                continue
            if class_field.name in type_hints:
                found_type: Type[Any] = type_hints[class_field.name]
                type_origin = get_origin(found_type)
                if type_origin in (list,):
                    type_args: Tuple[Type[Any]] = get_args(found_type)  # type: ignore
                    found_type = type_args[0]
                    if issubclass(found_type, SerializableDataclass):
                        data[class_field.name] = [found_type.from_dict(x) for x in data[class_field.name]]
                elif isinstance(found_type, Enum):
                    data[class_field.name] = found_type(data[class_field.name])
                elif found_type is datetime:
                    data[class_field.name] = datetime.fromisoformat(data[class_field.name])

        return cls(**data)

    def to_dict(self) -> Dict[str, Any]:

        def process_field_value(field_value: Any) -> Optional[Any]:
            """ Function that processes a field value based on its type into serializable form
            If a field value is an enum, it'll unpack it back to its serializable json value
            If a field is a list, it'll recursively process all elements
            """
            if isinstance(field_value, SerializableDataclass):
                return field_value.to_dict()
            elif isinstance(field_value, Enum):
                return field_value.value
            elif isinstance(field_value, datetime):
                return field_value.isoformat()
            elif isinstance(field_value, list):
                return [process_field_value(x) for x in field_value]
            elif field_value is not None:
                return field_value

        data = {}
        for class_field in fields(self):
            field_value = getattr(self, class_field.name)
            field_value = process_field_value(field_value)
            data[class_field.name] = field_value
        return data


@dataclass
class MCLIPlatform(SerializableDataclass):
    """Configured MCLI platform relating to specific kubernetes context
    """
    name: str
    kubernetes_context: str
    namespace: str
    environment_overrides: List[MCLIEnvironmentItem] = field(default_factory=list)

    @classmethod
    @contextmanager
    def use(cls, platform: MCLIPlatform) -> Generator[MCLIPlatform, None, None]:
        """Temporarily set the platform to use for all Kubernetes API calls

        Args:
            platform (MCLIPlatform): The platform to use

        Yields:
            MCLIPlatform: The provided platform
        """
        with use_context(platform.kubernetes_context):
            yield platform


@dataclass
class MCLIEnvironmentItem(SerializableDataclass):
    # TODO(averylamp): This is a WIP to be flushed out more later
    name: str
    env_key: str
    env_value: str


class SecretType(Enum):
    """ Enum for Types of Secrets Allowed """
    docker_registry = 'docker_registry'
    ssh = 'ssh'
    generic = 'generic'
    generic_mounted = 'generic_mounted'
    generic_environment = 'generic_environment'
    s3_credentials = 's3_credentials'

    def __str__(self) -> str:
        return str(self.value)

    @classmethod
    def ensure_enum(cls, val: Union[str, SecretType]) -> SecretType:
        if isinstance(val, str):
            return SecretType[val]
        elif isinstance(val, SecretType):
            return val
        raise ValueError(f'Unable to ensure {val} is a SecretType Enum')


@dataclass
class MCLISecret(SerializableDataclass, ABC):
    """
    The Base Secret Class for MCLI Secrets

    Secrets can not nest other SerializableDataclass objects
    """

    name: str
    secret_type: SecretType

    @property
    @abstractmethod
    def data(self) -> Dict[str, str]:
        """The `data` field for the corresponding kubernetes secret
        """
        raise NotImplementedError

    @classmethod
    def from_dict(cls: Type[T_SerializableDataclass], data: Dict[str, Any]) -> T_SerializableDataclass:
        secret_type = data.get('secret_type', None)
        if not secret_type:
            raise ValueError(f'No `secret_type` found for secret with data: \n{yaml.dump(data)}')

        secret_type: SecretType = SecretType.ensure_enum(secret_type)
        data['secret_type'] = secret_type

        secret: Optional[MCLISecret] = None
        if secret_type == SecretType.docker_registry:
            secret = MCLIDockerRegistrySecret(**data)
        elif secret_type == SecretType.generic_mounted:
            secret = MCLIGenericMountedSecret(**data)
        elif secret_type == SecretType.generic_environment:
            secret = MCLIGenericEnvironmentSecret(**data)
        elif secret_type == SecretType.ssh:
            secret = MCLISSHSecret(**data)
        elif secret_type == SecretType.s3_credentials:
            secret = MCLIS3Secret(**data)
        else:
            raise NotImplementedError(f'Secret of type: { secret_type } not supported yet')
        assert isinstance(secret, MCLISecret)
        return secret  # type: ignore

    @property
    def kubernetes_type(self) -> str:
        """The corresponding Kubernetes secret type for this class of secrets
        """
        return 'Opaque'

    def sync_to_platform(self, platform: MCLIPlatform) -> bool:
        """Sync a secret to the given platform

        Args:
            platform (MCLIPlatform): Platform to sync secret with

        Returns:
            bool: True if sync was successful
        """
        with MCLIPlatform.use(platform):
            # Check if secret exists in current context
            secret = read_secret(self.name, platform.namespace)

            success: bool
            if secret is not None:  # secret exists
                # Check if value is the same
                if secret['data'] != self.data:
                    # Patch existing secret
                    success = update_secret(self.name, platform.namespace, self.data)
                else:
                    success = True
            else:
                # Create secret
                success = create_secret(self.name, platform.namespace, self.data, self.kubernetes_type)

        return success


@dataclass
class MCLIDockerRegistrySecret(MCLISecret):
    """Secret class for docker image pull secrets
    """
    docker_username: str
    docker_password: str
    docker_email: str
    docker_server: Optional[str] = None

    @property
    def kubernetes_type(self) -> str:
        """The corresponding Kubernetes secret type for this class of secrets
        """
        return 'kubernetes.io/dockerconfigjson'

    @property
    def data(self) -> Dict[str, str]:
        """The `data` field for the corresponding kubernetes secret
        """
        data = {
            'docker_username': base64_decode(self.docker_username),
            'docker_password': base64_decode(self.docker_password),
            'docker_email': base64_decode(self.docker_email),
        }
        if self.docker_server is not None:
            data['docker_server'] = base64_decode(self.docker_server)
        json_str = json.dumps(data)
        return {'.dockerconfigjson': base64_encode(json_str)}


@dataclass
class MCLIGenericSecret(MCLISecret):
    """Secret class for generic secrets
    """
    value: str

    @property
    def data(self) -> Dict[str, str]:
        """The `data` field for the corresponding kubernetes secret
        """
        return {'value': self.value}


@dataclass
class MCLIGenericMountedSecret(MCLIGenericSecret):
    """Secret class for generic secrets that will be mounted to run pods as files
    """
    mount_path: str

    @classmethod
    def from_generic_secret(
        cls: Type[MCLIGenericMountedSecret],
        generic_secret: MCLIGenericSecret,
        mount_path: str,
    ) -> MCLIGenericMountedSecret:
        return cls(
            name=generic_secret.name,
            value=generic_secret.value,
            secret_type=SecretType.generic_mounted,
            mount_path=mount_path,
        )


@dataclass
class MCLIGenericEnvironmentSecret(MCLIGenericSecret):
    """Secret class for generic secrets that will be added as environment variables
    """
    env_key: str

    @classmethod
    def from_generic_secret(
        cls: Type[MCLIGenericEnvironmentSecret],
        generic_secret: MCLIGenericSecret,
        env_key: str,
    ) -> MCLIGenericEnvironmentSecret:
        return cls(
            name=generic_secret.name,
            value=generic_secret.value,
            secret_type=SecretType.generic_environment,
            env_key=env_key,
        )


@dataclass
class MCLISSHSecret(MCLISecret):
    """Secret class for ssh private keys that will be mounted to run pods as a file
    """
    ssh_private_key: str
    mount_path: str

    @property
    def kubernetes_type(self) -> str:
        """The corresponding Kubernetes secret type for this class of secrets
        """
        return 'kubernetes.io/ssh-auth'

    @property
    def data(self) -> Dict[str, str]:
        """The `data` field for the corresponding kubernetes secret

        NOTE: We need to ensure this is always verified on client-side
        """
        with open(self.ssh_private_key, 'r', encoding='utf8') as fh:
            key_value: str = fh.read()
        return {'ssh-privatekey': base64_encode(key_value)}


@dataclass
class MCLIS3Secret(MCLISecret):
    """Secret class for AWS credentials
    """
    credentials_file: str
    config_file: str

    @property
    def data(self) -> Dict[str, str]:
        """The `data` field for the corresponding kubernetes secret
        """
        with open(self.credentials_file, 'r', encoding='utf8') as fh:
            s3_credentials = fh.read()
        with open(self.config_file, 'r', encoding='utf8') as fh:
            s3_config = fh.read()
        return {'credentials': base64_encode(s3_credentials), 'config': base64_encode(s3_config)}
