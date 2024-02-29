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
from pydantic import BaseModel, Field
from qovery.models.probe_type_exec import ProbeTypeExec
from qovery.models.probe_type_grpc import ProbeTypeGrpc
from qovery.models.probe_type_http import ProbeTypeHttp
from qovery.models.probe_type_tcp import ProbeTypeTcp

class ProbeType(BaseModel):
    """
    ProbeType
    """
    tcp: Optional[ProbeTypeTcp] = None
    http: Optional[ProbeTypeHttp] = None
    var_exec: Optional[ProbeTypeExec] = Field(None, alias="exec")
    grpc: Optional[ProbeTypeGrpc] = None
    additional_properties: Dict[str, Any] = {}
    __properties = ["tcp", "http", "exec", "grpc"]

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
    def from_json(cls, json_str: str) -> ProbeType:
        """Create an instance of ProbeType from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of tcp
        if self.tcp:
            _dict['tcp'] = self.tcp.to_dict()
        # override the default output from pydantic by calling `to_dict()` of http
        if self.http:
            _dict['http'] = self.http.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_exec
        if self.var_exec:
            _dict['exec'] = self.var_exec.to_dict()
        # override the default output from pydantic by calling `to_dict()` of grpc
        if self.grpc:
            _dict['grpc'] = self.grpc.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if tcp (nullable) is None
        # and __fields_set__ contains the field
        if self.tcp is None and "tcp" in self.__fields_set__:
            _dict['tcp'] = None

        # set to None if http (nullable) is None
        # and __fields_set__ contains the field
        if self.http is None and "http" in self.__fields_set__:
            _dict['http'] = None

        # set to None if var_exec (nullable) is None
        # and __fields_set__ contains the field
        if self.var_exec is None and "var_exec" in self.__fields_set__:
            _dict['exec'] = None

        # set to None if grpc (nullable) is None
        # and __fields_set__ contains the field
        if self.grpc is None and "grpc" in self.__fields_set__:
            _dict['grpc'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProbeType:
        """Create an instance of ProbeType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ProbeType.parse_obj(obj)

        _obj = ProbeType.parse_obj({
            "tcp": ProbeTypeTcp.from_dict(obj.get("tcp")) if obj.get("tcp") is not None else None,
            "http": ProbeTypeHttp.from_dict(obj.get("http")) if obj.get("http") is not None else None,
            "var_exec": ProbeTypeExec.from_dict(obj.get("exec")) if obj.get("exec") is not None else None,
            "grpc": ProbeTypeGrpc.from_dict(obj.get("grpc")) if obj.get("grpc") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


