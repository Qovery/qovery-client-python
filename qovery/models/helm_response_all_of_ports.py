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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from qovery.models.helm_port_protocol_enum import HelmPortProtocolEnum

class HelmResponseAllOfPorts(BaseModel):
    """
    HelmResponseAllOfPorts
    """
    id: StrictStr = Field(...)
    name: Optional[StrictStr] = None
    internal_port: StrictInt = Field(..., description="The listening port of your service.")
    external_port: Optional[StrictInt] = Field(None, description="The exposed port for your service. This is optional. If not set a default port will be used.")
    service_name: StrictStr = Field(...)
    namespace: Optional[StrictStr] = None
    protocol: HelmPortProtocolEnum = Field(...)
    is_default: Optional[StrictBool] = Field(None, description="is the default port to use for domain")
    __properties = ["id", "name", "internal_port", "external_port", "service_name", "namespace", "protocol", "is_default"]

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
    def from_json(cls, json_str: str) -> HelmResponseAllOfPorts:
        """Create an instance of HelmResponseAllOfPorts from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> HelmResponseAllOfPorts:
        """Create an instance of HelmResponseAllOfPorts from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return HelmResponseAllOfPorts.parse_obj(obj)

        _obj = HelmResponseAllOfPorts.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "internal_port": obj.get("internal_port"),
            "external_port": obj.get("external_port"),
            "service_name": obj.get("service_name"),
            "namespace": obj.get("namespace"),
            "protocol": obj.get("protocol"),
            "is_default": obj.get("is_default")
        })
        return _obj


