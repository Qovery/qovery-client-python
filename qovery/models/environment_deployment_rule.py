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
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist
from qovery.models.weekday_enum import WeekdayEnum

class EnvironmentDeploymentRule(BaseModel):
    """
    EnvironmentDeploymentRule
    """
    id: StrictStr = Field(...)
    created_at: datetime = Field(...)
    updated_at: Optional[datetime] = None
    on_demand_preview: Optional[StrictBool] = False
    auto_stop: Optional[StrictBool] = False
    auto_preview: Optional[StrictBool] = False
    timezone: StrictStr = Field(...)
    start_time: datetime = Field(...)
    stop_time: datetime = Field(...)
    weekdays: conlist(WeekdayEnum) = Field(...)
    additional_properties: Dict[str, Any] = {}
    __properties = ["id", "created_at", "updated_at", "on_demand_preview", "auto_stop", "auto_preview", "timezone", "start_time", "stop_time", "weekdays"]

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
    def from_json(cls, json_str: str) -> EnvironmentDeploymentRule:
        """Create an instance of EnvironmentDeploymentRule from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "id",
                            "created_at",
                            "updated_at",
                            "additional_properties"
                          },
                          exclude_none=True)
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EnvironmentDeploymentRule:
        """Create an instance of EnvironmentDeploymentRule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EnvironmentDeploymentRule.parse_obj(obj)

        _obj = EnvironmentDeploymentRule.parse_obj({
            "id": obj.get("id"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "on_demand_preview": obj.get("on_demand_preview") if obj.get("on_demand_preview") is not None else False,
            "auto_stop": obj.get("auto_stop") if obj.get("auto_stop") is not None else False,
            "auto_preview": obj.get("auto_preview") if obj.get("auto_preview") is not None else False,
            "timezone": obj.get("timezone"),
            "start_time": obj.get("start_time"),
            "stop_time": obj.get("stop_time"),
            "weekdays": obj.get("weekdays")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


