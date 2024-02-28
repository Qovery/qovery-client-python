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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist

class ClusterFeatureAwsExistingVpc(BaseModel):
    """
    ClusterFeatureAwsExistingVpc
    """
    aws_vpc_eks_id: StrictStr = Field(...)
    eks_subnets_zone_a_ids: conlist(StrictStr) = Field(...)
    eks_subnets_zone_b_ids: conlist(StrictStr) = Field(...)
    eks_subnets_zone_c_ids: conlist(StrictStr) = Field(...)
    documentdb_subnets_zone_a_ids: Optional[conlist(StrictStr)] = None
    documentdb_subnets_zone_b_ids: Optional[conlist(StrictStr)] = None
    documentdb_subnets_zone_c_ids: Optional[conlist(StrictStr)] = None
    elasticache_subnets_zone_a_ids: Optional[conlist(StrictStr)] = None
    elasticache_subnets_zone_b_ids: Optional[conlist(StrictStr)] = None
    elasticache_subnets_zone_c_ids: Optional[conlist(StrictStr)] = None
    rds_subnets_zone_a_ids: Optional[conlist(StrictStr)] = None
    rds_subnets_zone_b_ids: Optional[conlist(StrictStr)] = None
    rds_subnets_zone_c_ids: Optional[conlist(StrictStr)] = None
    __properties = ["aws_vpc_eks_id", "eks_subnets_zone_a_ids", "eks_subnets_zone_b_ids", "eks_subnets_zone_c_ids", "documentdb_subnets_zone_a_ids", "documentdb_subnets_zone_b_ids", "documentdb_subnets_zone_c_ids", "elasticache_subnets_zone_a_ids", "elasticache_subnets_zone_b_ids", "elasticache_subnets_zone_c_ids", "rds_subnets_zone_a_ids", "rds_subnets_zone_b_ids", "rds_subnets_zone_c_ids"]

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
    def from_json(cls, json_str: str) -> ClusterFeatureAwsExistingVpc:
        """Create an instance of ClusterFeatureAwsExistingVpc from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if documentdb_subnets_zone_a_ids (nullable) is None
        # and __fields_set__ contains the field
        if self.documentdb_subnets_zone_a_ids is None and "documentdb_subnets_zone_a_ids" in self.__fields_set__:
            _dict['documentdb_subnets_zone_a_ids'] = None

        # set to None if documentdb_subnets_zone_b_ids (nullable) is None
        # and __fields_set__ contains the field
        if self.documentdb_subnets_zone_b_ids is None and "documentdb_subnets_zone_b_ids" in self.__fields_set__:
            _dict['documentdb_subnets_zone_b_ids'] = None

        # set to None if documentdb_subnets_zone_c_ids (nullable) is None
        # and __fields_set__ contains the field
        if self.documentdb_subnets_zone_c_ids is None and "documentdb_subnets_zone_c_ids" in self.__fields_set__:
            _dict['documentdb_subnets_zone_c_ids'] = None

        # set to None if elasticache_subnets_zone_a_ids (nullable) is None
        # and __fields_set__ contains the field
        if self.elasticache_subnets_zone_a_ids is None and "elasticache_subnets_zone_a_ids" in self.__fields_set__:
            _dict['elasticache_subnets_zone_a_ids'] = None

        # set to None if elasticache_subnets_zone_b_ids (nullable) is None
        # and __fields_set__ contains the field
        if self.elasticache_subnets_zone_b_ids is None and "elasticache_subnets_zone_b_ids" in self.__fields_set__:
            _dict['elasticache_subnets_zone_b_ids'] = None

        # set to None if elasticache_subnets_zone_c_ids (nullable) is None
        # and __fields_set__ contains the field
        if self.elasticache_subnets_zone_c_ids is None and "elasticache_subnets_zone_c_ids" in self.__fields_set__:
            _dict['elasticache_subnets_zone_c_ids'] = None

        # set to None if rds_subnets_zone_a_ids (nullable) is None
        # and __fields_set__ contains the field
        if self.rds_subnets_zone_a_ids is None and "rds_subnets_zone_a_ids" in self.__fields_set__:
            _dict['rds_subnets_zone_a_ids'] = None

        # set to None if rds_subnets_zone_b_ids (nullable) is None
        # and __fields_set__ contains the field
        if self.rds_subnets_zone_b_ids is None and "rds_subnets_zone_b_ids" in self.__fields_set__:
            _dict['rds_subnets_zone_b_ids'] = None

        # set to None if rds_subnets_zone_c_ids (nullable) is None
        # and __fields_set__ contains the field
        if self.rds_subnets_zone_c_ids is None and "rds_subnets_zone_c_ids" in self.__fields_set__:
            _dict['rds_subnets_zone_c_ids'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ClusterFeatureAwsExistingVpc:
        """Create an instance of ClusterFeatureAwsExistingVpc from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ClusterFeatureAwsExistingVpc.parse_obj(obj)

        _obj = ClusterFeatureAwsExistingVpc.parse_obj({
            "aws_vpc_eks_id": obj.get("aws_vpc_eks_id"),
            "eks_subnets_zone_a_ids": obj.get("eks_subnets_zone_a_ids"),
            "eks_subnets_zone_b_ids": obj.get("eks_subnets_zone_b_ids"),
            "eks_subnets_zone_c_ids": obj.get("eks_subnets_zone_c_ids"),
            "documentdb_subnets_zone_a_ids": obj.get("documentdb_subnets_zone_a_ids"),
            "documentdb_subnets_zone_b_ids": obj.get("documentdb_subnets_zone_b_ids"),
            "documentdb_subnets_zone_c_ids": obj.get("documentdb_subnets_zone_c_ids"),
            "elasticache_subnets_zone_a_ids": obj.get("elasticache_subnets_zone_a_ids"),
            "elasticache_subnets_zone_b_ids": obj.get("elasticache_subnets_zone_b_ids"),
            "elasticache_subnets_zone_c_ids": obj.get("elasticache_subnets_zone_c_ids"),
            "rds_subnets_zone_a_ids": obj.get("rds_subnets_zone_a_ids"),
            "rds_subnets_zone_b_ids": obj.get("rds_subnets_zone_b_ids"),
            "rds_subnets_zone_c_ids": obj.get("rds_subnets_zone_c_ids")
        })
        return _obj


