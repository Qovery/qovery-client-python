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
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr
from qovery.models.service_deployment_status_enum import ServiceDeploymentStatusEnum
from qovery.models.service_step_metrics import ServiceStepMetrics
from qovery.models.state_enum import StateEnum
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Status(BaseModel):
    """
    Status
    """ # noqa: E501
    id: StrictStr
    state: StateEnum
    service_deployment_status: ServiceDeploymentStatusEnum
    last_deployment_date: Optional[datetime] = None
    is_part_last_deployment: Optional[StrictBool] = None
    steps: Optional[ServiceStepMetrics] = None
    __properties: ClassVar[List[str]] = ["id", "state", "service_deployment_status", "last_deployment_date", "is_part_last_deployment", "steps"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Status from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of steps
        if self.steps:
            _dict['steps'] = self.steps.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Status from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "state": obj.get("state"),
            "service_deployment_status": obj.get("service_deployment_status"),
            "last_deployment_date": obj.get("last_deployment_date"),
            "is_part_last_deployment": obj.get("is_part_last_deployment"),
            "steps": ServiceStepMetrics.from_dict(obj.get("steps")) if obj.get("steps") is not None else None
        })
        return _obj


