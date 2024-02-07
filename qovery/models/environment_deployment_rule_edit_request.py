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
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictStr
from qovery.models.weekday_enum import WeekdayEnum
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class EnvironmentDeploymentRuleEditRequest(BaseModel):
    """
    EnvironmentDeploymentRuleEditRequest
    """ # noqa: E501
    on_demand_preview: Optional[StrictBool] = False
    auto_preview: Optional[StrictBool] = False
    auto_stop: Optional[StrictBool] = False
    timezone: StrictStr
    start_time: datetime
    stop_time: datetime
    weekdays: List[WeekdayEnum]
    __properties: ClassVar[List[str]] = ["on_demand_preview", "auto_preview", "auto_stop", "timezone", "start_time", "stop_time", "weekdays"]

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
        """Create an instance of EnvironmentDeploymentRuleEditRequest from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of EnvironmentDeploymentRuleEditRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "on_demand_preview": obj.get("on_demand_preview") if obj.get("on_demand_preview") is not None else False,
            "auto_preview": obj.get("auto_preview") if obj.get("auto_preview") is not None else False,
            "auto_stop": obj.get("auto_stop") if obj.get("auto_stop") is not None else False,
            "timezone": obj.get("timezone"),
            "start_time": obj.get("start_time"),
            "stop_time": obj.get("stop_time"),
            "weekdays": obj.get("weekdays")
        })
        return _obj


