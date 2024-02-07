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
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Link(BaseModel):
    """
    Link
    """ # noqa: E501
    url: Optional[StrictStr] = None
    internal_port: Optional[StrictInt] = Field(default=None, description="The port from which the service is reachable from within the cluster")
    external_port: Optional[StrictInt] = Field(default=None, description="The port from which the service is reachable from externally (i.e: 443 for HTTPS)")
    is_qovery_domain: Optional[StrictBool] = Field(default=None, description="True if the domain is managed by Qovery, false if it belongs to the user")
    is_default: Optional[StrictBool] = Field(default=None, description="Indicate if the link is using the root of the domain and not one derivated from port i.e: p8080.zxxxx.jvm.worl      => is_default = false, is_qovery = true zxxxx.jvm.world           => is_default = true, is_qovery = true p8080-my-super-domain.com => is_default = false, is_qovery = false my-super-domain.com       => is_default = true, is_qovery = false ")
    __properties: ClassVar[List[str]] = ["url", "internal_port", "external_port", "is_qovery_domain", "is_default"]

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
        """Create an instance of Link from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Link from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "url": obj.get("url"),
            "internal_port": obj.get("internal_port"),
            "external_port": obj.get("external_port"),
            "is_qovery_domain": obj.get("is_qovery_domain"),
            "is_default": obj.get("is_default")
        })
        return _obj


