""" Create Secrets """
import argparse
from pathlib import Path
from typing import Optional

from mcli.cli.m_create.create_secret import configure_secret_argparser, create_secret_helptext
from mcli.config import MCLIConfig
from mcli.config_objects import (MCLIDockerRegistrySecret, MCLIGenericEnvironmentSecret, MCLIGenericMountedSecret,
                                 MCLIGenericSecret, MCLIS3Secret, MCLISecret, MCLISSHSecret, SecretType)
from mcli.utils.utils_interactive import list_options
from mcli.utils.utils_kube import base64_encode
from mcli.utils.utils_string_validation import (validate_secret_key, validate_secret_name,
                                                validate_simple_absolute_filename)

_secret_default_prompt_options = {
    'allow_custom_response': True,
    'options': [],
    'pre_helptext': None,
}


def create_new_secret(
    secret_type: Optional[str] = None,
    secret_name: Optional[str] = None,
    **kwargs,
) -> int:

    def print_secret_parser_usage() -> None:
        parser = argparse.ArgumentParser()
        configure_secret_argparser(parser, secret_handler=lambda _: 1)
        parser.print_usage()

    if secret_type is None and secret_name is None:
        print('Missing required positional arguments')
        print_secret_parser_usage()
        print(create_secret_helptext)
        return 1

    conf = MCLIConfig.load_config()
    existing_secrets = conf.secrets

    if secret_name is None:
        secret_name = list_options(
            input_text='Unique Secret Name',
            helptext='Secret Name',
            validate=validate_secret_name,
            **_secret_default_prompt_options,
        )
    assert secret_name is not None

    if not validate_secret_name(secret_name):
        return 1

    if secret_name in {x.name for x in existing_secrets}:
        print(
            f'Secret Name: {secret_name} already taken.'
            ' Please choose a unique Secret Name. ',
            ' To see all env variables `mcli get secrets`',
        )
        print_secret_parser_usage()
        return 1

    generated_secret: Optional[MCLISecret] = None
    if secret_type == SecretType.docker_registry.value:
        generated_secret = _create_docker_registry_secret(secret_name=secret_name, **kwargs)
    elif secret_type == SecretType.generic_mounted.value:
        generated_secret = _create_generic_mounted_secret(secret_name=secret_name, **kwargs)
    elif secret_type == SecretType.generic_environment.value:
        generated_secret = _create_generic_environment_secret(secret_name=secret_name, **kwargs)
    elif secret_type == SecretType.ssh.value:
        generated_secret = _create_ssh_secret(secret_name=secret_name, **kwargs)
    elif secret_type == SecretType.s3_credentials.value:
        generated_secret = _create_s3_secret(secret_name=secret_name, **kwargs)
    else:
        raise NotImplementedError(f'The secret type: {secret_type} is not implemented yet')
    assert generated_secret is not None
    print(generated_secret)
    conf.secrets.append(generated_secret)
    conf.save_config()

    # Sync to all known platforms
    for platform in conf.platforms:
        generated_secret.sync_to_platform(platform)

    return 0


def _create_docker_registry_secret(
    secret_name: str,
    docker_username: Optional[str] = None,
    docker_password: Optional[str] = None,
    docker_email: Optional[str] = None,
    docker_server: Optional[str] = None,
    **kwargs,
) -> MCLISecret:
    del kwargs

    if docker_username is None:
        docker_username = list_options(
            input_text='Docker Username',
            helptext='DockerID',
            **_secret_default_prompt_options,
        )
    if docker_password is None:
        docker_password = list_options(
            input_text='Docker Password',
            helptext='Docker Access Token in Security',
            **_secret_default_prompt_options,
        )
    if docker_email is None:
        docker_email = list_options(
            input_text='Docker Email',
            helptext='Email associated with DockerID',
            **_secret_default_prompt_options,
        )

    if docker_server is None:
        docker_server = list_options(
            input_text='Docker Server',
            default_response='https://index.docker.io/v1/',
            helptext='Server location for the registry',
            **_secret_default_prompt_options,
        )

    assert docker_username is not None
    assert docker_password is not None
    assert docker_email is not None

    docker_secret = MCLIDockerRegistrySecret(
        name=secret_name,
        secret_type=SecretType.docker_registry,
        docker_username=base64_encode(docker_username),
        docker_password=base64_encode(docker_password),
        docker_email=base64_encode(docker_email),
        docker_server=base64_encode(docker_server) if docker_server else None,
    )
    return docker_secret


