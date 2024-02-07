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
from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from pydantic import Field
from qovery.models.service_type_enum import ServiceTypeEnum
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Service(BaseModel):
    """
    Service
    """ # noqa: E501
    id: StrictStr = Field(description="uuid of the associated service (application, database, job, gateway...)")
    created_at: datetime
    updated_at: Optional[datetime] = None
    type: Optional[ServiceTypeEnum] = None
    name: Optional[StrictStr] = Field(default=None, description="name of the service")
    deployed_commit_id: Optional[StrictStr] = Field(default=None, description="Git commit ID corresponding to the deployed version of the application")
    last_updated_by: Optional[StrictStr] = Field(default=None, description="uuid of the user that made the last update")
    consumed_resources_in_percent: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="global overview of resources consumption of the service")
    service_typology: Optional[StrictStr] = Field(default=None, description="describes the typology of service (container, postgresl, redis...)")
    service_version: Optional[StrictStr] = Field(default=None, description="for databases this field exposes the database version")
    to_update: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["id", "created_at", "updated_at", "type", "name", "deployed_commit_id", "last_updated_by", "consumed_resources_in_percent", "service_typology", "service_version", "to_update"]

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
        """Create an instance of Service from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "created_at",
                "updated_at",
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Service from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "type": obj.get("type"),
            "name": obj.get("name"),
            "deployed_commit_id": obj.get("deployed_commit_id"),
            "last_updated_by": obj.get("last_updated_by"),
            "consumed_resources_in_percent": obj.get("consumed_resources_in_percent"),
            "service_typology": obj.get("service_typology"),
            "service_version": obj.get("service_version"),
            "to_update": obj.get("to_update")
        })
        return _obj


