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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from qovery.models.port_protocol_enum import PortProtocolEnum

class ServicePortRequestPortsInner(BaseModel):
    """
    ServicePortRequestPortsInner
    """
    id: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    internal_port: StrictInt = Field(..., description="The listening port of your service.")
    external_port: Optional[StrictInt] = Field(None, description="The exposed port for your service. This is optional. If not set a default port will be used.")
    publicly_accessible: StrictBool = Field(..., description="Expose the port to the world")
    is_default: Optional[StrictBool] = Field(None, description="is the default port to use for domain")
    protocol: Optional[PortProtocolEnum] = None
    additional_properties: Dict[str, Any] = {}
    __properties = ["id", "name", "internal_port", "external_port", "publicly_accessible", "is_default", "protocol"]

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
    def from_json(cls, json_str: str) -> ServicePortRequestPortsInner:
        """Create an instance of ServicePortRequestPortsInner from a JSON string"""
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

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ServicePortRequestPortsInner:
        """Create an instance of ServicePortRequestPortsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ServicePortRequestPortsInner.parse_obj(obj)

        _obj = ServicePortRequestPortsInner.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "internal_port": obj.get("internal_port"),
            "external_port": obj.get("external_port"),
            "publicly_accessible": obj.get("publicly_accessible"),
            "is_default": obj.get("is_default"),
            "protocol": obj.get("protocol")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


