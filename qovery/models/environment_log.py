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
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr
from pydantic import Field
from qovery.models.environment_log_scope import EnvironmentLogScope
from qovery.models.status_kind_enum import StatusKindEnum
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class EnvironmentLog(BaseModel):
    """
    EnvironmentLog
    """ # noqa: E501
    id: StrictStr
    created_at: datetime
    scope: Optional[EnvironmentLogScope] = None
    state: Optional[StatusKindEnum] = None
    message: Optional[StrictStr] = Field(description="Log message")
    execution_id: Optional[StrictStr] = Field(default=None, description="Only for errors. Helps Qovery team to investigate.")
    hint: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["id", "created_at", "scope", "state", "message", "execution_id", "hint"]

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
        """Create an instance of EnvironmentLog from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of scope
        if self.scope:
            _dict['scope'] = self.scope.to_dict()
        # set to None if message (nullable) is None
        # and model_fields_set contains the field
        if self.message is None and "message" in self.model_fields_set:
            _dict['message'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of EnvironmentLog from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "created_at": obj.get("created_at"),
            "scope": EnvironmentLogScope.from_dict(obj.get("scope")) if obj.get("scope") is not None else None,
            "state": obj.get("state"),
            "message": obj.get("message"),
            "execution_id": obj.get("execution_id"),
            "hint": obj.get("hint")
        })
        return _obj


