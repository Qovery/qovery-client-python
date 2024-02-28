# LifecycleJobResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**environment** | [**ReferenceObject**](ReferenceObject.md) |  | 
**maximum_cpu** | **int** | Maximum cpu that can be allocated to the job based on organization cluster configuration. unit is millicores (m). 1000m &#x3D; 1 cpu | 
**maximum_memory** | **int** | Maximum memory that can be allocated to the job based on organization cluster configuration. unit is MB. 1024 MB &#x3D; 1GB | 
**name** | **str** | name is case insensitive | 
**description** | **str** |  | [optional] 
**cpu** | **int** | unit is millicores (m). 1000m &#x3D; 1 cpu | 
**memory** | **int** | unit is MB. 1024 MB &#x3D; 1GB | 
**max_nb_restart** | **int** | Maximum number of restart allowed before the job is considered as failed 0 means that no restart/crash of the job is allowed  | [optional] 
**max_duration_seconds** | **int** | Maximum number of seconds allowed for the job to run before killing it and mark it as failed  | [optional] 
**auto_preview** | **bool** | Indicates if the &#39;environment preview option&#39; is enabled for this container.   If enabled, a preview environment will be automatically cloned when &#x60;/preview&#x60; endpoint is called.   If not specified, it takes the value of the &#x60;auto_preview&#x60; property from the associated environment.  | 
**port** | **int** | Port where to run readiness and liveliness probes checks. The port will not be exposed externally | [optional] 
**source** | [**BaseJobResponseAllOfSource**](BaseJobResponseAllOfSource.md) |  | 
**healthchecks** | [**Healthcheck**](Healthcheck.md) |  | 
**auto_deploy** | **bool** | Specify if the job will be automatically updated after receiving a new image tag or a new commit according to the source type.  The new image tag shall be communicated via the \&quot;Auto Deploy job\&quot; endpoint https://api-doc.qovery.com/#tag/Jobs/operation/autoDeployJobEnvironments  | [optional] 
**job_type** | **str** |  | 
**schedule** | [**LifecycleJobResponseAllOfSchedule**](LifecycleJobResponseAllOfSchedule.md) |  | 

## Example

```python
from qovery.models.lifecycle_job_response import LifecycleJobResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LifecycleJobResponse from a JSON string
lifecycle_job_response_instance = LifecycleJobResponse.from_json(json)
# print the JSON string representation of the object
print LifecycleJobResponse.to_json()

# convert the object into a dict
lifecycle_job_response_dict = lifecycle_job_response_instance.to_dict()
# create an instance of LifecycleJobResponse from a dict
lifecycle_job_response_form_dict = lifecycle_job_response.from_dict(lifecycle_job_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


