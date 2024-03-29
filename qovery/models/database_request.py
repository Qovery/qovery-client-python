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
from pydantic import BaseModel, Field, StrictInt, StrictStr
from qovery.models.database_accessibility_enum import DatabaseAccessibilityEnum
from qovery.models.database_mode_enum import DatabaseModeEnum
from qovery.models.database_type_enum import DatabaseTypeEnum

class DatabaseRequest(BaseModel):
    """
    DatabaseRequest
    """
    name: StrictStr = Field(..., description="name is case insensitive")
    description: Optional[StrictStr] = Field(None, description="give a description to this database")
    type: DatabaseTypeEnum = Field(...)
    version: StrictStr = Field(...)
    mode: DatabaseModeEnum = Field(...)
    accessibility: Optional[DatabaseAccessibilityEnum] = None
    cpu: Optional[StrictInt] = Field(250, description="unit is millicores (m). 1000m = 1 cpu This field will be ignored for managed DB (instance type will be used instead). ")
    instance_type: Optional[StrictStr] = Field(None, description="Database instance type to be used for this database. The list of values can be retrieved via the endpoint /{CloudProvider}/managedDatabase/instanceType/{region}/{dbType}. This field SHOULD NOT be set for container DB.")
    memory: Optional[StrictInt] = Field(None, description="unit is MB. 1024 MB = 1GB This field will be ignored for managed DB (instance type will be used instead). Default value is linked to the database type: - MANAGED: `100` - CONTAINER   - POSTGRES: `100`   - REDIS: `100`   - MYSQL: `512`   - MONGODB: `256` ")
    storage: Optional[StrictInt] = Field(10, description="unit is GB")
    additional_properties: Dict[str, Any] = {}
    __properties = ["name", "description", "type", "version", "mode", "accessibility", "cpu", "instance_type", "memory", "storage"]

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
    def from_json(cls, json_str: str) -> DatabaseRequest:
        """Create an instance of DatabaseRequest from a JSON string"""
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
    def from_dict(cls, obj: dict) -> DatabaseRequest:
        """Create an instance of DatabaseRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DatabaseRequest.parse_obj(obj)

        _obj = DatabaseRequest.parse_obj({
            "name": obj.get("name"),
            "description": obj.get("description"),
            "type": obj.get("type"),
            "version": obj.get("version"),
            "mode": obj.get("mode"),
            "accessibility": obj.get("accessibility"),
            "cpu": obj.get("cpu") if obj.get("cpu") is not None else 250,
            "instance_type": obj.get("instance_type"),
            "memory": obj.get("memory"),
            "storage": obj.get("storage") if obj.get("storage") is not None else 10
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


