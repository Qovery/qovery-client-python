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


class OrganizationEventSubTargetType(str, Enum):
    """
    Type of the organization event
    """

    """
    allowed enum values
    """
    ADVANCED_SETTINGS = 'ADVANCED_SETTINGS'
    API_TOKEN = 'API_TOKEN'
    BILLING_INFO = 'BILLING_INFO'
    CLOUD_PROVIDER_CREDENTIALS = 'CLOUD_PROVIDER_CREDENTIALS'
    CLUSTER_CREDENTIALS = 'CLUSTER_CREDENTIALS'
    CLUSTER_ROUTING_TABLE = 'CLUSTER_ROUTING_TABLE'
    CONFIG = 'CONFIG'
    CREDIT_CARD = 'CREDIT_CARD'
    CREDIT_CODE = 'CREDIT_CODE'
    CUSTOM_DOMAIN = 'CUSTOM_DOMAIN'
    CUSTOM_ROLE = 'CUSTOM_ROLE'
    DEPLOYMENT_RULE = 'DEPLOYMENT_RULE'
    DEPLOYMENT_STAGE = 'DEPLOYMENT_STAGE'
    GITHUB_APP = 'GITHUB_APP'
    GIT_REPOSITORY = 'GIT_REPOSITORY'
    GIT_TOKEN = 'GIT_TOKEN'
    INVITATION = 'INVITATION'
    MEMBER_ROLE = 'MEMBER_ROLE'
    PLAN = 'PLAN'
    SECRET = 'SECRET'
    TERRAFORM = 'TERRAFORM'
    TRANSFER_OWNERSHIP = 'TRANSFER_OWNERSHIP'
    VARIABLE = 'VARIABLE'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of OrganizationEventSubTargetType from a JSON string"""
        return cls(json.loads(json_str))


