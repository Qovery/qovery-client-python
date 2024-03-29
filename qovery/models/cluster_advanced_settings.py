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


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist, validator
from qovery.models.registry_mirroring_mode_enum import RegistryMirroringModeEnum

class ClusterAdvancedSettings(BaseModel):
    """
    ClusterAdvancedSettings
    """
    aws_cloudwatch_eks_logs_retention_days: Optional[StrictInt] = Field(None, alias="aws.cloudwatch.eks_logs_retention_days", description="Set the number of retention days for EKS Cloudwatch logs")
    aws_vpc_enable_s3_flow_logs: Optional[StrictBool] = Field(None, alias="aws.vpc.enable_s3_flow_logs", description="Enable flow logs for on the VPC and store them in an S3 bucket")
    aws_vpc_flow_logs_retention_days: Optional[StrictInt] = Field(None, alias="aws.vpc.flow_logs_retention_days", description="Set the number of retention days for flow logs. Disable with value \"0\"")
    loki_log_retention_in_week: Optional[StrictInt] = Field(None, alias="loki.log_retention_in_week", description="For how long in week loki is going to keep logs of your applications")
    registry_image_retention_time: Optional[StrictInt] = Field(None, alias="registry.image_retention_time", description="Configure the number of seconds before cleaning images in the registry")
    cloud_provider_container_registry_tags: Optional[Dict[str, StrictStr]] = Field(None, alias="cloud_provider.container_registry.tags", description="Add additional tags on the cluster dedicated registry")
    load_balancer_size: Optional[StrictStr] = Field(None, alias="load_balancer.size", description="Select the size of the main load_balancer (only effective for Scaleway)")
    database_postgresql_deny_public_access: Optional[StrictBool] = Field(None, alias="database.postgresql.deny_public_access", description="Deny public access to any PostgreSQL database")
    database_postgresql_allowed_cidrs: Optional[conlist(StrictStr)] = Field(None, alias="database.postgresql.allowed_cidrs", description="List of CIDRs allowed to access the PostgreSQL database")
    database_mysql_deny_public_access: Optional[StrictBool] = Field(None, alias="database.mysql.deny_public_access", description="Deny public access to any MySql database")
    database_mysql_allowed_cidrs: Optional[conlist(StrictStr)] = Field(None, alias="database.mysql.allowed_cidrs", description="List of CIDRs allowed to access the MySql database")
    database_mongodb_deny_public_access: Optional[StrictBool] = Field(None, alias="database.mongodb.deny_public_access", description="Deny public access to any MongoDB/DocumentDB database")
    database_mongodb_allowed_cidrs: Optional[conlist(StrictStr)] = Field(None, alias="database.mongodb.allowed_cidrs", description="List of CIDRs allowed to access the MongoDB/DocumentDB database")
    database_redis_deny_public_access: Optional[StrictBool] = Field(None, alias="database.redis.deny_public_access", description="Deny public access to any Redis database")
    database_redis_allowed_cidrs: Optional[conlist(StrictStr)] = Field(None, alias="database.redis.allowed_cidrs", description="List of CIDRs allowed to access the Redis database")
    aws_iam_admin_group: Optional[StrictStr] = Field(None, alias="aws.iam.admin_group", description="AWS IAM group name with cluster access")
    aws_eks_ec2_metadata_imds: Optional[StrictStr] = Field(None, alias="aws.eks.ec2.metadata_imds", description="Specify the [IMDS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html) version you want to use:   * `required`: IMDS V2 only   * `optional`: IMDS V1 + V2 ")
    pleco_resources_ttl: Optional[StrictInt] = Field(None, alias="pleco.resources_ttl")
    registry_mirroring_mode: Optional[RegistryMirroringModeEnum] = Field(None, alias="registry.mirroring_mode")
    nginx_vcpu_request_in_milli_cpu: Optional[StrictInt] = Field(None, alias="nginx.vcpu.request_in_milli_cpu", description="vcpu request in millicores")
    nginx_vcpu_limit_in_milli_cpu: Optional[StrictInt] = Field(None, alias="nginx.vcpu.limit_in_milli_cpu", description="vcpu limit in millicores")
    nginx_memory_request_in_mib: Optional[StrictInt] = Field(None, alias="nginx.memory.request_in_mib", description="memory request in MiB")
    nginx_memory_limit_in_mib: Optional[StrictInt] = Field(None, alias="nginx.memory.limit_in_mib", description="memory limit in MiB")
    nginx_hpa_cpu_utilization_percentage_threshold: Optional[StrictInt] = Field(None, alias="nginx.hpa.cpu_utilization_percentage_threshold", description="hpa cpu threshold in percentage")
    nginx_hpa_min_number_instances: Optional[StrictInt] = Field(None, alias="nginx.hpa.min_number_instances", description="hpa minimum number of instances")
    nginx_hpa_max_number_instances: Optional[StrictInt] = Field(None, alias="nginx.hpa.max_number_instances", description="hpa maximum number of instances")
    additional_properties: Dict[str, Any] = {}
    __properties = ["aws.cloudwatch.eks_logs_retention_days", "aws.vpc.enable_s3_flow_logs", "aws.vpc.flow_logs_retention_days", "loki.log_retention_in_week", "registry.image_retention_time", "cloud_provider.container_registry.tags", "load_balancer.size", "database.postgresql.deny_public_access", "database.postgresql.allowed_cidrs", "database.mysql.deny_public_access", "database.mysql.allowed_cidrs", "database.mongodb.deny_public_access", "database.mongodb.allowed_cidrs", "database.redis.deny_public_access", "database.redis.allowed_cidrs", "aws.iam.admin_group", "aws.eks.ec2.metadata_imds", "pleco.resources_ttl", "registry.mirroring_mode", "nginx.vcpu.request_in_milli_cpu", "nginx.vcpu.limit_in_milli_cpu", "nginx.memory.request_in_mib", "nginx.memory.limit_in_mib", "nginx.hpa.cpu_utilization_percentage_threshold", "nginx.hpa.min_number_instances", "nginx.hpa.max_number_instances"]

    @validator('aws_eks_ec2_metadata_imds')
    def aws_eks_ec2_metadata_imds_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('optional', 'required'):
            raise ValueError("must be one of enum values ('optional', 'required')")
        return value

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
    def from_json(cls, json_str: str) -> ClusterAdvancedSettings:
        """Create an instance of ClusterAdvancedSettings from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ClusterAdvancedSettings:
        """Create an instance of ClusterAdvancedSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ClusterAdvancedSettings.parse_obj(obj)

        _obj = ClusterAdvancedSettings.parse_obj({
            "aws_cloudwatch_eks_logs_retention_days": obj.get("aws.cloudwatch.eks_logs_retention_days"),
            "aws_vpc_enable_s3_flow_logs": obj.get("aws.vpc.enable_s3_flow_logs"),
            "aws_vpc_flow_logs_retention_days": obj.get("aws.vpc.flow_logs_retention_days"),
            "loki_log_retention_in_week": obj.get("loki.log_retention_in_week"),
            "registry_image_retention_time": obj.get("registry.image_retention_time"),
            "cloud_provider_container_registry_tags": obj.get("cloud_provider.container_registry.tags"),
            "load_balancer_size": obj.get("load_balancer.size"),
            "database_postgresql_deny_public_access": obj.get("database.postgresql.deny_public_access"),
            "database_postgresql_allowed_cidrs": obj.get("database.postgresql.allowed_cidrs"),
            "database_mysql_deny_public_access": obj.get("database.mysql.deny_public_access"),
            "database_mysql_allowed_cidrs": obj.get("database.mysql.allowed_cidrs"),
            "database_mongodb_deny_public_access": obj.get("database.mongodb.deny_public_access"),
            "database_mongodb_allowed_cidrs": obj.get("database.mongodb.allowed_cidrs"),
            "database_redis_deny_public_access": obj.get("database.redis.deny_public_access"),
            "database_redis_allowed_cidrs": obj.get("database.redis.allowed_cidrs"),
            "aws_iam_admin_group": obj.get("aws.iam.admin_group"),
            "aws_eks_ec2_metadata_imds": obj.get("aws.eks.ec2.metadata_imds"),
            "pleco_resources_ttl": obj.get("pleco.resources_ttl"),
            "registry_mirroring_mode": obj.get("registry.mirroring_mode"),
            "nginx_vcpu_request_in_milli_cpu": obj.get("nginx.vcpu.request_in_milli_cpu"),
            "nginx_vcpu_limit_in_milli_cpu": obj.get("nginx.vcpu.limit_in_milli_cpu"),
            "nginx_memory_request_in_mib": obj.get("nginx.memory.request_in_mib"),
            "nginx_memory_limit_in_mib": obj.get("nginx.memory.limit_in_mib"),
            "nginx_hpa_cpu_utilization_percentage_threshold": obj.get("nginx.hpa.cpu_utilization_percentage_threshold"),
            "nginx_hpa_min_number_instances": obj.get("nginx.hpa.min_number_instances"),
            "nginx_hpa_max_number_instances": obj.get("nginx.hpa.max_number_instances")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


