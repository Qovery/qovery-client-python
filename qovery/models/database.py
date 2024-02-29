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
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from qovery.models.database_accessibility_enum import DatabaseAccessibilityEnum
from qovery.models.database_mode_enum import DatabaseModeEnum
from qovery.models.database_type_enum import DatabaseTypeEnum
from qovery.models.reference_object import ReferenceObject

class Database(BaseModel):
    """
    Database
    """
    id: StrictStr = Field(...)
    created_at: datetime = Field(...)
    updated_at: Optional[datetime] = None
    name: StrictStr = Field(..., description="name is case insensitive")
    description: Optional[StrictStr] = Field(None, description="give a description to this database")
    type: DatabaseTypeEnum = Field(...)
    version: StrictStr = Field(...)
    mode: DatabaseModeEnum = Field(...)
    accessibility: Optional[DatabaseAccessibilityEnum] = None
    cpu: Optional[StrictInt] = Field(250, description="unit is millicores (m). 1000m = 1 cpu This field will be ignored for managed DB (instance type will be used instead). ")
    instance_type: Optional[StrictStr] = Field(None, description="Database instance type to be used for this database. The list of values can be retrieved via the endpoint /{CloudProvider}/managedDatabase/instanceType/{region}/{dbType}. This field is null for container DB.")
    memory: Optional[StrictInt] = Field(None, description="unit is MB. 1024 MB = 1GB This field will be ignored for managed DB (instance type will be used instead). Default value is linked to the database type: - MANAGED: `100` - CONTAINER   - POSTGRES: `100`   - REDIS: `100`   - MYSQL: `512`   - MONGODB: `256` ")
    storage: Optional[StrictInt] = Field(10, description="unit is GB")
    environment: ReferenceObject = Field(...)
    host: Optional[StrictStr] = None
    port: Optional[StrictInt] = None
    maximum_cpu: Optional[StrictInt] = Field(None, description="Maximum cpu that can be allocated to the database based on organization cluster configuration. unit is millicores (m). 1000m = 1 cpu")
    maximum_memory: Optional[StrictInt] = Field(None, description="Maximum memory that can be allocated to the database based on organization cluster configuration. unit is MB. 1024 MB = 1GB")
    disk_encrypted: Optional[StrictBool] = Field(None, description="indicates if the database disk is encrypted or not")
    additional_properties: Dict[str, Any] = {}
    __properties = ["id", "created_at", "updated_at", "name", "description", "type", "version", "mode", "accessibility", "cpu", "instance_type", "memory", "storage", "environment", "host", "port", "maximum_cpu", "maximum_memory", "disk_encrypted"]

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
    def from_json(cls, json_str: str) -> Database:
        """Create an instance of Database from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of environment
        if self.environment:
            _dict['environment'] = self.environment.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Database:
        """Create an instance of Database from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Database.parse_obj(obj)

        _obj = Database.parse_obj({
            "id": obj.get("id"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "type": obj.get("type"),
            "version": obj.get("version"),
            "mode": obj.get("mode"),
            "accessibility": obj.get("accessibility"),
            "cpu": obj.get("cpu") if obj.get("cpu") is not None else 250,
            "instance_type": obj.get("instance_type"),
            "memory": obj.get("memory"),
            "storage": obj.get("storage") if obj.get("storage") is not None else 10,
            "environment": ReferenceObject.from_dict(obj.get("environment")) if obj.get("environment") is not None else None,
            "host": obj.get("host"),
            "port": obj.get("port"),
            "maximum_cpu": obj.get("maximum_cpu"),
            "maximum_memory": obj.get("maximum_memory"),
            "disk_encrypted": obj.get("disk_encrypted")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


