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
from pydantic import BaseModel, Field, StrictInt, conlist
from qovery.models.service_step_metric import ServiceStepMetric

class ServiceStepMetrics(BaseModel):
    """
    ServiceStepMetrics
    """
    total_duration_sec: Optional[StrictInt] = Field(None, description="The total duration in seconds of the service deployment or null if the deployment is not completed.")
    total_computing_duration_sec: Optional[StrictInt] = Field(None, description="The total duration in seconds of the service deployment without queuing steps.")
    details: Optional[conlist(ServiceStepMetric)] = Field(None, description="A list of metrics for deployment steps of the service.")
    additional_properties: Dict[str, Any] = {}
    __properties = ["total_duration_sec", "total_computing_duration_sec", "details"]

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
    def from_json(cls, json_str: str) -> ServiceStepMetrics:
        """Create an instance of ServiceStepMetrics from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in details (list)
        _items = []
        if self.details:
            for _item in self.details:
                if _item:
                    _items.append(_item.to_dict())
            _dict['details'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if total_duration_sec (nullable) is None
        # and __fields_set__ contains the field
        if self.total_duration_sec is None and "total_duration_sec" in self.__fields_set__:
            _dict['total_duration_sec'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ServiceStepMetrics:
        """Create an instance of ServiceStepMetrics from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ServiceStepMetrics.parse_obj(obj)

        _obj = ServiceStepMetrics.parse_obj({
            "total_duration_sec": obj.get("total_duration_sec"),
            "total_computing_duration_sec": obj.get("total_computing_duration_sec"),
            "details": [ServiceStepMetric.from_dict(_item) for _item in obj.get("details")] if obj.get("details") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


