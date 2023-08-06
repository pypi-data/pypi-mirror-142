# pylint: disable=duplicate-code

""" The COTA Platform """
from dataclasses import dataclass
from typing import Dict, List

from kubernetes import client

from mcli.submit.kubernetes.mcli_job_future import MCLIVolume
from mcli.submit.platforms_future.cota_instances import COTA_INSTANCE_LIST
from mcli.submit.platforms_future.instance_type import InstanceList
from mcli.submit.platforms_future.platform import GenericPlatform

NUM_MULTI_GPU_TOLERATE = 8
MAX_CPUS = 120


@dataclass
class COTAPlatform(GenericPlatform):
    """ The COTA Platform """

    allowed_instances: InstanceList = COTA_INSTANCE_LIST

    def get_volumes(self) -> List[MCLIVolume]:
        volumes = super().get_volumes()
        volumes.append(
            MCLIVolume(
                volume=client.V1Volume(
                    name='local',
                    host_path=client.V1HostPathVolumeSource(path='/localdisk', type='Directory'),
                ),
                volume_mount=client.V1VolumeMount(
                    name='local',
                    mount_path='/localdisk',
                ),
            ))

        # TODO: Readd workdisk later
        # volumes.append(
        #     MCLIVolume(
        #         volume=client.V1Volume(
        #             name="workdisk",
        #             persistent_volume_claim=client.V1PersistentVolumeClaimVolumeSource(claim_name=self.pvc_name)),
        #         volume_mount=client.V1VolumeMount(name="workdisk", mount_path=self.mount_path),
        #     ))

        return volumes

    def get_tolerations(self, instance_type: str) -> List[Dict[str, str]]:
        tolerations = []
        resources = self.get_resources(instance_type)
        num_gpus = resources['limits'].get('nvidia.com/gpu', 0)

        if num_gpus > 0:
            tolerations.append({
                'effect': 'PreferNoSchedule',
                'key': 'mosaicml.com/prefer-gpu-workloads',
                'operator': 'Equal',
                'value': 'true'
            })

        if num_gpus == NUM_MULTI_GPU_TOLERATE:
            tolerations.append({
                'effect': 'NoSchedule',
                'key': f'mosaicml.com/multigpu_{NUM_MULTI_GPU_TOLERATE}',
                'operator': 'Equal',
                'value': 'true'
            })

        return tolerations
