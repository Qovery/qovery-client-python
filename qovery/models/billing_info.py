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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class BillingInfo(BaseModel):
    """
    BillingInfo
    """
    first_name: Optional[StrictStr] = None
    last_name: Optional[StrictStr] = None
    email: Optional[StrictStr] = Field(None, description="email used for billing, and to receive all invoices by email")
    address: Optional[StrictStr] = None
    city: Optional[StrictStr] = None
    zip: Optional[StrictStr] = None
    state: Optional[StrictStr] = Field(None, description="only for US")
    country_code: Optional[StrictStr] = Field(None, description="ISO code of the country")
    company: Optional[StrictStr] = Field(None, description="name of the company to bill")
    vat_number: Optional[StrictStr] = None
    __properties = ["first_name", "last_name", "email", "address", "city", "zip", "state", "country_code", "company", "vat_number"]

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
    def from_json(cls, json_str: str) -> BillingInfo:
        """Create an instance of BillingInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if first_name (nullable) is None
        # and __fields_set__ contains the field
        if self.first_name is None and "first_name" in self.__fields_set__:
            _dict['first_name'] = None

        # set to None if last_name (nullable) is None
        # and __fields_set__ contains the field
        if self.last_name is None and "last_name" in self.__fields_set__:
            _dict['last_name'] = None

        # set to None if email (nullable) is None
        # and __fields_set__ contains the field
        if self.email is None and "email" in self.__fields_set__:
            _dict['email'] = None

        # set to None if address (nullable) is None
        # and __fields_set__ contains the field
        if self.address is None and "address" in self.__fields_set__:
            _dict['address'] = None

        # set to None if city (nullable) is None
        # and __fields_set__ contains the field
        if self.city is None and "city" in self.__fields_set__:
            _dict['city'] = None

        # set to None if zip (nullable) is None
        # and __fields_set__ contains the field
        if self.zip is None and "zip" in self.__fields_set__:
            _dict['zip'] = None

        # set to None if state (nullable) is None
        # and __fields_set__ contains the field
        if self.state is None and "state" in self.__fields_set__:
            _dict['state'] = None

        # set to None if country_code (nullable) is None
        # and __fields_set__ contains the field
        if self.country_code is None and "country_code" in self.__fields_set__:
            _dict['country_code'] = None

        # set to None if company (nullable) is None
        # and __fields_set__ contains the field
        if self.company is None and "company" in self.__fields_set__:
            _dict['company'] = None

        # set to None if vat_number (nullable) is None
        # and __fields_set__ contains the field
        if self.vat_number is None and "vat_number" in self.__fields_set__:
            _dict['vat_number'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BillingInfo:
        """Create an instance of BillingInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BillingInfo.parse_obj(obj)

        _obj = BillingInfo.parse_obj({
            "first_name": obj.get("first_name"),
            "last_name": obj.get("last_name"),
            "email": obj.get("email"),
            "address": obj.get("address"),
            "city": obj.get("city"),
            "zip": obj.get("zip"),
            "state": obj.get("state"),
            "country_code": obj.get("country_code"),
            "company": obj.get("company"),
            "vat_number": obj.get("vat_number")
        })
        return _obj


