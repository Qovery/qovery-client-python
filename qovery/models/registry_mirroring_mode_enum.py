# coding: utf-8

"""
    Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is stable and still in development. 

    The version of the OpenAPI document: 1.0.3
    Contact: support+api+documentation@qovery.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class RegistryMirroringModeEnum(str, Enum):
    """
    Mirroring mode when deploying a service from a container registry - CLUSTER: This is not available on Scaleway. Images within the mirroring registry are organized by \"Qovery cluster\", meaning that the application deployed on the same cluster are all mirrored on the same repository. - SERVICE: Images within the mirroring registry are organized by \"Qovery service\", each service has its own repository 
    """

    """
    allowed enum values
    """
    CLUSTER = 'CLUSTER'
    SERVICE = 'SERVICE'

    @classmethod
    def from_json(cls, json_str: str) -> RegistryMirroringModeEnum:
        """Create an instance of RegistryMirroringModeEnum from a JSON string"""
        return RegistryMirroringModeEnum(json.loads(json_str))


