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


from typing import List, Optional
from pydantic import BaseModel, conlist
from qovery.models.managed_database_type_response import ManagedDatabaseTypeResponse

class ManagedDatabaseTypeResponseList(BaseModel):
    """
    ManagedDatabaseTypeResponseList
    """
    results: Optional[conlist(ManagedDatabaseTypeResponse)] = None
    __properties = ["results"]

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
    def from_json(cls, json_str: str) -> ManagedDatabaseTypeResponseList:
        """Create an instance of ManagedDatabaseTypeResponseList from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in results (list)
        _items = []
        if self.results:
            for _item in self.results:
                if _item:
                    _items.append(_item.to_dict())
            _dict['results'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ManagedDatabaseTypeResponseList:
        """Create an instance of ManagedDatabaseTypeResponseList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ManagedDatabaseTypeResponseList.parse_obj(obj)

        _obj = ManagedDatabaseTypeResponseList.parse_obj({
            "results": [ManagedDatabaseTypeResponse.from_dict(_item) for _item in obj.get("results")] if obj.get("results") is not None else None
        })
        return _obj


