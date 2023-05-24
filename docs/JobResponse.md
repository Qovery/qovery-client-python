# JobResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**environment** | [**ReferenceObject**](ReferenceObject.md) |  | 
**registry** | [**ReferenceObject**](ReferenceObject.md) |  | 
**maximum_cpu** | **int** | Maximum cpu that can be allocated to the job based on organization cluster configuration. unit is millicores (m). 1000m &#x3D; 1 cpu | 
**maximum_memory** | **int** | Maximum memory that can be allocated to the job based on organization cluster configuration. unit is MB. 1024 MB &#x3D; 1GB | 
**name** | **str** | name is case insensitive | 
**cpu** | **int** | unit is millicores (m). 1000m &#x3D; 1 cpu | 
**memory** | **int** | unit is MB. 1024 MB &#x3D; 1GB | 
**auto_preview** | **bool** | Indicates if the &#39;environment preview option&#39; is enabled for this container.   If enabled, a preview environment will be automatically cloned when &#x60;/preview&#x60; endpoint is called.   If not specified, it takes the value of the &#x60;auto_preview&#x60; property from the associated environment.  | 
**updated_at** | **datetime** |  | [optional] [readonly] 
**description** | **str** |  | [optional] 
**max_nb_restart** | **int** | Maximum number of restart allowed before the job is considered as failed 0 means that no restart/crash of the job is allowed  | [optional] 
**max_duration_seconds** | **int** | Maximum number of seconds allowed for the job to run before killing it and mark it as failed  | [optional] 
**port** | **int, none_type** | Port where to run readiness and liveliness probes checks. The port will not be exposed externally | [optional] 
**source** | [**JobResponseAllOfSource**](JobResponseAllOfSource.md) |  | [optional] 
**healthchecks** | [**Healthcheck**](Healthcheck.md) |  | [optional] 
**schedule** | [**JobResponseAllOfSchedule**](JobResponseAllOfSchedule.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


