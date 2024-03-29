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

from datetime import datetime
from typing import Any, Dict, Optional
from pydantic import BaseModel, StrictStr
from qovery.models.organization_event_origin import OrganizationEventOrigin
from qovery.models.organization_event_sub_target_type import OrganizationEventSubTargetType
from qovery.models.organization_event_target_type import OrganizationEventTargetType
from qovery.models.organization_event_type import OrganizationEventType

class OrganizationEventResponse(BaseModel):
    """
    OrganizationEventResponse
    """
    id: Optional[StrictStr] = None
    timestamp: Optional[datetime] = None
    event_type: Optional[OrganizationEventType] = None
    target_id: Optional[StrictStr] = None
    target_name: Optional[StrictStr] = None
    target_type: Optional[OrganizationEventTargetType] = None
    sub_target_type: Optional[OrganizationEventSubTargetType] = None
    change: Optional[StrictStr] = None
    origin: Optional[OrganizationEventOrigin] = None
    triggered_by: Optional[StrictStr] = None
    project_id: Optional[StrictStr] = None
    project_name: Optional[StrictStr] = None
    environment_id: Optional[StrictStr] = None
    environment_name: Optional[StrictStr] = None
    additional_properties: Dict[str, Any] = {}
    __properties = ["id", "timestamp", "event_type", "target_id", "target_name", "target_type", "sub_target_type", "change", "origin", "triggered_by", "project_id", "project_name", "environment_id", "environment_name"]

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
    def from_json(cls, json_str: str) -> OrganizationEventResponse:
        """Create an instance of OrganizationEventResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if target_id (nullable) is None
        # and __fields_set__ contains the field
        if self.target_id is None and "target_id" in self.__fields_set__:
            _dict['target_id'] = None

        # set to None if sub_target_type (nullable) is None
        # and __fields_set__ contains the field
        if self.sub_target_type is None and "sub_target_type" in self.__fields_set__:
            _dict['sub_target_type'] = None

        # set to None if project_id (nullable) is None
        # and __fields_set__ contains the field
        if self.project_id is None and "project_id" in self.__fields_set__:
            _dict['project_id'] = None

        # set to None if environment_id (nullable) is None
        # and __fields_set__ contains the field
        if self.environment_id is None and "environment_id" in self.__fields_set__:
            _dict['environment_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OrganizationEventResponse:
        """Create an instance of OrganizationEventResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OrganizationEventResponse.parse_obj(obj)

        _obj = OrganizationEventResponse.parse_obj({
            "id": obj.get("id"),
            "timestamp": obj.get("timestamp"),
            "event_type": obj.get("event_type"),
            "target_id": obj.get("target_id"),
            "target_name": obj.get("target_name"),
            "target_type": obj.get("target_type"),
            "sub_target_type": obj.get("sub_target_type"),
            "change": obj.get("change"),
            "origin": obj.get("origin"),
            "triggered_by": obj.get("triggered_by"),
            "project_id": obj.get("project_id"),
            "project_name": obj.get("project_name"),
            "environment_id": obj.get("environment_id"),
            "environment_name": obj.get("environment_name")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


