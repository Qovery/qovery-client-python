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
from qovery.models.job_request_all_of_source_docker import JobRequestAllOfSourceDocker
from qovery.models.job_request_all_of_source_image import JobRequestAllOfSourceImage

class JobRequestAllOfSource(BaseModel):
    """
    JobRequestAllOfSource
    """
    image: Optional[JobRequestAllOfSourceImage] = None
    docker: Optional[JobRequestAllOfSourceDocker] = None
    __properties = ["image", "docker"]

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
    def from_json(cls, json_str: str) -> JobRequestAllOfSource:
        """Create an instance of JobRequestAllOfSource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of image
        if self.image:
            _dict['image'] = self.image.to_dict()
        # override the default output from pydantic by calling `to_dict()` of docker
        if self.docker:
            _dict['docker'] = self.docker.to_dict()
        # set to None if image (nullable) is None
        # and __fields_set__ contains the field
        if self.image is None and "image" in self.__fields_set__:
            _dict['image'] = None

        # set to None if docker (nullable) is None
        # and __fields_set__ contains the field
        if self.docker is None and "docker" in self.__fields_set__:
            _dict['docker'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> JobRequestAllOfSource:
        """Create an instance of JobRequestAllOfSource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return JobRequestAllOfSource.parse_obj(obj)

        _obj = JobRequestAllOfSource.parse_obj({
            "image": JobRequestAllOfSourceImage.from_dict(obj.get("image")) if obj.get("image") is not None else None,
            "docker": JobRequestAllOfSourceDocker.from_dict(obj.get("docker")) if obj.get("docker") is not None else None
        })
        return _obj


