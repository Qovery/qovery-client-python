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
from qovery.models.commit import Commit
from qovery.models.state_enum import StateEnum

class DeploymentHistoryApplication(BaseModel):
    """
    DeploymentHistoryApplication
    """
    id: StrictStr = Field(...)
    created_at: datetime = Field(...)
    updated_at: Optional[datetime] = None
    name: Optional[StrictStr] = None
    commit: Optional[Commit] = None
    status: Optional[StateEnum] = None
    additional_properties: Dict[str, Any] = {}
    __properties = ["id", "created_at", "updated_at", "name", "commit", "status"]

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
    def from_json(cls, json_str: str) -> DeploymentHistoryApplication:
        """Create an instance of DeploymentHistoryApplication from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of commit
        if self.commit:
            _dict['commit'] = self.commit.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if commit (nullable) is None
        # and __fields_set__ contains the field
        if self.commit is None and "commit" in self.__fields_set__:
            _dict['commit'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DeploymentHistoryApplication:
        """Create an instance of DeploymentHistoryApplication from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DeploymentHistoryApplication.parse_obj(obj)

        _obj = DeploymentHistoryApplication.parse_obj({
            "id": obj.get("id"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "name": obj.get("name"),
            "commit": Commit.from_dict(obj.get("commit")) if obj.get("commit") is not None else None,
            "status": obj.get("status")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

