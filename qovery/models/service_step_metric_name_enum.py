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


class ServiceStepMetricNameEnum(str, Enum):
    """
    The name of the deployment step at the service level: - REGISTRY_CREATE_REPOSITORY: The step to create the repository in the registry. - GIT_CLONE: The step to clone the source code repository.  - BUILD_QUEUEING: The queuing time preceding the actual building step. - BUILD: The step to build the source code. - DEPLOYMENT_QUEUEING: The queuing time preceding the actual deployment step. - DEPLOYMENT: The step to deploy the service.  - ROUTER_DEPLOYMENT: The step to deploy the router.  - MIRROR_IMAGE: The step to mirror the image to the private registry. 
    """

    """
    allowed enum values
    """
    REGISTRY_CREATE_REPOSITORY = 'REGISTRY_CREATE_REPOSITORY'
    GIT_CLONE = 'GIT_CLONE'
    BUILD_QUEUEING = 'BUILD_QUEUEING'
    BUILD = 'BUILD'
    DEPLOYMENT_QUEUEING = 'DEPLOYMENT_QUEUEING'
    DEPLOYMENT = 'DEPLOYMENT'
    ROUTER_DEPLOYMENT = 'ROUTER_DEPLOYMENT'
    MIRROR_IMAGE = 'MIRROR_IMAGE'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ServiceStepMetricNameEnum from a JSON string"""
        return cls(json.loads(json_str))


