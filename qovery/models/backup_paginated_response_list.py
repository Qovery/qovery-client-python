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


from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, conlist
from qovery.models.backup import Backup

class BackupPaginatedResponseList(BaseModel):
    """
    BackupPaginatedResponseList
    """
    page: Union[StrictFloat, StrictInt] = Field(...)
    page_size: Union[StrictFloat, StrictInt] = Field(...)
    results: Optional[conlist(Backup)] = None
    additional_properties: Dict[str, Any] = {}
    __properties = ["page", "page_size", "results"]

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
    def from_json(cls, json_str: str) -> BackupPaginatedResponseList:
        """Create an instance of BackupPaginatedResponseList from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in results (list)
        _items = []
        if self.results:
            for _item in self.results:
                if _item:
                    _items.append(_item.to_dict())
            _dict['results'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BackupPaginatedResponseList:
        """Create an instance of BackupPaginatedResponseList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BackupPaginatedResponseList.parse_obj(obj)

        _obj = BackupPaginatedResponseList.parse_obj({
            "page": obj.get("page"),
            "page_size": obj.get("page_size"),
            "results": [Backup.from_dict(_item) for _item in obj.get("results")] if obj.get("results") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


