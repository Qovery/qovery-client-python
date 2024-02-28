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
from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from qovery.models.environment_logs_details import EnvironmentLogsDetails
from qovery.models.environment_logs_error import EnvironmentLogsError
from qovery.models.environment_logs_message import EnvironmentLogsMessage

class EnvironmentLogs(BaseModel):
    """
    EnvironmentLogs
    """
    type: StrictStr = Field(...)
    timestamp: datetime = Field(...)
    details: EnvironmentLogsDetails = Field(...)
    error: Optional[EnvironmentLogsError] = None
    message: Optional[EnvironmentLogsMessage] = None
    __properties = ["type", "timestamp", "details", "error", "message"]

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
    def from_json(cls, json_str: str) -> EnvironmentLogs:
        """Create an instance of EnvironmentLogs from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of details
        if self.details:
            _dict['details'] = self.details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of error
        if self.error:
            _dict['error'] = self.error.to_dict()
        # override the default output from pydantic by calling `to_dict()` of message
        if self.message:
            _dict['message'] = self.message.to_dict()
        # set to None if error (nullable) is None
        # and __fields_set__ contains the field
        if self.error is None and "error" in self.__fields_set__:
            _dict['error'] = None

        # set to None if message (nullable) is None
        # and __fields_set__ contains the field
        if self.message is None and "message" in self.__fields_set__:
            _dict['message'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EnvironmentLogs:
        """Create an instance of EnvironmentLogs from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EnvironmentLogs.parse_obj(obj)

        _obj = EnvironmentLogs.parse_obj({
            "type": obj.get("type"),
            "timestamp": obj.get("timestamp"),
            "details": EnvironmentLogsDetails.from_dict(obj.get("details")) if obj.get("details") is not None else None,
            "error": EnvironmentLogsError.from_dict(obj.get("error")) if obj.get("error") is not None else None,
            "message": EnvironmentLogsMessage.from_dict(obj.get("message")) if obj.get("message") is not None else None
        })
        return _obj


