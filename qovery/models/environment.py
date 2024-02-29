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
from pydantic import BaseModel, Field, StrictStr
from qovery.models.environment_all_of_cloud_provider import EnvironmentAllOfCloudProvider
from qovery.models.environment_mode_enum import EnvironmentModeEnum
from qovery.models.reference_object import ReferenceObject

class Environment(BaseModel):
    """
    Environment
    """
    id: StrictStr = Field(...)
    created_at: datetime = Field(...)
    updated_at: Optional[datetime] = None
    name: StrictStr = Field(..., description="name is case insensitive")
    organization: ReferenceObject = Field(...)
    project: ReferenceObject = Field(...)
    last_updated_by: Optional[StrictStr] = Field(None, description="uuid of the user that made the last update")
    cloud_provider: EnvironmentAllOfCloudProvider = Field(...)
    mode: EnvironmentModeEnum = Field(...)
    cluster_id: StrictStr = Field(...)
    cluster_name: Optional[StrictStr] = None
    additional_properties: Dict[str, Any] = {}
    __properties = ["id", "created_at", "updated_at", "name", "organization", "project", "last_updated_by", "cloud_provider", "mode", "cluster_id", "cluster_name"]

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
    def from_json(cls, json_str: str) -> Environment:
        """Create an instance of Environment from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of organization
        if self.organization:
            _dict['organization'] = self.organization.to_dict()
        # override the default output from pydantic by calling `to_dict()` of project
        if self.project:
            _dict['project'] = self.project.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cloud_provider
        if self.cloud_provider:
            _dict['cloud_provider'] = self.cloud_provider.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Environment:
        """Create an instance of Environment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Environment.parse_obj(obj)

        _obj = Environment.parse_obj({
            "id": obj.get("id"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "name": obj.get("name"),
            "organization": ReferenceObject.from_dict(obj.get("organization")) if obj.get("organization") is not None else None,
            "project": ReferenceObject.from_dict(obj.get("project")) if obj.get("project") is not None else None,
            "last_updated_by": obj.get("last_updated_by"),
            "cloud_provider": EnvironmentAllOfCloudProvider.from_dict(obj.get("cloud_provider")) if obj.get("cloud_provider") is not None else None,
            "mode": obj.get("mode"),
            "cluster_id": obj.get("cluster_id"),
            "cluster_name": obj.get("cluster_name")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


