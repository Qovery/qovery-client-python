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





class TypeOfUseEnum(str, Enum):
    """
    TypeOfUseEnum
    """

    """
    allowed enum values
    """
    PERSONAL = 'PERSONAL'
    SCHOOL = 'SCHOOL'
    WORK = 'WORK'

    @classmethod
    def from_json(cls, json_str: str) -> TypeOfUseEnum:
        """Create an instance of TypeOfUseEnum from a JSON string"""
        return TypeOfUseEnum(json.loads(json_str))


