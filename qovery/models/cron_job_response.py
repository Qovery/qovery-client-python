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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conint, validator
from qovery.models.base_job_response_all_of_source import BaseJobResponseAllOfSource
from qovery.models.cron_job_response_all_of_schedule import CronJobResponseAllOfSchedule
from qovery.models.healthcheck import Healthcheck
from qovery.models.reference_object import ReferenceObject

class CronJobResponse(BaseModel):
    """
    CronJobResponse
    """
    id: StrictStr = Field(...)
    created_at: datetime = Field(...)
    updated_at: Optional[datetime] = None
    environment: ReferenceObject = Field(...)
    maximum_cpu: StrictInt = Field(..., description="Maximum cpu that can be allocated to the job based on organization cluster configuration. unit is millicores (m). 1000m = 1 cpu")
    maximum_memory: StrictInt = Field(..., description="Maximum memory that can be allocated to the job based on organization cluster configuration. unit is MB. 1024 MB = 1GB")
    name: StrictStr = Field(..., description="name is case insensitive")
    description: Optional[StrictStr] = None
    cpu: StrictInt = Field(..., description="unit is millicores (m). 1000m = 1 cpu")
    memory: StrictInt = Field(..., description="unit is MB. 1024 MB = 1GB")
    max_nb_restart: Optional[conint(strict=True, ge=0)] = Field(None, description="Maximum number of restart allowed before the job is considered as failed 0 means that no restart/crash of the job is allowed ")
    max_duration_seconds: Optional[conint(strict=True, ge=0)] = Field(None, description="Maximum number of seconds allowed for the job to run before killing it and mark it as failed ")
    auto_preview: StrictBool = Field(..., description="Indicates if the 'environment preview option' is enabled for this container.   If enabled, a preview environment will be automatically cloned when `/preview` endpoint is called.   If not specified, it takes the value of the `auto_preview` property from the associated environment. ")
    port: Optional[conint(strict=True, ge=1)] = Field(None, description="Port where to run readiness and liveliness probes checks. The port will not be exposed externally")
    source: BaseJobResponseAllOfSource = Field(...)
    healthchecks: Healthcheck = Field(...)
    auto_deploy: Optional[StrictBool] = Field(None, description="Specify if the job will be automatically updated after receiving a new image tag or a new commit according to the source type.  The new image tag shall be communicated via the \"Auto Deploy job\" endpoint https://api-doc.qovery.com/#tag/Jobs/operation/autoDeployJobEnvironments ")
    job_type: StrictStr = Field(...)
    schedule: CronJobResponseAllOfSchedule = Field(...)
    additional_properties: Dict[str, Any] = {}
    __properties = ["id", "created_at", "updated_at", "environment", "maximum_cpu", "maximum_memory", "name", "description", "cpu", "memory", "max_nb_restart", "max_duration_seconds", "auto_preview", "port", "source", "healthchecks", "auto_deploy", "job_type", "schedule"]

    @validator('job_type')
    def job_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('CRON'):
            raise ValueError("must be one of enum values ('CRON')")
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
    def from_json(cls, json_str: str) -> CronJobResponse:
        """Create an instance of CronJobResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "id",
                            "created_at",
                            "updated_at",
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of environment
        if self.environment:
            _dict['environment'] = self.environment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        # override the default output from pydantic by calling `to_dict()` of healthchecks
        if self.healthchecks:
            _dict['healthchecks'] = self.healthchecks.to_dict()
        # override the default output from pydantic by calling `to_dict()` of schedule
        if self.schedule:
            _dict['schedule'] = self.schedule.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if port (nullable) is None
        # and __fields_set__ contains the field
        if self.port is None and "port" in self.__fields_set__:
            _dict['port'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CronJobResponse:
        """Create an instance of CronJobResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CronJobResponse.parse_obj(obj)

        _obj = CronJobResponse.parse_obj({
            "id": obj.get("id"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "environment": ReferenceObject.from_dict(obj.get("environment")) if obj.get("environment") is not None else None,
            "maximum_cpu": obj.get("maximum_cpu"),
            "maximum_memory": obj.get("maximum_memory"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "cpu": obj.get("cpu"),
            "memory": obj.get("memory"),
            "max_nb_restart": obj.get("max_nb_restart"),
            "max_duration_seconds": obj.get("max_duration_seconds"),
            "auto_preview": obj.get("auto_preview"),
            "port": obj.get("port"),
            "source": BaseJobResponseAllOfSource.from_dict(obj.get("source")) if obj.get("source") is not None else None,
            "healthchecks": Healthcheck.from_dict(obj.get("healthchecks")) if obj.get("healthchecks") is not None else None,
            "auto_deploy": obj.get("auto_deploy"),
            "job_type": obj.get("job_type"),
            "schedule": CronJobResponseAllOfSchedule.from_dict(obj.get("schedule")) if obj.get("schedule") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


