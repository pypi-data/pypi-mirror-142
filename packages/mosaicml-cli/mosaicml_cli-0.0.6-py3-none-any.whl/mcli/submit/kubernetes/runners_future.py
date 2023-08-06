""" Generic Runner for MCLI K8s Jobs """
from typing import Any, Dict, List, Optional, cast

from kubernetes import client
from kubernetes import config as kubernetes_config
from kubernetes.client.api_client import ApiClient

from mcli import config
from mcli.config_objects import SecretType
from mcli.submit.kubernetes.mcli_job_future import MCLIJob, MCLIK8sJob
from mcli.submit.platforms_future.platform import GenericPlatform
from mcli.submit.platforms_future.registry import PlatformRegistry
from mcli.utils.utils_kube import merge_V1ObjectMeta


def title_to_snake(s):
    return ''.join(['_' + c.lower() if c.isupper() else c for c in s]).lstrip('_')


class Runner:
    """ Generic Runner for MCLI K8s Jobs """

    def __init__(self,):
        self.platform_registry = PlatformRegistry()

    def configure_job_global_environment(self, job_spec: MCLIK8sJob):
        conf = config.get_mcli_config()
        for env_item in conf.environment_variables:
            job_spec.add_environment_variable(client.V1EnvVar(name=env_item.env_key, value=env_item.env_value))

    def configure_job_global_secrets(self, job_spec: MCLIK8sJob):
        del job_spec
        conf = config.get_mcli_config()
        for secret in conf.secrets:
            if secret.secret_type == SecretType.docker_registry:
                print('WARNING: NOT IMPLEMENTED SECRET YET', secret)
            else:
                print('WARNING: NOT IMPLEMENTED SECRET YET', secret)

    def get_specs(
        self,
        job: MCLIJob,
        instance: str,
        priority_class: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        platform: GenericPlatform = self.platform_registry.get_for_instance_type(instance)

        job_spec = job.get_job_spec()
        self.configure_job_global_environment(job_spec=job_spec)
        self.configure_job_global_secrets(job_spec=job_spec)
        job_shared_metadata = job.get_shared_metadata()
        config_map, cm_volume = job.get_config_map()
        job_spec.add_volume(cm_volume)

        platform.prepare_job_for_platform(
            job_spec=job_spec,
            instance_type=instance,
            priority_class=priority_class,
        )
        platform_shared_metadata = platform.get_shared_metadata(instance_type=instance)

        shared_metadata = merge_V1ObjectMeta(job_shared_metadata, platform_shared_metadata)
        job_spec.metadata = merge_V1ObjectMeta(job_spec.metadata, shared_metadata)
        pod_template_spec = cast(client.V1PodTemplateSpec, job_spec.spec.template)

        existing_pod_template_metadata: client.V1ObjectMeta
        if pod_template_spec.metadata:
            existing_pod_template_metadata = pod_template_spec.metadata
        else:
            existing_pod_template_metadata = client.V1ObjectMeta()
        pod_template_spec.metadata = merge_V1ObjectMeta(existing_pod_template_metadata, shared_metadata)

        if config_map.metadata:
            config_map.metadata = merge_V1ObjectMeta(shared_metadata, config_map.metadata)
        else:
            config_map.metadata = shared_metadata

        k8s_objects = [config_map, job_spec]
        api = ApiClient()
        return cast(List[Dict[str, Any]], [api.sanitize_for_serialization(x) for x in k8s_objects])

    def submit(
        self,
        job: MCLIJob,
        instance: str,
        priority_class: Optional[str] = None,
    ):
        specs = self.get_specs(job, instance, priority_class)
        platform = self.platform_registry.get_for_instance_type(instance)
        # api_client = kubernetes_config.new_client_from_config(context=platform.context_name)
        api_client = kubernetes_config.new_client_from_config(context=None)

        for spec in specs:
            # Get API client from the object api version string.
            # E.g. "batch/v1" => client.BatchV1Api()

            api_version_str = spec['apiVersion']
            api_version_fragments = api_version_str.split('/')
            if len(api_version_fragments) > 1:
                api_name, api_version = api_version_fragments[:2]
            else:
                api_name, api_version = ('Core', api_version_fragments[0])
            api_name = api_name.capitalize() + api_version.upper() + 'Api'
            api = getattr(client, api_name)
            api = api(api_client=api_client)

            # Find corresponding create method from Kind string.
            # e.g. "Job" => api.create_namespaced_job(...)
            kind_str = spec['kind']
            create = getattr(api, f'create_namespaced_{title_to_snake(kind_str)}')
            create(platform.namespace, body=spec)
