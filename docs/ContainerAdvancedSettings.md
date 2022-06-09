# ContainerAdvancedSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_delay_start_time_sec** | **int** |  | [optional] 
**deployment_custom_domain_check_enabled** | **bool** | disable custom domain check when deploying an application | [optional] 
**build_timeout_max_sec** | **int** |  | [optional] 
**network_ingress_proxy_body_size_mb** | **int** |  | [optional] 
**network_ingress_enable_cors** | **bool** |  | [optional] 
**network_ingress_cors_allow_origin** | **str** |  | [optional] 
**network_ingress_cors_allow_methods** | **str** |  | [optional] 
**network_ingress_cors_allow_headers** | **str** |  | [optional] 
**readiness_probe_type** | **str** | &#x60;NONE&#x60; disable readiness probe &#x60;TCP&#x60; enable TCP readiness probe &#x60;HTTP&#x60; enable HTTP readiness probe  | [optional] 
**readiness_probe_http_get_path** | **str** | HTTP GET path to check status (must returns 2xx E.g \&quot;/healtz\&quot;) - only usable with TYPE &#x3D; HTTP | [optional]  if omitted the server will use the default value of "/"
**readiness_probe_initial_delay_seconds** | **int** | Delay before liveness probe is initiated | [optional] 
**readiness_probe_period_seconds** | **int** | How often to perform the probe | [optional] 
**readiness_probe_timeout_seconds** | **int** | When the probe times out | [optional] 
**readiness_probe_success_threshold** | **int** | Minimum consecutive successes for the probe to be considered successful after having failed. | [optional] 
**readiness_probe_failure_threshold** | **int** | Minimum consecutive failures for the probe to be considered failed after having succeeded. | [optional] 
**liveness_probe_type** | **str** | &#x60;NONE&#x60; disable liveness probe &#x60;TCP&#x60; enable TCP liveness probe &#x60;HTTP&#x60; enable HTTP liveness probe  | [optional] 
**liveness_probe_http_get_path** | **str** | HTTP GET path to check status (must returns 2xx E.g \&quot;/healtz\&quot;) - only usable with TYPE &#x3D; HTTP | [optional]  if omitted the server will use the default value of "/"
**liveness_probe_initial_delay_seconds** | **int** | Delay before liveness probe is initiated | [optional] 
**liveness_probe_period_seconds** | **int** | How often to perform the probe | [optional] 
**liveness_probe_timeout_seconds** | **int** | When the probe times out | [optional] 
**liveness_probe_success_threshold** | **int** | Minimum consecutive successes for the probe to be considered successful after having failed. | [optional] 
**liveness_probe_failure_threshold** | **int** | Minimum consecutive failures for the probe to be considered failed after having succeeded. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


