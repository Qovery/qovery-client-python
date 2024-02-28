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
from pydantic import BaseModel, Field, StrictBool, StrictStr
from qovery.models.api_variable_scope_enum import APIVariableScopeEnum
from qovery.models.api_variable_type_enum import APIVariableTypeEnum
from qovery.models.linked_service_type_enum import LinkedServiceTypeEnum
from qovery.models.variable_alias import VariableAlias
from qovery.models.variable_override import VariableOverride

class VariableResponse(BaseModel):
    """
    VariableResponse
    """
    id: StrictStr = Field(...)
    created_at: datetime = Field(...)
    updated_at: Optional[datetime] = None
    key: StrictStr = Field(...)
    value: Optional[StrictStr] = Field(...)
    mount_path: Optional[StrictStr] = None
    overridden_variable: Optional[VariableOverride] = None
    aliased_variable: Optional[VariableAlias] = None
    scope: APIVariableScopeEnum = Field(...)
    variable_type: Optional[APIVariableTypeEnum] = None
    service_id: Optional[StrictStr] = Field(None, description="The id of the service referenced by this variable.")
    service_name: Optional[StrictStr] = Field(None, description="The name of the service referenced by this variable.")
    service_type: Optional[LinkedServiceTypeEnum] = None
    owned_by: Optional[StrictStr] = Field(None, description="Entity that created/own the variable (i.e: Qovery, Doppler)")
    is_secret: StrictBool = Field(...)
    __properties = ["id", "created_at", "updated_at", "key", "value", "mount_path", "overridden_variable", "aliased_variable", "scope", "variable_type", "service_id", "service_name", "service_type", "owned_by", "is_secret"]

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
    def from_json(cls, json_str: str) -> VariableResponse:
        """Create an instance of VariableResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "id",
                            "created_at",
                            "updated_at",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of overridden_variable
        if self.overridden_variable:
            _dict['overridden_variable'] = self.overridden_variable.to_dict()
        # override the default output from pydantic by calling `to_dict()` of aliased_variable
        if self.aliased_variable:
            _dict['aliased_variable'] = self.aliased_variable.to_dict()
        # set to None if value (nullable) is None
        # and __fields_set__ contains the field
        if self.value is None and "value" in self.__fields_set__:
            _dict['value'] = None

        # set to None if mount_path (nullable) is None
        # and __fields_set__ contains the field
        if self.mount_path is None and "mount_path" in self.__fields_set__:
            _dict['mount_path'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VariableResponse:
        """Create an instance of VariableResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VariableResponse.parse_obj(obj)

        _obj = VariableResponse.parse_obj({
            "id": obj.get("id"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "key": obj.get("key"),
            "value": obj.get("value"),
            "mount_path": obj.get("mount_path"),
            "overridden_variable": VariableOverride.from_dict(obj.get("overridden_variable")) if obj.get("overridden_variable") is not None else None,
            "aliased_variable": VariableAlias.from_dict(obj.get("aliased_variable")) if obj.get("aliased_variable") is not None else None,
            "scope": obj.get("scope"),
            "variable_type": obj.get("variable_type"),
            "service_id": obj.get("service_id"),
            "service_name": obj.get("service_name"),
            "service_type": obj.get("service_type"),
            "owned_by": obj.get("owned_by"),
            "is_secret": obj.get("is_secret")
        })
        return _obj


