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


from typing import Optional
from pydantic import BaseModel
from qovery.models.helm_response_all_of_source_one_of_git import HelmResponseAllOfSourceOneOfGit

class HelmResponseAllOfSourceOneOf(BaseModel):
    """
    HelmResponseAllOfSourceOneOf
    """
    git: Optional[HelmResponseAllOfSourceOneOfGit] = None
    __properties = ["git"]

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
    def from_json(cls, json_str: str) -> HelmResponseAllOfSourceOneOf:
        """Create an instance of HelmResponseAllOfSourceOneOf from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of git
        if self.git:
            _dict['git'] = self.git.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> HelmResponseAllOfSourceOneOf:
        """Create an instance of HelmResponseAllOfSourceOneOf from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return HelmResponseAllOfSourceOneOf.parse_obj(obj)

        _obj = HelmResponseAllOfSourceOneOf.parse_obj({
            "git": HelmResponseAllOfSourceOneOfGit.from_dict(obj.get("git")) if obj.get("git") is not None else None
        })
        return _obj


