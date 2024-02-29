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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr
from qovery.models.application_git_repository import ApplicationGitRepository

class BaseJobResponseAllOfSourceOneOf1Docker(BaseModel):
    """
    BaseJobResponseAllOfSourceOneOf1Docker
    """
    dockerfile_path: Optional[StrictStr] = Field(None, description="The path of the associated Dockerfile. Only if you are using build_mode = DOCKER")
    git_repository: Optional[ApplicationGitRepository] = None
    additional_properties: Dict[str, Any] = {}
    __properties = ["dockerfile_path", "git_repository"]

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
    def from_json(cls, json_str: str) -> BaseJobResponseAllOfSourceOneOf1Docker:
        """Create an instance of BaseJobResponseAllOfSourceOneOf1Docker from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of git_repository
        if self.git_repository:
            _dict['git_repository'] = self.git_repository.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if dockerfile_path (nullable) is None
        # and __fields_set__ contains the field
        if self.dockerfile_path is None and "dockerfile_path" in self.__fields_set__:
            _dict['dockerfile_path'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BaseJobResponseAllOfSourceOneOf1Docker:
        """Create an instance of BaseJobResponseAllOfSourceOneOf1Docker from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BaseJobResponseAllOfSourceOneOf1Docker.parse_obj(obj)

        _obj = BaseJobResponseAllOfSourceOneOf1Docker.parse_obj({
            "dockerfile_path": obj.get("dockerfile_path"),
            "git_repository": ApplicationGitRepository.from_dict(obj.get("git_repository")) if obj.get("git_repository") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


