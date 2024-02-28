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


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr
from qovery.models.environment_mode_enum import EnvironmentModeEnum

class CloneEnvironmentRequest(BaseModel):
    """
    CloneEnvironmentRequest
    """
    name: StrictStr = Field(..., description="name is case insensitive")
    cluster_id: Optional[StrictStr] = None
    mode: Optional[EnvironmentModeEnum] = None
    apply_deployment_rule: Optional[StrictBool] = False
    __properties = ["name", "cluster_id", "mode", "apply_deployment_rule"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> CloneEnvironmentRequest:
        """Create an instance of CloneEnvironmentRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CloneEnvironmentRequest:
        """Create an instance of CloneEnvironmentRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CloneEnvironmentRequest.parse_obj(obj)

        _obj = CloneEnvironmentRequest.parse_obj({
            "name": obj.get("name"),
            "cluster_id": obj.get("cluster_id"),
            "mode": obj.get("mode"),
            "apply_deployment_rule": obj.get("apply_deployment_rule") if obj.get("apply_deployment_rule") is not None else False
        })
        return _obj


