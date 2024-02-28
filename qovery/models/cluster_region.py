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



from pydantic import BaseModel, Field, StrictStr

class ClusterRegion(BaseModel):
    """
    ClusterRegion
    """
    name: StrictStr = Field(...)
    country_code: StrictStr = Field(...)
    country: StrictStr = Field(...)
    city: StrictStr = Field(...)
    __properties = ["name", "country_code", "country", "city"]

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
    def from_json(cls, json_str: str) -> ClusterRegion:
        """Create an instance of ClusterRegion from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ClusterRegion:
        """Create an instance of ClusterRegion from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ClusterRegion.parse_obj(obj)

        _obj = ClusterRegion.parse_obj({
            "name": obj.get("name"),
            "country_code": obj.get("country_code"),
            "country": obj.get("country"),
            "city": obj.get("city")
        })
        return _obj


