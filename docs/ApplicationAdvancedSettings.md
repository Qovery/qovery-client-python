# ApplicationAdvancedSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_custom_domain_check_enabled** | **bool** | disable custom domain check when deploying an application | [optional]  if omitted the server will use the default value of True
**deployment_termination_grace_period_seconds** | **int** | define how long in seconds an application is supposed to be stopped gracefully | [optional]  if omitted the server will use the default value of 60
**deployment_affinity_node_required** | **{str: (str,)}** | Set pod placement on specific Kubernetes nodes labels | [optional] 
**deployment_antiaffinity_pod** | **str** | Define how you want pods affinity to behave: * &#x60;Preferred&#x60; allows, but does not require, pods of a given service are not co-located (or co-hosted) on a single node * &#x60;Requirred&#x60; ensures that the pods of a given service are not co-located (or co-hosted) on a single node (safer in term of availability but can be expensive depending on the number of replicas)  | [optional]  if omitted the server will use the default value of "Preferred"
**deployment_update_strategy_type** | **str** | * &#x60;RollingUpdate&#x60; gracefully rollout new versions, and automatically rollback if the new version fails to start * &#x60;Recreate&#x60; stop all current versions and create new ones once all old ones have been shutdown  | [optional]  if omitted the server will use the default value of "RollingUpdate"
**deployment_update_strategy_rolling_update_max_unavailable_percent** | **int** | Define the percentage of a maximum number of pods that can be unavailable during the update process | [optional]  if omitted the server will use the default value of 25
**deployment_update_strategy_rolling_update_max_surge_percent** | **int** | Define the percentage of the maximum number of pods that can be created over the desired number of pods | [optional]  if omitted the server will use the default value of 25
**build_timeout_max_sec** | **int** |  | [optional]  if omitted the server will use the default value of 1800
**build_cpu_max_in_milli** | **int** | define the max cpu resources (in milli) | [optional]  if omitted the server will use the default value of 4000
**build_ram_max_in_gib** | **int** | define the max ram resources (in gib) | [optional]  if omitted the server will use the default value of 8
**network_ingress_proxy_body_size_mb** | **int** |  | [optional]  if omitted the server will use the default value of 100
**network_ingress_enable_cors** | **bool** |  | [optional]  if omitted the server will use the default value of False
**network_ingress_cors_allow_origin** | **str** |  | [optional]  if omitted the server will use the default value of "*"
**network_ingress_cors_allow_methods** | **str** |  | [optional]  if omitted the server will use the default value of "GET, PUT, POST, DELETE, PATCH, OPTIONS"
**network_ingress_cors_allow_headers** | **str** |  | [optional]  if omitted the server will use the default value of "DNT,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range,Authorization"
**network_ingress_proxy_buffer_size_kb** | **int** | header buffer size used while reading response header from upstream | [optional]  if omitted the server will use the default value of 4
**network_ingress_keepalive_time_seconds** | **int** | Limits the maximum time (in seconds) during which requests can be processed through one keepalive connection | [optional]  if omitted the server will use the default value of 3600
**network_ingress_keepalive_timeout_seconds** | **int** | Sets a timeout (in seconds) during which an idle keepalive connection to an upstream server will stay open. | [optional]  if omitted the server will use the default value of 60
**network_ingress_send_timeout_seconds** | **int** | Sets a timeout (in seconds) for transmitting a response to the client | [optional]  if omitted the server will use the default value of 60
**network_ingress_proxy_connect_timeout_seconds** | **int** | Sets a timeout (in seconds) for establishing a connection to a proxied server | [optional]  if omitted the server will use the default value of 60
**network_ingress_proxy_send_timeout_seconds** | **int** | Sets a timeout (in seconds) for transmitting a request to the proxied server | [optional]  if omitted the server will use the default value of 60
**network_ingress_proxy_read_timeout_seconds** | **int** | Sets a timeout (in seconds) for reading a response from the proxied server | [optional]  if omitted the server will use the default value of 60
**network_ingress_whitelist_source_range** | **str** | list of source ranges to allow access to ingress proxy.  This property can be used to whitelist source IP ranges for ingress proxy. The value is a comma separated list of CIDRs, e.g. 10.0.0.0/24,172.10.0.1 To allow all source ranges, set 0.0.0.0/0.  | [optional]  if omitted the server will use the default value of "0.0.0.0/0"
**network_ingress_denylist_source_range** | **str** | list of source ranges to deny access to ingress proxy.  This property can be used to blacklist source IP ranges for ingress proxy. The value is a comma separated list of CIDRs, e.g. 10.0.0.0/24,172.10.0.1  | [optional]  if omitted the server will use the default value of ""
**network_ingress_basic_auth_env_var** | **str** | Set the name of an environment variable to use as a basic authentication (&#x60;login:crypted_password&#x60;) from &#x60;htpasswd&#x60; command.  | [optional]  if omitted the server will use the default value of ""
**network_ingress_enable_sticky_session** | **bool** | Enable the load balancer to bind a user&#39;s session to a specific target. This ensures that all requests from the user during the session are sent to the same target  | [optional]  if omitted the server will use the default value of False
**network_ingress_grpc_send_timeout_seconds** | **int** | Sets a timeout (in seconds) for transmitting a request to the grpc server | [optional]  if omitted the server will use the default value of 60
**network_ingress_grpc_read_timeout_seconds** | **int** | Sets a timeout (in seconds) for transmitting a request to the grpc server | [optional]  if omitted the server will use the default value of 60
**hpa_cpu_average_utilization_percent** | **int** | Percentage value of cpu usage at which point pods should scale up. | [optional]  if omitted the server will use the default value of 60
**security_service_account_name** | **str** | Allows you to set an existing Kubernetes service account name  | [optional]  if omitted the server will use the default value of ""
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


