# JobAdvancedSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_delete_ttl_seconds_after_finished** | **int, none_type** |  | [optional] 
**cronjob_concurrency_policy** | **str** |  | [optional]  if omitted the server will use the default value of "Forbid"
**cronjob_failed_jobs_history_limit** | **int** |  | [optional]  if omitted the server will use the default value of 1
**cronjob_success_jobs_history_limit** | **int** |  | [optional]  if omitted the server will use the default value of 1
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


