# pylint: disable=duplicate-code

""" The base class for how a platform will operate """
from abc import ABC
from typing import Any, Dict, List, Optional

from kubernetes import client

from mcli.config_objects import MCLIPlatform
from mcli.submit.kubernetes.mcli_job_future import MCLIK8sJob, MCLIVolume
from mcli.submit.platforms_future.instance_type import InstanceList, InstanceType
from mcli.utils.utils_kube import safe_update_optional_dictionary, safe_update_optional_list

# types
Resources = Dict[str, int]
Description = Dict[str, Any]


class PlatformInstance(ABC):
    """ All Instance Related Functions """
    allowed_instances: InstanceList  # InstanceList

    def is_allowed_instance(self, instance_type: str) -> bool:
        """ checks if the instance type is an allowed instances """
        instance = self.allowed_instances.get_instance_by_name(instance_name=instance_type)
        if instance is None:
            return False
        return True

    def get_instance(self, instance_type: str) -> InstanceType:
        """ gets the InstanceType from a str, throws if not available in platform"""
        instance = self.allowed_instances.get_instance_by_name(instance_name=instance_type)
        if instance is None:
            raise ValueError(f'{instance_type} not found in {self.__class__.__name__}')
        assert isinstance(instance, InstanceType)
        return instance

    def get_instance_description(self, instance_type: str) -> str:
        instance = self.get_instance(instance_type=instance_type)
        return instance.desc

    def get_smallest_cpu_instance(self, min_cpus: int) -> InstanceType:
        assert min_cpus > 0, f'min_cpus must be > 0, got {min_cpus}.'
        min_instance = None
        available_cpus = float('inf')

        for instance in self.allowed_instances:
            if (instance.gpu_count is None or instance.gpu_count == 0) and \
              (instance.cpu_count is not None and  0 < instance.cpu_count < available_cpus):
                min_instance = instance
                available_cpus = instance.cpu_count

        if min_instance is None:
            raise ValueError(f'CPU-only node '
                             f'with at least {min_cpus} cpus not found.'
                             ' Use mctl instances to view available types.')
        assert min_instance is not None
        print(min_instance)
        return min_instance


class PlatformPriority(ABC):
    # priority class to use for the job
    priority_class_labels: Dict[str, str] = {}
    default_priority_class: Optional[str] = None  # If a priority class should be default, put it here.

    def get_priority_class_label(self, priority_class_override: Optional[str]) -> Optional[str]:
        priority_class = priority_class_override if priority_class_override else self.default_priority_class

        priority_class_label: Optional[str] = None
        if priority_class is not None:
            if priority_class not in self.priority_class_labels:
                raise ValueError(
                    f'Invalid priority class. Must be one of {self.priority_class_labels}, not {priority_class}')
            priority_class_label = self.priority_class_labels[priority_class]
        return priority_class_label


class PlatformProperties(ABC):
    platform_information: MCLIPlatform

    @property
    def namespace(self):
        return self.platform_information.namespace


class GenericPlatform(PlatformInstance, PlatformPriority, PlatformProperties):
    """ A Generic Platform implementation """

    def __init__(self, platform_information: MCLIPlatform) -> None:
        self.platform_information = platform_information
        super().__init__()

    def get_node_selectors(self, instance_type: str) -> Dict[str, str]:
        instance = self.get_instance(instance_type=instance_type)
        return instance.node_selectors

    def get_annotations(self, instance_type: str):
        del instance_type
        return {}

    def get_volumes(self) -> List[MCLIVolume]:
        return [
            MCLIVolume(
                volume=client.V1Volume(
                    name='dshm',
                    empty_dir=client.V1EmptyDirVolumeSource(medium='Memory'),
                ),
                volume_mount=client.V1VolumeMount(
                    name='dshm',
                    mount_path='/dev/shm',
                ),
            ),
        ]

    def get_tolerations(self, instance_type: str) -> List[Dict[str, str]]:
        del instance_type
        return []

    def prepare_job_for_platform(
        self,
        job_spec: MCLIK8sJob,
        instance_type: str,
        priority_class: Optional[str] = None,
    ) -> None:
        """Modifies a MCLIK8sJob with the proper specs of the Platform

        Args:
            job_spec: The MCLIK8sJob object to that represents the K8s job
            instance_type: The instance type to use on the platform
            priority_class: An optional priority class to assign the job to
       """
        job_spec.metadata.namespace = self.namespace
        job_spec.metadata.annotations = self.get_annotations(instance_type)
        job_spec.spec.backoff_limit = 0

        env_vars = {'MOSAICML_INSTANCE_TYPE': instance_type}

        resources = self.get_resources(instance_type)
        job_spec.container.resources = client.V1ResourceRequirements(**resources)

        if resources['limits'].get('nvidia.com/gpu', 0) == 0:
            # If no GPUs requested, limit the container visibility with this envvar.
            # see: https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/user-guide.html#gpu-enumeration
            env_vars['NVIDIA_VISIBLE_DEVICES'] = 'void'

        volumes = self.get_volumes()
        for volume in volumes:
            job_spec.add_volume(volume)

        pod_spec = job_spec.pod_spec
        pod_spec.priority_class_name = self.get_priority_class_label(priority_class_override=priority_class,)
        for env_name, env_value in env_vars.items():
            job_spec.add_environment_variable(client.V1EnvVar(name=env_name, value=env_value))

        pod_spec.restart_policy = 'Never'
        pod_spec.host_ipc = True
        pod_spec.tolerations = safe_update_optional_list(
            pod_spec.tolerations,
            self.get_tolerations(instance_type),
        )
        pod_spec.node_selector = safe_update_optional_dictionary(
            pod_spec.node_selector,
            self.get_node_selectors(instance_type),
        )

    def get_shared_metadata(self, instance_type: str) -> client.V1ObjectMeta:
        return client.V1ObjectMeta(
            namespace=self.namespace,
            labels={'mosaicml.com/instance': instance_type},
        )

    def get_resources(self, instance_type: str) -> Dict[str, Dict[str, int]]:
        """
        Returns resource requests and limits for kubernetes. Resources are
        hard-coded.
        """

        instance = self.allowed_instances.get_instance_by_name(instance_name=instance_type)

        if instance is None:
            raise ValueError(f'{instance_type} not found in {self.platform_information.name}')

        assert isinstance(instance, InstanceType)
        requests: Dict[str, int] = {}
        limits: Dict[str, int] = {}
        if instance.gpu_count is not None and instance.gpu_count > 0:
            limits['nvidia.com/gpu'] = instance.gpu_count

        requests['cpu'] = instance.cpu_count - 1  # -1 core for buffer
        limits['cpu'] = instance.cpu_count

        return {'requests': requests, 'limits': limits}
