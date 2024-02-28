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


from typing import List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr, conlist, validator
from qovery.models.cluster_feature_accepted_values_inner import ClusterFeatureAcceptedValuesInner
from qovery.models.cluster_feature_value import ClusterFeatureValue

class ClusterFeature(BaseModel):
    """
    ClusterFeature
    """
    id: Optional[StrictStr] = None
    title: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    cost_per_month_in_cents: Optional[StrictInt] = None
    cost_per_month: Optional[Union[StrictFloat, StrictInt]] = None
    currency_code: Optional[StrictStr] = None
    value_type: Optional[StrictStr] = None
    value: Optional[ClusterFeatureValue] = None
    is_value_updatable: Optional[StrictBool] = False
    accepted_values: Optional[conlist(ClusterFeatureAcceptedValuesInner)] = None
    __properties = ["id", "title", "description", "cost_per_month_in_cents", "cost_per_month", "currency_code", "value_type", "value", "is_value_updatable", "accepted_values"]

    @validator('value_type')
    def value_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('BOOLEAN'):
            raise ValueError("must be one of enum values ('BOOLEAN')")
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
    def from_json(cls, json_str: str) -> ClusterFeature:
        """Create an instance of ClusterFeature from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of value
        if self.value:
            _dict['value'] = self.value.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in accepted_values (list)
        _items = []
        if self.accepted_values:
            for _item in self.accepted_values:
                if _item:
                    _items.append(_item.to_dict())
            _dict['accepted_values'] = _items
        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if cost_per_month_in_cents (nullable) is None
        # and __fields_set__ contains the field
        if self.cost_per_month_in_cents is None and "cost_per_month_in_cents" in self.__fields_set__:
            _dict['cost_per_month_in_cents'] = None

        # set to None if cost_per_month (nullable) is None
        # and __fields_set__ contains the field
        if self.cost_per_month is None and "cost_per_month" in self.__fields_set__:
            _dict['cost_per_month'] = None

        # set to None if currency_code (nullable) is None
        # and __fields_set__ contains the field
        if self.currency_code is None and "currency_code" in self.__fields_set__:
            _dict['currency_code'] = None

        # set to None if value (nullable) is None
        # and __fields_set__ contains the field
        if self.value is None and "value" in self.__fields_set__:
            _dict['value'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ClusterFeature:
        """Create an instance of ClusterFeature from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ClusterFeature.parse_obj(obj)

        _obj = ClusterFeature.parse_obj({
            "id": obj.get("id"),
            "title": obj.get("title"),
            "description": obj.get("description"),
            "cost_per_month_in_cents": obj.get("cost_per_month_in_cents"),
            "cost_per_month": obj.get("cost_per_month"),
            "currency_code": obj.get("currency_code"),
            "value_type": obj.get("value_type"),
            "value": ClusterFeatureValue.from_dict(obj.get("value")) if obj.get("value") is not None else None,
            "is_value_updatable": obj.get("is_value_updatable") if obj.get("is_value_updatable") is not None else False,
            "accepted_values": [ClusterFeatureAcceptedValuesInner.from_dict(_item) for _item in obj.get("accepted_values")] if obj.get("accepted_values") is not None else None
        })
        return _obj


