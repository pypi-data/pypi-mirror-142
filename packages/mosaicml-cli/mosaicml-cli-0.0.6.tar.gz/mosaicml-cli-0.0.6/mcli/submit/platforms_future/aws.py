# pylint: disable=duplicate-code

""" The AWS Platform """
from dataclasses import dataclass

from mcli.submit.platforms_future.aws_instances import AWS_INSTANCE_LIST
from mcli.submit.platforms_future.instance_type import InstanceList
from mcli.submit.platforms_future.platform import GenericPlatform


@dataclass
class AWSPlatform(GenericPlatform):
    """ The AWS Platform """

    allowed_instances: InstanceList = AWS_INSTANCE_LIST
