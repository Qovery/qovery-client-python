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
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from qovery.models.base_job_response_all_of_source_one_of import BaseJobResponseAllOfSourceOneOf
from qovery.models.base_job_response_all_of_source_one_of1 import BaseJobResponseAllOfSourceOneOf1
from typing import Union, Any, List, TYPE_CHECKING
from pydantic import StrictStr, Field

BASEJOBRESPONSEALLOFSOURCE_ONE_OF_SCHEMAS = ["BaseJobResponseAllOfSourceOneOf", "BaseJobResponseAllOfSourceOneOf1"]

class BaseJobResponseAllOfSource(BaseModel):
    """
    BaseJobResponseAllOfSource
    """
    # data type: BaseJobResponseAllOfSourceOneOf
    oneof_schema_1_validator: Optional[BaseJobResponseAllOfSourceOneOf] = None
    # data type: BaseJobResponseAllOfSourceOneOf1
    oneof_schema_2_validator: Optional[BaseJobResponseAllOfSourceOneOf1] = None
    if TYPE_CHECKING:
        actual_instance: Union[BaseJobResponseAllOfSourceOneOf, BaseJobResponseAllOfSourceOneOf1]
    else:
        actual_instance: Any
    one_of_schemas: List[str] = Field(BASEJOBRESPONSEALLOFSOURCE_ONE_OF_SCHEMAS, const=True)

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
        instance = BaseJobResponseAllOfSource.construct()
        error_messages = []
        match = 0
        # validate data type: BaseJobResponseAllOfSourceOneOf
        if not isinstance(v, BaseJobResponseAllOfSourceOneOf):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BaseJobResponseAllOfSourceOneOf`")
        else:
            match += 1
        # validate data type: BaseJobResponseAllOfSourceOneOf1
        if not isinstance(v, BaseJobResponseAllOfSourceOneOf1):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BaseJobResponseAllOfSourceOneOf1`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in BaseJobResponseAllOfSource with oneOf schemas: BaseJobResponseAllOfSourceOneOf, BaseJobResponseAllOfSourceOneOf1. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in BaseJobResponseAllOfSource with oneOf schemas: BaseJobResponseAllOfSourceOneOf, BaseJobResponseAllOfSourceOneOf1. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> BaseJobResponseAllOfSource:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> BaseJobResponseAllOfSource:
        """Returns the object represented by the json string"""
        instance = BaseJobResponseAllOfSource.construct()
        error_messages = []
        match = 0

        # deserialize data into BaseJobResponseAllOfSourceOneOf
        try:
            instance.actual_instance = BaseJobResponseAllOfSourceOneOf.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into BaseJobResponseAllOfSourceOneOf1
        try:
            instance.actual_instance = BaseJobResponseAllOfSourceOneOf1.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into BaseJobResponseAllOfSource with oneOf schemas: BaseJobResponseAllOfSourceOneOf, BaseJobResponseAllOfSourceOneOf1. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into BaseJobResponseAllOfSource with oneOf schemas: BaseJobResponseAllOfSourceOneOf, BaseJobResponseAllOfSourceOneOf1. Details: " + ", ".join(error_messages))
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

