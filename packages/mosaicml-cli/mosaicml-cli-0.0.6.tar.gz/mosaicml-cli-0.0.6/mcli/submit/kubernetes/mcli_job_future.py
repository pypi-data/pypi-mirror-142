""" Kubernetes Intermediate Job Abstraction """

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import timedelta
from typing import Any, Dict, List, NamedTuple

import yaml
from kubernetes import client

from mcli.submit.kubernetes.mcli_job_future_typing import MCLIK8sJobTyping


class MCLIVolume(NamedTuple):
    volume: client.V1Volume
    volume_mount: client.V1VolumeMount


class MCLIK8sJob(MCLIK8sJobTyping):

    def add_volume(self, volume: MCLIVolume):
        self.pod_volumes.append(volume.volume)
        self.container_volume_mounts.append(volume.volume_mount)

    def add_environment_variable(self, environment_variable: client.V1EnvVar):
        self.environment_variables.append(environment_variable)


class MCLIConfigMap(NamedTuple):
    config_map: client.V1ConfigMap
    config_volume: MCLIVolume


@dataclass
class MCLIJob():
    """ Kubernetes Intermediate Job Abstraction """

    name: str = ''
    container_image: str = ''
    working_dir: str = ''
    command: List[str] = field(default_factory=list)
    ttl: int = int(timedelta(days=14).total_seconds())
    parameters: Dict[str, Any] = field(default_factory=dict)

    def get_job_spec(self) -> MCLIK8sJob:
        job_spec = MCLIK8sJob()
        job_spec.container.image = self.container_image
        job_spec.container.command = ['/bin/bash', '-c']
        job_spec.container.args = self.command
        job_spec.container.name = self.name
        job_spec.metadata = client.V1ObjectMeta(name=self.name)
        job_spec.spec.ttl_seconds_after_finished = self.ttl
        return job_spec

    def get_config_map(self) -> MCLIConfigMap:
        data = yaml.dump({k: v for k, v in self.parameters.items() if not k.startswith('_')})
        cm = client.V1ConfigMap(
            api_version='v1',
            kind='ConfigMap',
            data={'parameters.yaml': data},
        )
        cm.metadata = client.V1ObjectMeta(name=self.name)
        cm_volume = client.V1Volume(
            name='config',
            config_map=client.V1ConfigMapVolumeSource(name=self.name),
        )
        cm_mount = client.V1VolumeMount(
            name='config',
            mount_path='/mnt/config',
        )

        return MCLIConfigMap(
            config_map=cm,
            config_volume=MCLIVolume(
                volume=cm_volume,
                volume_mount=cm_mount,
            ),
        )

    def get_shared_metadata(self) -> client.V1ObjectMeta:
        labels = {
            'mosaicml.com/job': self.name,
            'type': 'mcli',
            'mosaicml.com/launcher_type': 'mcli',
        }
        shared_metadata = client.V1ObjectMeta(labels=labels)
        return shared_metadata
