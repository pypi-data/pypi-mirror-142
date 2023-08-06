""" Kubernetes Intermediate Job Abstraction """
from abc import abstractmethod
from dataclasses import dataclass, field
from datetime import timedelta
from enum import Enum
from typing import Any, Dict, List, Optional

import yaml
from kubernetes import client  # , config

from mcli import version


@dataclass
class MCLIJob():
    """ Kubernetes Intermediate Job Abstraction """

    name: str = ''
    container_image: str = ''
    working_dir: str = ''
    command: List[str] = field(default_factory=list)
    environment: Dict[str, str] = field(default_factory=dict)
    ttl: int = int(timedelta(days=14).total_seconds())
    parameters: Dict[str, Any] = field(default_factory=dict)
    sweep: Optional[str] = None

    def get_specs(self):
        """
        Generates base kubernetes specs
        """
        other_specs = []

        job_spec = client.V1Job(api_version='batch/v1', kind='Job')
        job_spec.metadata = client.V1ObjectMeta(name=self.name)
        job_spec.status = client.V1JobStatus()

        env_list = []
        for env_name, env_value in self.environment.items():
            env_list.append(client.V1EnvVar(name=env_name, value=env_value))

        # Create the configmap spec
        data = yaml.dump({k: v for k, v in self.parameters.items() if not k.startswith('_')})
        cm = client.V1ConfigMap(api_version='v1', kind='ConfigMap', data={'parameters.yaml': data})
        cm.metadata = client.V1ObjectMeta(name=self.name)
        other_specs.append(cm)

        # Create the volume and volume mount
        cm_volume = client.V1Volume(name='config', config_map=client.V1ConfigMapVolumeSource(name=self.name))
        cm_mount = client.V1VolumeMount(name='config', mount_path='/mnt/config')

        container = client.V1Container(name='default',
                                       env=env_list,
                                       image=self.container_image,
                                       command=['/bin/bash', '-c'],
                                       args=self.command,
                                       volume_mounts=[cm_mount])

        template = client.V1PodTemplate()
        template.template = client.V1PodTemplateSpec()
        template.template.spec = client.V1PodSpec(containers=[container], volumes=[cm_volume])
        job_spec.spec = client.V1JobSpec(template=template.template, ttl_seconds_after_finished=self.ttl)

        labels = {
            'mosaicml.com/job': self.name,
            'type': 'mcli',
            'mosaicml.com/launcher_type': 'mcli',
            'mosaicml.com/mcli_version': str(version.__version__),
            'mosaicml.com/mcli_version_major': str(version.__version_major__),
            'mosaicml.com/mcli_version_minor': str(version.__version_minor__),
            'mosaicml.com/mcli_version_patch': str(version.__version_patch__),
        }
        if self.sweep:
            labels['mosaicml.com/sweep'] = self.sweep
        shared_metadata = client.V1ObjectMeta(labels=labels)

        return [job_spec, other_specs, shared_metadata]


JOB_TTL: int = int(timedelta(days=14).total_seconds())
JOB_LABELS = {
    'type': 'mcli',
    'mosaicml.com/launcher_type': 'mcli',
}


class MCLIJobSetupType(Enum):
    GIT_PULL = 'GIT_PULL'


@dataclass
class MCLIJobSetup():

    name: str
    environment_variables: List[client.V1EnvVar]
    image: str
    platform: str
    instance: str

    @abstractmethod
    def get_command(self) -> Optional[List[str]]:
        raise NotImplementedError('Not implemented')


@dataclass
class MCLIJobGitCloneSetup(MCLIJobSetup):
    instance: str
    git_repo: str
    git_branch: str

    def get_command(self) -> Optional[List[str]]:
        raise NotImplementedError('Not implemented')


@dataclass
class MCLIJobDockerSetup(MCLIJobSetup):

    def get_command(self) -> Optional[List[str]]:
        return None


@dataclass
class MCLIJobFuture():
    """ Kubernetes Intermediate Job Abstraction """

    name: str
    job_setup: MCLIJobSetup
    parameters: Dict[str, Any] = field(default_factory=dict)
    sweep: Optional[str] = None

    def get_specs(self):
        """
        Generates base kubernetes specs
        """
        other_specs = []

        job_spec = client.V1Job(api_version='batch/v1', kind='Job')
        job_spec.metadata = client.V1ObjectMeta(name=self.name)
        job_spec.status = client.V1JobStatus()

        env_list = []
        for env_item in self.job_setup.environment_variables:
            env_list.append(env_item)

        # Create the configmap spec
        data = yaml.dump({k: v for k, v in self.parameters.items() if not k.startswith('_')})
        cm = client.V1ConfigMap(api_version='v1', kind='ConfigMap', data={'parameters.yaml': data})
        cm.metadata = client.V1ObjectMeta(name=self.name)
        other_specs.append(cm)

        # Create the volume and volume mount
        cm_volume = client.V1Volume(name='config', config_map=client.V1ConfigMapVolumeSource(name=self.name))
        cm_mount = client.V1VolumeMount(name='config', mount_path='/mnt/config')

        container = client.V1Container(
            name='default',
            env=env_list,
            image=self.job_setup.image,
            volume_mounts=[cm_mount],
        )
        if self.job_setup.get_command():
            container.command = ['/bin/bash', '-c']
            container.args = self.job_setup.get_command()

        template = client.V1PodTemplate()
        template.template = client.V1PodTemplateSpec()
        template.template.spec = client.V1PodSpec(containers=[container], volumes=[cm_volume])
        job_spec.spec = client.V1JobSpec(template=template.template, ttl_seconds_after_finished=JOB_TTL)

        labels = JOB_LABELS
        labels['mosaicml.com/job'] = self.name
        shared_metadata = client.V1ObjectMeta(labels=labels)

        return [job_spec, other_specs, shared_metadata]
