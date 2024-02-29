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


from typing import Any, Dict
from pydantic import BaseModel, Field, StrictStr
from qovery.models.api_variable_scope_enum import APIVariableScopeEnum
from qovery.models.api_variable_type_enum import APIVariableTypeEnum

class EnvironmentVariableOverride(BaseModel):
    """
    EnvironmentVariableOverride
    """
    id: StrictStr = Field(...)
    key: StrictStr = Field(...)
    value: StrictStr = Field(...)
    mount_path: StrictStr = Field(...)
    scope: APIVariableScopeEnum = Field(...)
    variable_type: APIVariableTypeEnum = Field(...)
    additional_properties: Dict[str, Any] = {}
    __properties = ["id", "key", "value", "mount_path", "scope", "variable_type"]

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
    def from_json(cls, json_str: str) -> EnvironmentVariableOverride:
        """Create an instance of EnvironmentVariableOverride from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EnvironmentVariableOverride:
        """Create an instance of EnvironmentVariableOverride from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EnvironmentVariableOverride.parse_obj(obj)

        _obj = EnvironmentVariableOverride.parse_obj({
            "id": obj.get("id"),
            "key": obj.get("key"),
            "value": obj.get("value"),
            "mount_path": obj.get("mount_path"),
            "scope": obj.get("scope"),
            "variable_type": obj.get("variable_type")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


