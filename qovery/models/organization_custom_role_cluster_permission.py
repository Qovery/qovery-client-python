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





class OrganizationCustomRoleClusterPermission(str, Enum):
    """
    Indicates the permission for a target cluster, from the lowest to the highest: - `VIEWER` user has only read access on target cluster - `ENV_CREATOR` user can deploy on the cluster - `ADMIN` user can modify the cluster settings 
    """

    """
    allowed enum values
    """
    VIEWER = 'VIEWER'
    ENV_CREATOR = 'ENV_CREATOR'
    ADMIN = 'ADMIN'

    @classmethod
    def from_json(cls, json_str: str) -> OrganizationCustomRoleClusterPermission:
        """Create an instance of OrganizationCustomRoleClusterPermission from a JSON string"""
        return OrganizationCustomRoleClusterPermission(json.loads(json_str))

