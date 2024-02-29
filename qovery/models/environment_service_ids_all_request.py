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


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, StrictStr, conlist

class EnvironmentServiceIdsAllRequest(BaseModel):
    """
    EnvironmentServiceIdsAllRequest
    """
    application_ids: Optional[conlist(StrictStr)] = None
    container_ids: Optional[conlist(StrictStr)] = None
    database_ids: Optional[conlist(StrictStr)] = None
    job_ids: Optional[conlist(StrictStr)] = None
    helm_ids: Optional[conlist(StrictStr)] = None
    additional_properties: Dict[str, Any] = {}
    __properties = ["application_ids", "container_ids", "database_ids", "job_ids", "helm_ids"]

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
    def from_json(cls, json_str: str) -> EnvironmentServiceIdsAllRequest:
        """Create an instance of EnvironmentServiceIdsAllRequest from a JSON string"""
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
    def from_dict(cls, obj: dict) -> EnvironmentServiceIdsAllRequest:
        """Create an instance of EnvironmentServiceIdsAllRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EnvironmentServiceIdsAllRequest.parse_obj(obj)

        _obj = EnvironmentServiceIdsAllRequest.parse_obj({
            "application_ids": obj.get("application_ids"),
            "container_ids": obj.get("container_ids"),
            "database_ids": obj.get("database_ids"),
            "job_ids": obj.get("job_ids"),
            "helm_ids": obj.get("helm_ids")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


