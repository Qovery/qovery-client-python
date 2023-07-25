# JobAdvancedSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build_timeout_max_sec** | **int** | define the max timeout for the build | [optional]  if omitted the server will use the default value of 1800
**build_cpu_max_in_milli** | **int** | define the max cpu resources (in milli) | [optional]  if omitted the server will use the default value of 4000
**build_ram_max_in_gib** | **int** | define the max ram resources (in gib) | [optional]  if omitted the server will use the default value of 8
**deployment_termination_grace_period_seconds** | **int** | define how long in seconds an application is supposed to be stopped gracefully | [optional]  if omitted the server will use the default value of 60
**job_delete_ttl_seconds_after_finished** | **int, none_type** |  | [optional] 
**cronjob_concurrency_policy** | **str** |  | [optional]  if omitted the server will use the default value of "Forbid"
**cronjob_failed_jobs_history_limit** | **int** |  | [optional]  if omitted the server will use the default value of 1
**cronjob_success_jobs_history_limit** | **int** |  | [optional]  if omitted the server will use the default value of 1
**security_service_account_name** | **str** | Allows you to set an existing Kubernetes service account name  | [optional]  if omitted the server will use the default value of ""
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


