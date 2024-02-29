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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr
from qovery.models.api_variable_scope_enum import APIVariableScopeEnum

class VariableRequest(BaseModel):
    """
    VariableRequest
    """
    key: StrictStr = Field(..., description="the key of the environment variable")
    value: StrictStr = Field(..., description="the value of the environment variable")
    mount_path: Optional[StrictStr] = Field(None, description="the path where the file will be mounted (only if type =file)")
    is_secret: StrictBool = Field(..., description="if true, the variable will be considered as a secret and will not be accessible after its creation. Only your applications will be able to access its value at build and run time.")
    variable_scope: APIVariableScopeEnum = Field(...)
    variable_parent_id: StrictStr = Field(..., description="based on the selected scope, it contains the ID of the service, environment or project where the variable is attached")
    additional_properties: Dict[str, Any] = {}
    __properties = ["key", "value", "mount_path", "is_secret", "variable_scope", "variable_parent_id"]

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
    def from_json(cls, json_str: str) -> VariableRequest:
        """Create an instance of VariableRequest from a JSON string"""
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

        # set to None if mount_path (nullable) is None
        # and __fields_set__ contains the field
        if self.mount_path is None and "mount_path" in self.__fields_set__:
            _dict['mount_path'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VariableRequest:
        """Create an instance of VariableRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VariableRequest.parse_obj(obj)

        _obj = VariableRequest.parse_obj({
            "key": obj.get("key"),
            "value": obj.get("value"),
            "mount_path": obj.get("mount_path"),
            "is_secret": obj.get("is_secret"),
            "variable_scope": obj.get("variable_scope"),
            "variable_parent_id": obj.get("variable_parent_id")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


