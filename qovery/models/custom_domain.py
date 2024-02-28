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
from pydantic import BaseModel, Field, StrictBool, StrictStr
from qovery.models.custom_domain_status_enum import CustomDomainStatusEnum

class CustomDomain(BaseModel):
    """
    CustomDomain
    """
    id: StrictStr = Field(...)
    created_at: datetime = Field(...)
    updated_at: Optional[datetime] = None
    domain: StrictStr = Field(..., description="your custom domain")
    generate_certificate: StrictBool = Field(..., description="to control if a certificate has to be generated for this custom domain by Qovery. The default value is `true`. This flag should be set to `false` if a CDN or other entities are managing the certificate for the specified domain and the traffic is proxied by the CDN to Qovery.")
    validation_domain: Optional[StrictStr] = Field(None, description="URL provided by Qovery. You must create a CNAME on your DNS provider using that URL")
    status: Optional[CustomDomainStatusEnum] = None
    additional_properties: Dict[str, Any] = {}
    __properties = ["id", "created_at", "updated_at", "domain", "generate_certificate", "validation_domain", "status"]

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
    def from_json(cls, json_str: str) -> CustomDomain:
        """Create an instance of CustomDomain from a JSON string"""
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
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CustomDomain:
        """Create an instance of CustomDomain from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CustomDomain.parse_obj(obj)

        _obj = CustomDomain.parse_obj({
            "id": obj.get("id"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "domain": obj.get("domain"),
            "generate_certificate": obj.get("generate_certificate"),
            "validation_domain": obj.get("validation_domain"),
            "status": obj.get("status")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


