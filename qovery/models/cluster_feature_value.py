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
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, ValidationError, validator
from qovery.models.cluster_feature_aws_existing_vpc import ClusterFeatureAwsExistingVpc
from qovery.models.cluster_feature_gcp_existing_vpc import ClusterFeatureGcpExistingVpc
from typing import Union, Any, List, TYPE_CHECKING
from pydantic import StrictStr, Field

CLUSTERFEATUREVALUE_ONE_OF_SCHEMAS = ["ClusterFeatureAwsExistingVpc", "ClusterFeatureGcpExistingVpc", "bool", "str"]

class ClusterFeatureValue(BaseModel):
    """
    ClusterFeatureValue
    """
    # data type: str
    oneof_schema_1_validator: Optional[StrictStr] = None
    # data type: bool
    oneof_schema_2_validator: Optional[StrictBool] = None
    # data type: ClusterFeatureAwsExistingVpc
    oneof_schema_3_validator: Optional[ClusterFeatureAwsExistingVpc] = None
    # data type: ClusterFeatureGcpExistingVpc
    oneof_schema_4_validator: Optional[ClusterFeatureGcpExistingVpc] = None
    if TYPE_CHECKING:
        actual_instance: Union[ClusterFeatureAwsExistingVpc, ClusterFeatureGcpExistingVpc, bool, str]
    else:
        actual_instance: Any
    one_of_schemas: List[str] = Field(CLUSTERFEATUREVALUE_ONE_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        if v is None:
            return v

        instance = ClusterFeatureValue.construct()
        error_messages = []
        match = 0
        # validate data type: str
        try:
            instance.oneof_schema_1_validator = v
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # validate data type: bool
        try:
            instance.oneof_schema_2_validator = v
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # validate data type: ClusterFeatureAwsExistingVpc
        if not isinstance(v, ClusterFeatureAwsExistingVpc):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ClusterFeatureAwsExistingVpc`")
        else:
            match += 1
        # validate data type: ClusterFeatureGcpExistingVpc
        if not isinstance(v, ClusterFeatureGcpExistingVpc):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ClusterFeatureGcpExistingVpc`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ClusterFeatureValue with oneOf schemas: ClusterFeatureAwsExistingVpc, ClusterFeatureGcpExistingVpc, bool, str. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ClusterFeatureValue with oneOf schemas: ClusterFeatureAwsExistingVpc, ClusterFeatureGcpExistingVpc, bool, str. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> ClusterFeatureValue:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> ClusterFeatureValue:
        """Returns the object represented by the json string"""
        instance = ClusterFeatureValue.construct()
        if json_str is None:
            return instance

        error_messages = []
        match = 0

        # deserialize data into str
        try:
            # validation
            instance.oneof_schema_1_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.oneof_schema_1_validator
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into bool
        try:
            # validation
            instance.oneof_schema_2_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.oneof_schema_2_validator
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ClusterFeatureAwsExistingVpc
        try:
            instance.actual_instance = ClusterFeatureAwsExistingVpc.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ClusterFeatureGcpExistingVpc
        try:
            instance.actual_instance = ClusterFeatureGcpExistingVpc.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ClusterFeatureValue with oneOf schemas: ClusterFeatureAwsExistingVpc, ClusterFeatureGcpExistingVpc, bool, str. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ClusterFeatureValue with oneOf schemas: ClusterFeatureAwsExistingVpc, ClusterFeatureGcpExistingVpc, bool, str. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        to_dict = getattr(self.actual_instance, "to_dict", None)
        if callable(to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())


