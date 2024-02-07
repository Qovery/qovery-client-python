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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
from qovery.models.job_request_all_of_schedule_cronjob import JobRequestAllOfScheduleCronjob
from qovery.models.job_request_all_of_schedule_on_start import JobRequestAllOfScheduleOnStart
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class JobRequestAllOfSchedule(BaseModel):
    """
    If you want to define a Cron job, only the `cronjob` property must be filled   A Lifecycle job should contain at least one property `on_XXX` among the 3 properties: `on_start`, `on_stop`, `on_delete` 
    """ # noqa: E501
    on_start: Optional[JobRequestAllOfScheduleOnStart] = None
    on_stop: Optional[JobRequestAllOfScheduleOnStart] = None
    on_delete: Optional[JobRequestAllOfScheduleOnStart] = None
    cronjob: Optional[JobRequestAllOfScheduleCronjob] = None
    __properties: ClassVar[List[str]] = ["on_start", "on_stop", "on_delete", "cronjob"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of JobRequestAllOfSchedule from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of on_start
        if self.on_start:
            _dict['on_start'] = self.on_start.to_dict()
        # override the default output from pydantic by calling `to_dict()` of on_stop
        if self.on_stop:
            _dict['on_stop'] = self.on_stop.to_dict()
        # override the default output from pydantic by calling `to_dict()` of on_delete
        if self.on_delete:
            _dict['on_delete'] = self.on_delete.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cronjob
        if self.cronjob:
            _dict['cronjob'] = self.cronjob.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of JobRequestAllOfSchedule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "on_start": JobRequestAllOfScheduleOnStart.from_dict(obj.get("on_start")) if obj.get("on_start") is not None else None,
            "on_stop": JobRequestAllOfScheduleOnStart.from_dict(obj.get("on_stop")) if obj.get("on_stop") is not None else None,
            "on_delete": JobRequestAllOfScheduleOnStart.from_dict(obj.get("on_delete")) if obj.get("on_delete") is not None else None,
            "cronjob": JobRequestAllOfScheduleCronjob.from_dict(obj.get("cronjob")) if obj.get("cronjob") is not None else None
        })
        return _obj


