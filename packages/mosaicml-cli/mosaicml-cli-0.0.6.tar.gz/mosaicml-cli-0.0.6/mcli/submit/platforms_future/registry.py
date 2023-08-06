# pylint: disable=duplicate-code

""" A Singleton Platform Registry for all Sub Platforms """
from __future__ import annotations

from typing import Dict, List, Optional, Type

from mcli import config
from mcli.config_objects import MCLIPlatform
from mcli.submit.platforms_future.aws import AWSPlatform
from mcli.submit.platforms_future.azure import AzurePlatform
from mcli.submit.platforms_future.cota import COTAPlatform
from mcli.submit.platforms_future.gcp import GCPPlatform
from mcli.submit.platforms_future.platform import GenericPlatform
from mcli.submit.platforms_future.r1z1 import R1Z1Platform
from mcli.submit.platforms_future.r6z1 import R6Z1Platform

k8s_platforms: Dict[str, Type[GenericPlatform]] = {
    'aws': AWSPlatform,
    'azure': AzurePlatform,
    'gcp': GCPPlatform,
    'cota': COTAPlatform,
    'r1z1': R1Z1Platform,
    'r6z1': R6Z1Platform,
}


class PlatformRegistry():
    """ A Singleton designed to track multiple platforms """

    def __init__(self):
        self._platforms = {}
        self._instance_lookup = {}

    @property
    def platforms(self) -> List[MCLIPlatform]:
        return config.get_mcli_config().platforms

    def get(self, platform_name: str) -> GenericPlatform:
        """ Returns platform by name """
        if platform_name not in self._platforms:
            raise ValueError(f'No such platform: {platform_name}')
        else:
            return self._platforms[platform_name]

    def get_k8s_platform(self, platform: MCLIPlatform) -> GenericPlatform:
        if platform.name in k8s_platforms:
            found_platform = k8s_platforms[platform.name]
            return found_platform(platform_information=platform)
        return GenericPlatform(platform_information=platform)

    def get_for_instance_type(self, instance_type: str) -> GenericPlatform:
        """ Returns platform by instance type """
        found_platform: Optional[GenericPlatform] = None

        for platform in self.platforms:
            k8s_platform = self.get_k8s_platform(platform)
            if k8s_platform.is_allowed_instance(instance_type):

                # check for duplicate allowed instances
                if found_platform is not None:
                    raise ValueError(f'{instance_type} found on multiple' + f'platforms: {found_platform}, {platform}.')
                else:
                    found_platform = k8s_platform

        if found_platform is None:
            raise ValueError(f'Instance type {instance_type} not in allowed instances.')
        else:
            return found_platform

    def available_platforms(self) -> List[str]:
        """ Returns all available platforms by name"""
        return list(self._platforms.keys())

    def __iter__(self):
        """ allow iteration through the platforms, returning (name, platform) tuples"""
        return iter(self._platforms.items())
