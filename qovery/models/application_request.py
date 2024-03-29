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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conint, conlist
from qovery.models.application_git_repository_request import ApplicationGitRepositoryRequest
from qovery.models.build_mode_enum import BuildModeEnum
from qovery.models.build_pack_language_enum import BuildPackLanguageEnum
from qovery.models.healthcheck import Healthcheck
from qovery.models.service_port_request_ports_inner import ServicePortRequestPortsInner
from qovery.models.service_storage_request_storage_inner import ServiceStorageRequestStorageInner

class ApplicationRequest(BaseModel):
    """
    ApplicationRequest
    """
    storage: Optional[conlist(ServiceStorageRequestStorageInner)] = None
    ports: Optional[conlist(ServicePortRequestPortsInner)] = None
    name: StrictStr = Field(..., description="name is case insensitive")
    description: Optional[StrictStr] = Field(None, description="give a description to this application")
    git_repository: ApplicationGitRepositoryRequest = Field(...)
    build_mode: Optional[BuildModeEnum] = None
    dockerfile_path: Optional[StrictStr] = Field(None, description="The path of the associated Dockerfile. Only if you are using build_mode = DOCKER")
    buildpack_language: Optional[BuildPackLanguageEnum] = None
    cpu: Optional[StrictInt] = Field(500, description="unit is millicores (m). 1000m = 1 cpu")
    memory: Optional[StrictInt] = Field(512, description="unit is MB. 1024 MB = 1GB")
    min_running_instances: Optional[conint(strict=True, ge=0)] = Field(1, description="Minimum number of instances running. This resource auto-scale based on the CPU and Memory consumption. Note: 0 means that there is no application running. ")
    max_running_instances: Optional[StrictInt] = Field(1, description="Maximum number of instances running. This resource auto-scale based on the CPU and Memory consumption. Note: -1 means that there is no limit. ")
    healthchecks: Healthcheck = Field(...)
    auto_preview: Optional[StrictBool] = Field(True, description="Specify if the environment preview option is activated or not for this application.   If activated, a preview environment will be automatically cloned at each pull request.   If not specified, it takes the value of the `auto_preview` property from the associated environment. ")
    arguments: Optional[conlist(StrictStr)] = None
    entrypoint: Optional[StrictStr] = Field(None, description="optional entrypoint when launching container")
    auto_deploy: Optional[StrictBool] = Field(None, description="Specify if the application will be automatically updated after receiving a new commit.")
    additional_properties: Dict[str, Any] = {}
    __properties = ["storage", "ports", "name", "description", "git_repository", "build_mode", "dockerfile_path", "buildpack_language", "cpu", "memory", "min_running_instances", "max_running_instances", "healthchecks", "auto_preview", "arguments", "entrypoint", "auto_deploy"]

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
    def from_json(cls, json_str: str) -> ApplicationRequest:
        """Create an instance of ApplicationRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in storage (list)
        _items = []
        if self.storage:
            for _item in self.storage:
                if _item:
                    _items.append(_item.to_dict())
            _dict['storage'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in ports (list)
        _items = []
        if self.ports:
            for _item in self.ports:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ports'] = _items
        # override the default output from pydantic by calling `to_dict()` of git_repository
        if self.git_repository:
            _dict['git_repository'] = self.git_repository.to_dict()
        # override the default output from pydantic by calling `to_dict()` of healthchecks
        if self.healthchecks:
            _dict['healthchecks'] = self.healthchecks.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if dockerfile_path (nullable) is None
        # and __fields_set__ contains the field
        if self.dockerfile_path is None and "dockerfile_path" in self.__fields_set__:
            _dict['dockerfile_path'] = None

        # set to None if buildpack_language (nullable) is None
        # and __fields_set__ contains the field
        if self.buildpack_language is None and "buildpack_language" in self.__fields_set__:
            _dict['buildpack_language'] = None

        # set to None if auto_deploy (nullable) is None
        # and __fields_set__ contains the field
        if self.auto_deploy is None and "auto_deploy" in self.__fields_set__:
            _dict['auto_deploy'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApplicationRequest:
        """Create an instance of ApplicationRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApplicationRequest.parse_obj(obj)

        _obj = ApplicationRequest.parse_obj({
            "storage": [ServiceStorageRequestStorageInner.from_dict(_item) for _item in obj.get("storage")] if obj.get("storage") is not None else None,
            "ports": [ServicePortRequestPortsInner.from_dict(_item) for _item in obj.get("ports")] if obj.get("ports") is not None else None,
            "name": obj.get("name"),
            "description": obj.get("description"),
            "git_repository": ApplicationGitRepositoryRequest.from_dict(obj.get("git_repository")) if obj.get("git_repository") is not None else None,
            "build_mode": obj.get("build_mode"),
            "dockerfile_path": obj.get("dockerfile_path"),
            "buildpack_language": obj.get("buildpack_language"),
            "cpu": obj.get("cpu") if obj.get("cpu") is not None else 500,
            "memory": obj.get("memory") if obj.get("memory") is not None else 512,
            "min_running_instances": obj.get("min_running_instances") if obj.get("min_running_instances") is not None else 1,
            "max_running_instances": obj.get("max_running_instances") if obj.get("max_running_instances") is not None else 1,
            "healthchecks": Healthcheck.from_dict(obj.get("healthchecks")) if obj.get("healthchecks") is not None else None,
            "auto_preview": obj.get("auto_preview") if obj.get("auto_preview") is not None else True,
            "arguments": obj.get("arguments"),
            "entrypoint": obj.get("entrypoint"),
            "auto_deploy": obj.get("auto_deploy")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


