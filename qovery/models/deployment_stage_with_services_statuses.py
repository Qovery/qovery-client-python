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
from qovery.models.stage import Stage
from qovery.models.status import Status

class DeploymentStageWithServicesStatuses(BaseModel):
    """
    DeploymentStageWithServicesStatuses
    """
    applications: Optional[conlist(Status)] = None
    containers: Optional[conlist(Status)] = None
    jobs: Optional[conlist(Status)] = None
    databases: Optional[conlist(Status)] = None
    helms: Optional[conlist(Status)] = None
    stage: Optional[Stage] = None
    __properties = ["applications", "containers", "jobs", "databases", "helms", "stage"]

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
    def from_json(cls, json_str: str) -> DeploymentStageWithServicesStatuses:
        """Create an instance of DeploymentStageWithServicesStatuses from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in applications (list)
        _items = []
        if self.applications:
            for _item in self.applications:
                if _item:
                    _items.append(_item.to_dict())
            _dict['applications'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in containers (list)
        _items = []
        if self.containers:
            for _item in self.containers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['containers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in jobs (list)
        _items = []
        if self.jobs:
            for _item in self.jobs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['jobs'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in databases (list)
        _items = []
        if self.databases:
            for _item in self.databases:
                if _item:
                    _items.append(_item.to_dict())
            _dict['databases'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in helms (list)
        _items = []
        if self.helms:
            for _item in self.helms:
                if _item:
                    _items.append(_item.to_dict())
            _dict['helms'] = _items
        # override the default output from pydantic by calling `to_dict()` of stage
        if self.stage:
            _dict['stage'] = self.stage.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DeploymentStageWithServicesStatuses:
        """Create an instance of DeploymentStageWithServicesStatuses from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DeploymentStageWithServicesStatuses.parse_obj(obj)

        _obj = DeploymentStageWithServicesStatuses.parse_obj({
            "applications": [Status.from_dict(_item) for _item in obj.get("applications")] if obj.get("applications") is not None else None,
            "containers": [Status.from_dict(_item) for _item in obj.get("containers")] if obj.get("containers") is not None else None,
            "jobs": [Status.from_dict(_item) for _item in obj.get("jobs")] if obj.get("jobs") is not None else None,
            "databases": [Status.from_dict(_item) for _item in obj.get("databases")] if obj.get("databases") is not None else None,
            "helms": [Status.from_dict(_item) for _item in obj.get("helms")] if obj.get("helms") is not None else None,
            "stage": Stage.from_dict(obj.get("stage")) if obj.get("stage") is not None else None
        })
        return _obj


