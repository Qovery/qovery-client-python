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
from pydantic import Field
from qovery.models.probe_type_exec import ProbeTypeExec
from qovery.models.probe_type_grpc import ProbeTypeGrpc
from qovery.models.probe_type_http import ProbeTypeHttp
from qovery.models.probe_type_tcp import ProbeTypeTcp
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ProbeType(BaseModel):
    """
    ProbeType
    """ # noqa: E501
    tcp: Optional[ProbeTypeTcp] = None
    http: Optional[ProbeTypeHttp] = None
    var_exec: Optional[ProbeTypeExec] = Field(default=None, alias="exec")
    grpc: Optional[ProbeTypeGrpc] = None
    __properties: ClassVar[List[str]] = ["tcp", "http", "exec", "grpc"]

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
        """Create an instance of ProbeType from a JSON string"""
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
        # set to None if tcp (nullable) is None
        # and model_fields_set contains the field
        if self.tcp is None and "tcp" in self.model_fields_set:
            _dict['tcp'] = None

        # set to None if http (nullable) is None
        # and model_fields_set contains the field
        if self.http is None and "http" in self.model_fields_set:
            _dict['http'] = None

        # set to None if var_exec (nullable) is None
        # and model_fields_set contains the field
        if self.var_exec is None and "var_exec" in self.model_fields_set:
            _dict['exec'] = None

        # set to None if grpc (nullable) is None
        # and model_fields_set contains the field
        if self.grpc is None and "grpc" in self.model_fields_set:
            _dict['grpc'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ProbeType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tcp": ProbeTypeTcp.from_dict(obj.get("tcp")) if obj.get("tcp") is not None else None,
            "http": ProbeTypeHttp.from_dict(obj.get("http")) if obj.get("http") is not None else None,
            "exec": ProbeTypeExec.from_dict(obj.get("exec")) if obj.get("exec") is not None else None,
            "grpc": ProbeTypeGrpc.from_dict(obj.get("grpc")) if obj.get("grpc") is not None else None
        })
        return _obj


