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





class OrganizationEventType(str, Enum):
    """
    Type of the organization event
    """

    """
    allowed enum values
    """
    CREATE = 'CREATE'
    UPDATE = 'UPDATE'
    DELETE = 'DELETE'
    ACCEPT = 'ACCEPT'
    EXPORT = 'EXPORT'
    TRIGGER_DEPLOY = 'TRIGGER_DEPLOY'
    TRIGGER_REDEPLOY = 'TRIGGER_REDEPLOY'
    TRIGGER_STOP = 'TRIGGER_STOP'
    TRIGGER_CANCEL = 'TRIGGER_CANCEL'
    TRIGGER_RESTART = 'TRIGGER_RESTART'
    TRIGGER_DELETE = 'TRIGGER_DELETE'

    @classmethod
    def from_json(cls, json_str: str) -> OrganizationEventType:
        """Create an instance of OrganizationEventType from a JSON string"""
        return OrganizationEventType(json.loads(json_str))


