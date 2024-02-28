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





class CreateEnvironmentModeEnum(str, Enum):
    """
    CreateEnvironmentModeEnum
    """

    """
    allowed enum values
    """
    DEVELOPMENT = 'DEVELOPMENT'
    PRODUCTION = 'PRODUCTION'
    STAGING = 'STAGING'

    @classmethod
    def from_json(cls, json_str: str) -> CreateEnvironmentModeEnum:
        """Create an instance of CreateEnvironmentModeEnum from a JSON string"""
        return CreateEnvironmentModeEnum(json.loads(json_str))


