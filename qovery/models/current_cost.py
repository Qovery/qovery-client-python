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
from pydantic import BaseModel, Field, StrictInt
from qovery.models.cost import Cost
from qovery.models.plan_enum import PlanEnum

class CurrentCost(BaseModel):
    """
    CurrentCost
    """
    plan: Optional[PlanEnum] = None
    remaining_trial_day: Optional[StrictInt] = Field(None, description="number of days remaining before the end of the trial period")
    renewal_at: Optional[datetime] = Field(None, description="date when the current plan will be renewed")
    cost: Optional[Cost] = None
    __properties = ["plan", "remaining_trial_day", "renewal_at", "cost"]

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
    def from_json(cls, json_str: str) -> CurrentCost:
        """Create an instance of CurrentCost from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "renewal_at",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of cost
        if self.cost:
            _dict['cost'] = self.cost.to_dict()
        # set to None if renewal_at (nullable) is None
        # and __fields_set__ contains the field
        if self.renewal_at is None and "renewal_at" in self.__fields_set__:
            _dict['renewal_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CurrentCost:
        """Create an instance of CurrentCost from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CurrentCost.parse_obj(obj)

        _obj = CurrentCost.parse_obj({
            "plan": obj.get("plan"),
            "remaining_trial_day": obj.get("remaining_trial_day"),
            "renewal_at": obj.get("renewal_at"),
            "cost": Cost.from_dict(obj.get("cost")) if obj.get("cost") is not None else None
        })
        return _obj


