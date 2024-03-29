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


from typing import Any, Dict, List
from pydantic import BaseModel, Field, StrictBool, conlist
from qovery.models.variable_import_request_vars_inner import VariableImportRequestVarsInner

class VariableImportRequest(BaseModel):
    """
    VariableImportRequest
    """
    overwrite: StrictBool = Field(...)
    vars: conlist(VariableImportRequestVarsInner) = Field(...)
    additional_properties: Dict[str, Any] = {}
    __properties = ["overwrite", "vars"]

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
    def from_json(cls, json_str: str) -> VariableImportRequest:
        """Create an instance of VariableImportRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in vars (list)
        _items = []
        if self.vars:
            for _item in self.vars:
                if _item:
                    _items.append(_item.to_dict())
            _dict['vars'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VariableImportRequest:
        """Create an instance of VariableImportRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VariableImportRequest.parse_obj(obj)

        _obj = VariableImportRequest.parse_obj({
            "overwrite": obj.get("overwrite") if obj.get("overwrite") is not None else False,
            "vars": [VariableImportRequestVarsInner.from_dict(_item) for _item in obj.get("vars")] if obj.get("vars") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


