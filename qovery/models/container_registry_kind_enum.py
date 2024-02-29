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





class ContainerRegistryKindEnum(str, Enum):
    """
    The type of your container registry
    """

    """
    allowed enum values
    """
    ECR = 'ECR'
    SCALEWAY_CR = 'SCALEWAY_CR'
    DOCKER_HUB = 'DOCKER_HUB'
    GITHUB_CR = 'GITHUB_CR'
    GITLAB_CR = 'GITLAB_CR'
    PUBLIC_ECR = 'PUBLIC_ECR'
    DOCR = 'DOCR'
    GENERIC_CR = 'GENERIC_CR'
    GCP_ARTIFACT_REGISTRY = 'GCP_ARTIFACT_REGISTRY'

    @classmethod
    def from_json(cls, json_str: str) -> ContainerRegistryKindEnum:
        """Create an instance of ContainerRegistryKindEnum from a JSON string"""
        return ContainerRegistryKindEnum(json.loads(json_str))