def _create_generic_secret(
    secret_name: str,
    value: Optional[str] = None,
    **kwargs,
) -> MCLIGenericSecret:
    del kwargs
    secret_value = value

    if secret_value is None:
        secret_value = list_options(
            input_text='Secret Value',
            helptext='Secret Data',
            **_secret_default_prompt_options,
        )
    assert secret_value is not None

    generic_secret = MCLIGenericSecret(
        name=secret_name,
        secret_type=SecretType.generic,
        value=base64_encode(secret_value),
    )
    return generic_secret


def _create_generic_mounted_secret(
    secret_name: str,
    value: Optional[str] = None,
    mount_path: Optional[str] = None,
    **kwargs,
) -> MCLIGenericMountedSecret:
    del kwargs

    generic_secret = _create_generic_secret(
        secret_name=secret_name,
        value=value,
    )

    if mount_path is None:
        mount_path = list_options(
            input_text='Mount Path For Secret',
            helptext='Mount Path',
            validate=validate_simple_absolute_filename,
            **_secret_default_prompt_options,
        )
    assert mount_path is not None

    return MCLIGenericMountedSecret.from_generic_secret(
        generic_secret=generic_secret,
        mount_path=mount_path,
    )


def _create_generic_environment_secret(
    secret_name: str,
    value: Optional[str] = None,
    env_key: Optional[str] = None,
    **kwargs,
) -> MCLIGenericEnvironmentSecret:
    del kwargs

    generic_secret = _create_generic_secret(
        secret_name=secret_name,
        value=value,
    )

    if env_key is None:
        env_key = list_options(
            input_text='Environment Key to use, KEY in KEY=VALUE',
            helptext='Environment Key',
            validate=validate_secret_key,
            **_secret_default_prompt_options,
        )
    assert env_key is not None

    return MCLIGenericEnvironmentSecret.from_generic_secret(
        generic_secret=generic_secret,
        env_key=env_key,
    )


def _create_ssh_secret(
    secret_name: str,
    ssh_private_key: Optional[str] = None,
    mount_path: Optional[str] = None,
    **kwargs,
) -> MCLISSHSecret:
    del kwargs

    if ssh_private_key is None:
        ssh_private_key = list_options(
            input_text='SSH private key',
            helptext='Path to your private SSH key',
            validate=validate_simple_absolute_filename,
            **_secret_default_prompt_options,
        )
    assert ssh_private_key is not None

    if mount_path is None:
        mount_path = list_options(
            input_text='Mount Path',
            helptext='Mount path for private SSH key within container',
            validate=validate_simple_absolute_filename,
            **_secret_default_prompt_options,
        )

    return MCLISSHSecret(name=secret_name,
                         secret_type=SecretType.ssh,
                         ssh_private_key=ssh_private_key,
                         mount_path=mount_path)


def _create_s3_secret(
    secret_name: str,
    credentials_file: Optional[str] = None,
    config_file: Optional[str] = None,
    **kwargs,
) -> MCLIS3Secret:
    del kwargs

    if credentials_file is None:
        credentials_file = list_options(
            input_text='Credentials file path',
            helptext='Path to your S3 credentials file',
            default_response=str(Path('~/.aws/credentials').expanduser()),
            **_secret_default_prompt_options,
        )

    if config_file is None:
        config_file = list_options(
            input_text='Config file path',
            helptext='Path to your S3 config file',
            default_response=str(Path('~/.aws/config').expanduser()),
            **_secret_default_prompt_options,
        )

    assert credentials_file is not None
    assert config_file is not None

    return MCLIS3Secret(name=secret_name,
                        secret_type=SecretType.s3_credentials,
                        credentials_file=credentials_file,
                        config_file=config_file)
