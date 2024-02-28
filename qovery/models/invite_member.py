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
from pydantic import BaseModel, Field, StrictStr
from qovery.models.invite_member_role_enum import InviteMemberRoleEnum
from qovery.models.invite_status_enum import InviteStatusEnum

class InviteMember(BaseModel):
    """
    InviteMember
    """
    id: StrictStr = Field(...)
    created_at: datetime = Field(...)
    updated_at: Optional[datetime] = None
    email: StrictStr = Field(...)
    role: InviteMemberRoleEnum = Field(...)
    invitation_link: StrictStr = Field(...)
    invitation_status: InviteStatusEnum = Field(...)
    organization_name: Optional[StrictStr] = None
    inviter: StrictStr = Field(...)
    logo_url: Optional[StrictStr] = None
    role_id: Optional[StrictStr] = None
    role_name: Optional[StrictStr] = None
    __properties = ["id", "created_at", "updated_at", "email", "role", "invitation_link", "invitation_status", "organization_name", "inviter", "logo_url", "role_id", "role_name"]

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
    def from_json(cls, json_str: str) -> InviteMember:
        """Create an instance of InviteMember from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InviteMember:
        """Create an instance of InviteMember from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InviteMember.parse_obj(obj)

        _obj = InviteMember.parse_obj({
            "id": obj.get("id"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "email": obj.get("email"),
            "role": obj.get("role"),
            "invitation_link": obj.get("invitation_link"),
            "invitation_status": obj.get("invitation_status"),
            "organization_name": obj.get("organization_name"),
            "inviter": obj.get("inviter"),
            "logo_url": obj.get("logo_url"),
            "role_id": obj.get("role_id"),
            "role_name": obj.get("role_name")
        })
        return _obj


