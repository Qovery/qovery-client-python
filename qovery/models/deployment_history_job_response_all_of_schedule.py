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
from qovery.models.job_schedule_event import JobScheduleEvent

class DeploymentHistoryJobResponseAllOfSchedule(BaseModel):
    """
    DeploymentHistoryJobResponseAllOfSchedule
    """
    event: Optional[JobScheduleEvent] = None
    schedule_at: Optional[StrictStr] = Field(None, description="Can only be set if the event is CRON. Represent the cron format for the job schedule without seconds. For example: `* * * * *` represent the cron to launch the job every minute. See https://crontab.guru/ to WISIWIG interface. Timezone is UTC ")
    additional_properties: Dict[str, Any] = {}
    __properties = ["event", "schedule_at"]

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
    def from_json(cls, json_str: str) -> DeploymentHistoryJobResponseAllOfSchedule:
        """Create an instance of DeploymentHistoryJobResponseAllOfSchedule from a JSON string"""
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

        # set to None if schedule_at (nullable) is None
        # and __fields_set__ contains the field
        if self.schedule_at is None and "schedule_at" in self.__fields_set__:
            _dict['schedule_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DeploymentHistoryJobResponseAllOfSchedule:
        """Create an instance of DeploymentHistoryJobResponseAllOfSchedule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DeploymentHistoryJobResponseAllOfSchedule.parse_obj(obj)

        _obj = DeploymentHistoryJobResponseAllOfSchedule.parse_obj({
            "event": obj.get("event"),
            "schedule_at": obj.get("schedule_at")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


