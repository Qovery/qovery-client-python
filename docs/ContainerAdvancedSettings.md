# ContainerAdvancedSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_custom_domain_check_enabled** | **bool** | disable custom domain check when deploying an application | [optional]  if omitted the server will use the default value of True
**network_ingress_proxy_body_size_mb** | **int** |  | [optional]  if omitted the server will use the default value of 100
**network_ingress_enable_cors** | **bool** |  | [optional]  if omitted the server will use the default value of False
**network_ingress_cors_allow_origin** | **str** |  | [optional]  if omitted the server will use the default value of "*"
**network_ingress_cors_allow_methods** | **str** |  | [optional]  if omitted the server will use the default value of "GET, PUT, POST, DELETE, PATCH, OPTIONS"
**network_ingress_cors_allow_headers** | **str** |  | [optional]  if omitted the server will use the default value of "DNT,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range,Authorization"
**readiness_probe_type** | **str** | &#x60;NONE&#x60; disable readiness probe &#x60;TCP&#x60; enable TCP readiness probe &#x60;HTTP&#x60; enable HTTP readiness probe  | [optional]  if omitted the server will use the default value of "TCP"
**readiness_probe_http_get_path** | **str** | HTTP GET path to check status (must returns 2xx E.g \&quot;/healtz\&quot;) - only usable with TYPE &#x3D; HTTP | [optional]  if omitted the server will use the default value of "/"
**readiness_probe_initial_delay_seconds** | **int** | Delay before liveness probe is initiated | [optional]  if omitted the server will use the default value of 30
**readiness_probe_period_seconds** | **int** | How often to perform the probe | [optional]  if omitted the server will use the default value of 10
**readiness_probe_timeout_seconds** | **int** | When the probe times out | [optional]  if omitted the server will use the default value of 1
**readiness_probe_success_threshold** | **int** | Minimum consecutive successes for the probe to be considered successful after having failed. | [optional]  if omitted the server will use the default value of 1
**readiness_probe_failure_threshold** | **int** | Minimum consecutive failures for the probe to be considered failed after having succeeded. | [optional]  if omitted the server will use the default value of 3
**liveness_probe_type** | **str** | &#x60;NONE&#x60; disable liveness probe &#x60;TCP&#x60; enable TCP liveness probe &#x60;HTTP&#x60; enable HTTP liveness probe  | [optional]  if omitted the server will use the default value of "TCP"
**liveness_probe_http_get_path** | **str** | HTTP GET path to check status (must returns 2xx E.g \&quot;/healtz\&quot;) - only usable with TYPE &#x3D; HTTP | [optional]  if omitted the server will use the default value of "/"
**liveness_probe_initial_delay_seconds** | **int** | Delay before liveness probe is initiated | [optional]  if omitted the server will use the default value of 30
**liveness_probe_period_seconds** | **int** | How often to perform the probe | [optional]  if omitted the server will use the default value of 10
**liveness_probe_timeout_seconds** | **int** | When the probe times out | [optional]  if omitted the server will use the default value of 5
**liveness_probe_success_threshold** | **int** | Minimum consecutive successes for the probe to be considered successful after having failed. | [optional]  if omitted the server will use the default value of 1
**liveness_probe_failure_threshold** | **int** | Minimum consecutive failures for the probe to be considered failed after having succeeded. | [optional]  if omitted the server will use the default value of 3
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


