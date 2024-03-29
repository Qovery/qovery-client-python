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
from pydantic import BaseModel, Field, StrictStr, validator
from qovery.models.cluster_logs_details import ClusterLogsDetails
from qovery.models.cluster_logs_error import ClusterLogsError
from qovery.models.cluster_logs_message import ClusterLogsMessage

class ClusterLogs(BaseModel):
    """
    ClusterLogs
    """
    type: Optional[StrictStr] = Field(None, description="log level")
    timestamp: Optional[datetime] = Field(None, description="log date creation")
    step: Optional[StrictStr] = Field(None, description="log step")
    message: Optional[ClusterLogsMessage] = None
    error: Optional[ClusterLogsError] = None
    details: Optional[ClusterLogsDetails] = None
    additional_properties: Dict[str, Any] = {}
    __properties = ["type", "timestamp", "step", "message", "error", "details"]

    @validator('step')
    def step_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('LoadConfiguration', 'Create', 'Created', 'CreateError', 'Pause', 'Paused', 'PauseError', 'Delete', 'Deleted', 'DeleteError', 'RetrieveClusterConfig', 'RetrieveClusterResources', 'ValidateSystemRequirements', 'UnderMigration', 'Unknown'):
            raise ValueError("must be one of enum values ('LoadConfiguration', 'Create', 'Created', 'CreateError', 'Pause', 'Paused', 'PauseError', 'Delete', 'Deleted', 'DeleteError', 'RetrieveClusterConfig', 'RetrieveClusterResources', 'ValidateSystemRequirements', 'UnderMigration', 'Unknown')")
        return value

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
    def from_json(cls, json_str: str) -> ClusterLogs:
        """Create an instance of ClusterLogs from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of message
        if self.message:
            _dict['message'] = self.message.to_dict()
        # override the default output from pydantic by calling `to_dict()` of error
        if self.error:
            _dict['error'] = self.error.to_dict()
        # override the default output from pydantic by calling `to_dict()` of details
        if self.details:
            _dict['details'] = self.details.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ClusterLogs:
        """Create an instance of ClusterLogs from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ClusterLogs.parse_obj(obj)

        _obj = ClusterLogs.parse_obj({
            "type": obj.get("type"),
            "timestamp": obj.get("timestamp"),
            "step": obj.get("step"),
            "message": ClusterLogsMessage.from_dict(obj.get("message")) if obj.get("message") is not None else None,
            "error": ClusterLogsError.from_dict(obj.get("error")) if obj.get("error") is not None else None,
            "details": ClusterLogsDetails.from_dict(obj.get("details")) if obj.get("details") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


