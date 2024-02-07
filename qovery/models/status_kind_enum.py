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


class StatusKindEnum(str, Enum):
    """
    StatusKindEnum
    """

    """
    allowed enum values
    """
    CANCELED = 'CANCELED'
    CANCELING = 'CANCELING'
    DELETED = 'DELETED'
    DELETE_ERROR = 'DELETE_ERROR'
    DELETE_IN_PROGRESS = 'DELETE_IN_PROGRESS'
    DEPLOYED = 'DEPLOYED'
    DEPLOYMENT_ERROR = 'DEPLOYMENT_ERROR'
    DEPLOYMENT_IN_PROGRESS = 'DEPLOYMENT_IN_PROGRESS'
    ERROR = 'ERROR'
    PAUSED = 'PAUSED'
    PAUSE_ERROR = 'PAUSE_ERROR'
    PAUSE_IN_PROGRESS = 'PAUSE_IN_PROGRESS'
    WAITING = 'WAITING'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of StatusKindEnum from a JSON string"""
        return cls(json.loads(json_str))


