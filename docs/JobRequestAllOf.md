# JobRequestAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name is case insensitive | 
**description** | **str** |  | [optional] 
**cpu** | **int** | unit is millicores (m). 1000m &#x3D; 1 cpu | [optional]  if omitted the server will use the default value of 500
**memory** | **int** | unit is MB. 1024 MB &#x3D; 1GB | [optional]  if omitted the server will use the default value of 512
**max_nb_restart** | **int** | Maximum number of restart allowed before the job is considered as failed 0 means that no restart/crash of the job is allowed  | [optional]  if omitted the server will use the default value of 0
**max_duration_seconds** | **int** | Maximum number of seconds allowed for the job to run before killing it and mark it as failed  | [optional] 
**auto_preview** | **bool** | Indicates if the &#39;environment preview option&#39; is enabled for this container.   If enabled, a preview environment will be automatically cloned when &#x60;/preview&#x60; endpoint is called.   If not specified, it takes the value of the &#x60;auto_preview&#x60; property from the associated environment.  | [optional] 
**port** | **int, none_type** | Port where to run readiness and liveliness probes checks. The port will not be exposed externally | [optional] 
**source** | [**JobRequestAllOfSource**](JobRequestAllOfSource.md) |  | [optional] 
**healthchecks** | [**Healthcheck**](Healthcheck.md) |  | [optional] 
**schedule** | [**JobRequestAllOfSchedule**](JobRequestAllOfSchedule.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


