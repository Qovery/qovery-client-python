# coding: utf-8

"""
    Qovery API

    - Qovery is the fastest way to deploy your full-stack apps on any Cloud provider. - ℹ️ The API is stable and still in development. 

    The version of the OpenAPI document: 1.0.3
    Contact: support+api+documentation@qovery.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class EnvironmentLogTypeEnum(str, Enum):
    """
    EnvironmentLogTypeEnum
    """

    """
    allowed enum values
    """
    APPLICATION = 'APPLICATION'
    DATABASE = 'DATABASE'
    ENVIRONMENT = 'ENVIRONMENT'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of EnvironmentLogTypeEnum from a JSON string"""
        return cls(json.loads(json_str))


