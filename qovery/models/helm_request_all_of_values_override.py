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
from pydantic import BaseModel, Field, StrictStr, conlist
from qovery.models.helm_request_all_of_values_override_file import HelmRequestAllOfValuesOverrideFile

class HelmRequestAllOfValuesOverride(BaseModel):
    """
    Specify helm values you want to set or override   # noqa: E501
    """
    set: Optional[conlist(conlist(StrictStr))] = Field(None, description="The input is in json array format: [ [$KEY,$VALUE], [...] ]")
    set_string: Optional[conlist(conlist(StrictStr))] = Field(None, description="The input is in json array format: [ [$KEY,$VALUE], [...] ]")
    set_json: Optional[conlist(conlist(StrictStr))] = Field(None, description="The input is in json array format: [ [$KEY,$VALUE], [...] ]")
    file: Optional[HelmRequestAllOfValuesOverrideFile] = None
    additional_properties: Dict[str, Any] = {}
    __properties = ["set", "set_string", "set_json", "file"]

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
    def from_json(cls, json_str: str) -> HelmRequestAllOfValuesOverride:
        """Create an instance of HelmRequestAllOfValuesOverride from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of file
        if self.file:
            _dict['file'] = self.file.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if file (nullable) is None
        # and __fields_set__ contains the field
        if self.file is None and "file" in self.__fields_set__:
            _dict['file'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> HelmRequestAllOfValuesOverride:
        """Create an instance of HelmRequestAllOfValuesOverride from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return HelmRequestAllOfValuesOverride.parse_obj(obj)

        _obj = HelmRequestAllOfValuesOverride.parse_obj({
            "set": obj.get("set"),
            "set_string": obj.get("set_string"),
            "set_json": obj.get("set_json"),
            "file": HelmRequestAllOfValuesOverrideFile.from_dict(obj.get("file")) if obj.get("file") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


