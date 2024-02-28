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


from typing import Dict, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, validator

class ApplicationAdvancedSettings(BaseModel):
    """
    ApplicationAdvancedSettings
    """
    deployment_custom_domain_check_enabled: Optional[StrictBool] = Field(None, alias="deployment.custom_domain_check_enabled", description="disable custom domain check when deploying an application")
    deployment_termination_grace_period_seconds: Optional[StrictInt] = Field(None, alias="deployment.termination_grace_period_seconds", description="define how long in seconds an application is supposed to be stopped gracefully")
    deployment_affinity_node_required: Optional[Dict[str, StrictStr]] = Field(None, alias="deployment.affinity.node.required", description="Set pod placement on specific Kubernetes nodes labels")
    deployment_antiaffinity_pod: Optional[StrictStr] = Field(None, alias="deployment.antiaffinity.pod", description="Define how you want pods affinity to behave: * `Preferred` allows, but does not require, pods of a given service are not co-located (or co-hosted) on a single node * `Requirred` ensures that the pods of a given service are not co-located (or co-hosted) on a single node (safer in term of availability but can be expensive depending on the number of replicas) ")
    deployment_update_strategy_type: Optional[StrictStr] = Field(None, alias="deployment.update_strategy.type", description="* `RollingUpdate` gracefully rollout new versions, and automatically rollback if the new version fails to start * `Recreate` stop all current versions and create new ones once all old ones have been shutdown ")
    deployment_update_strategy_rolling_update_max_unavailable_percent: Optional[StrictInt] = Field(None, alias="deployment.update_strategy.rolling_update.max_unavailable_percent", description="Define the percentage of a maximum number of pods that can be unavailable during the update process")
    deployment_update_strategy_rolling_update_max_surge_percent: Optional[StrictInt] = Field(None, alias="deployment.update_strategy.rolling_update.max_surge_percent", description="Define the percentage of the maximum number of pods that can be created over the desired number of pods")
    build_timeout_max_sec: Optional[StrictInt] = Field(None, alias="build.timeout_max_sec")
    build_cpu_max_in_milli: Optional[StrictInt] = Field(None, alias="build.cpu_max_in_milli", description="define the max cpu resources (in milli)")
    build_ram_max_in_gib: Optional[StrictInt] = Field(None, alias="build.ram_max_in_gib", description="define the max ram resources (in gib)")
    network_ingress_proxy_body_size_mb: Optional[StrictInt] = Field(None, alias="network.ingress.proxy_body_size_mb")
    network_ingress_enable_cors: Optional[StrictBool] = Field(None, alias="network.ingress.enable_cors")
    network_ingress_cors_allow_origin: Optional[StrictStr] = Field(None, alias="network.ingress.cors_allow_origin")
    network_ingress_cors_allow_methods: Optional[StrictStr] = Field(None, alias="network.ingress.cors_allow_methods")
    network_ingress_cors_allow_headers: Optional[StrictStr] = Field(None, alias="network.ingress.cors_allow_headers")
    network_ingress_proxy_buffer_size_kb: Optional[StrictInt] = Field(None, alias="network.ingress.proxy_buffer_size_kb", description="header buffer size used while reading response header from upstream")
    network_ingress_keepalive_time_seconds: Optional[StrictInt] = Field(None, alias="network.ingress.keepalive_time_seconds", description="Limits the maximum time (in seconds) during which requests can be processed through one keepalive connection")
    network_ingress_keepalive_timeout_seconds: Optional[StrictInt] = Field(None, alias="network.ingress.keepalive_timeout_seconds", description="Sets a timeout (in seconds) during which an idle keepalive connection to an upstream server will stay open.")
    network_ingress_send_timeout_seconds: Optional[StrictInt] = Field(None, alias="network.ingress.send_timeout_seconds", description="Sets a timeout (in seconds) for transmitting a response to the client")
    network_ingress_proxy_connect_timeout_seconds: Optional[StrictInt] = Field(None, alias="network.ingress.proxy_connect_timeout_seconds", description="Sets a timeout (in seconds) for establishing a connection to a proxied server")
    network_ingress_proxy_send_timeout_seconds: Optional[StrictInt] = Field(None, alias="network.ingress.proxy_send_timeout_seconds", description="Sets a timeout (in seconds) for transmitting a request to the proxied server")
    network_ingress_proxy_read_timeout_seconds: Optional[StrictInt] = Field(None, alias="network.ingress.proxy_read_timeout_seconds", description="Sets a timeout (in seconds) for reading a response from the proxied server")
    network_ingress_proxy_buffering: Optional[StrictStr] = Field(None, alias="network.ingress.proxy_buffering", description="Allows to enable or disable nginx `proxy-request-buffering`")
    network_ingress_whitelist_source_range: Optional[StrictStr] = Field(None, alias="network.ingress.whitelist_source_range", description="list of source ranges to allow access to ingress proxy.  This property can be used to whitelist source IP ranges for ingress proxy. The value is a comma separated list of CIDRs, e.g. 10.0.0.0/24,172.10.0.1 To allow all source ranges, set 0.0.0.0/0. ")
    network_ingress_denylist_source_range: Optional[StrictStr] = Field(None, alias="network.ingress.denylist_source_range", description="list of source ranges to deny access to ingress proxy.  This property can be used to blacklist source IP ranges for ingress proxy. The value is a comma separated list of CIDRs, e.g. 10.0.0.0/24,172.10.0.1 ")
    network_ingress_basic_auth_env_var: Optional[StrictStr] = Field(None, alias="network.ingress.basic_auth_env_var", description="Set the name of an environment variable to use as a basic authentication (`login:crypted_password`) from `htpasswd` command. ")
    network_ingress_enable_sticky_session: Optional[StrictBool] = Field(None, alias="network.ingress.enable_sticky_session", description="Enable the load balancer to bind a user's session to a specific target. This ensures that all requests from the user during the session are sent to the same target ")
    network_ingress_grpc_send_timeout_seconds: Optional[StrictInt] = Field(None, alias="network.ingress.grpc_send_timeout_seconds", description="Sets a timeout (in seconds) for transmitting a request to the grpc server")
    network_ingress_grpc_read_timeout_seconds: Optional[StrictInt] = Field(None, alias="network.ingress.grpc_read_timeout_seconds", description="Sets a timeout (in seconds) for transmitting a request to the grpc server")
    network_ingress_extra_headers: Optional[StrictStr] = Field(None, alias="network.ingress.extra_headers", description="Allows to define response headers")
    hpa_cpu_average_utilization_percent: Optional[StrictInt] = Field(None, alias="hpa.cpu.average_utilization_percent", description="Percentage value of cpu usage at which point pods should scale up.")
    security_service_account_name: Optional[StrictStr] = Field(None, alias="security.service_account_name", description="Allows you to set an existing Kubernetes service account name ")
    security_read_only_root_filesystem: Optional[StrictBool] = Field(None, alias="security.read_only_root_filesystem", description="Mounts the container's root filesystem as read-only ")
    __properties = ["deployment.custom_domain_check_enabled", "deployment.termination_grace_period_seconds", "deployment.affinity.node.required", "deployment.antiaffinity.pod", "deployment.update_strategy.type", "deployment.update_strategy.rolling_update.max_unavailable_percent", "deployment.update_strategy.rolling_update.max_surge_percent", "build.timeout_max_sec", "build.cpu_max_in_milli", "build.ram_max_in_gib", "network.ingress.proxy_body_size_mb", "network.ingress.enable_cors", "network.ingress.cors_allow_origin", "network.ingress.cors_allow_methods", "network.ingress.cors_allow_headers", "network.ingress.proxy_buffer_size_kb", "network.ingress.keepalive_time_seconds", "network.ingress.keepalive_timeout_seconds", "network.ingress.send_timeout_seconds", "network.ingress.proxy_connect_timeout_seconds", "network.ingress.proxy_send_timeout_seconds", "network.ingress.proxy_read_timeout_seconds", "network.ingress.proxy_buffering", "network.ingress.whitelist_source_range", "network.ingress.denylist_source_range", "network.ingress.basic_auth_env_var", "network.ingress.enable_sticky_session", "network.ingress.grpc_send_timeout_seconds", "network.ingress.grpc_read_timeout_seconds", "network.ingress.extra_headers", "hpa.cpu.average_utilization_percent", "security.service_account_name", "security.read_only_root_filesystem"]

    @validator('deployment_antiaffinity_pod')
    def deployment_antiaffinity_pod_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Preferred', 'Requirred'):
            raise ValueError("must be one of enum values ('Preferred', 'Requirred')")
        return value

    @validator('deployment_update_strategy_type')
    def deployment_update_strategy_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('RollingUpdate', 'Recreate'):
            raise ValueError("must be one of enum values ('RollingUpdate', 'Recreate')")
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
    def from_json(cls, json_str: str) -> ApplicationAdvancedSettings:
        """Create an instance of ApplicationAdvancedSettings from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApplicationAdvancedSettings:
        """Create an instance of ApplicationAdvancedSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApplicationAdvancedSettings.parse_obj(obj)

        _obj = ApplicationAdvancedSettings.parse_obj({
            "deployment_custom_domain_check_enabled": obj.get("deployment.custom_domain_check_enabled"),
            "deployment_termination_grace_period_seconds": obj.get("deployment.termination_grace_period_seconds"),
            "deployment_affinity_node_required": obj.get("deployment.affinity.node.required"),
            "deployment_antiaffinity_pod": obj.get("deployment.antiaffinity.pod"),
            "deployment_update_strategy_type": obj.get("deployment.update_strategy.type"),
            "deployment_update_strategy_rolling_update_max_unavailable_percent": obj.get("deployment.update_strategy.rolling_update.max_unavailable_percent"),
            "deployment_update_strategy_rolling_update_max_surge_percent": obj.get("deployment.update_strategy.rolling_update.max_surge_percent"),
            "build_timeout_max_sec": obj.get("build.timeout_max_sec"),
            "build_cpu_max_in_milli": obj.get("build.cpu_max_in_milli"),
            "build_ram_max_in_gib": obj.get("build.ram_max_in_gib"),
            "network_ingress_proxy_body_size_mb": obj.get("network.ingress.proxy_body_size_mb"),
            "network_ingress_enable_cors": obj.get("network.ingress.enable_cors"),
            "network_ingress_cors_allow_origin": obj.get("network.ingress.cors_allow_origin"),
            "network_ingress_cors_allow_methods": obj.get("network.ingress.cors_allow_methods"),
            "network_ingress_cors_allow_headers": obj.get("network.ingress.cors_allow_headers"),
            "network_ingress_proxy_buffer_size_kb": obj.get("network.ingress.proxy_buffer_size_kb"),
            "network_ingress_keepalive_time_seconds": obj.get("network.ingress.keepalive_time_seconds"),
            "network_ingress_keepalive_timeout_seconds": obj.get("network.ingress.keepalive_timeout_seconds"),
            "network_ingress_send_timeout_seconds": obj.get("network.ingress.send_timeout_seconds"),
            "network_ingress_proxy_connect_timeout_seconds": obj.get("network.ingress.proxy_connect_timeout_seconds"),
            "network_ingress_proxy_send_timeout_seconds": obj.get("network.ingress.proxy_send_timeout_seconds"),
            "network_ingress_proxy_read_timeout_seconds": obj.get("network.ingress.proxy_read_timeout_seconds"),
            "network_ingress_proxy_buffering": obj.get("network.ingress.proxy_buffering"),
            "network_ingress_whitelist_source_range": obj.get("network.ingress.whitelist_source_range"),
            "network_ingress_denylist_source_range": obj.get("network.ingress.denylist_source_range"),
            "network_ingress_basic_auth_env_var": obj.get("network.ingress.basic_auth_env_var"),
            "network_ingress_enable_sticky_session": obj.get("network.ingress.enable_sticky_session"),
            "network_ingress_grpc_send_timeout_seconds": obj.get("network.ingress.grpc_send_timeout_seconds"),
            "network_ingress_grpc_read_timeout_seconds": obj.get("network.ingress.grpc_read_timeout_seconds"),
            "network_ingress_extra_headers": obj.get("network.ingress.extra_headers"),
            "hpa_cpu_average_utilization_percent": obj.get("hpa.cpu.average_utilization_percent"),
            "security_service_account_name": obj.get("security.service_account_name"),
            "security_read_only_root_filesystem": obj.get("security.read_only_root_filesystem")
        })
        return _obj


