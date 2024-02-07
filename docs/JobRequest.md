# JobRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name is case insensitive | 
**description** | **str** |  | [optional] 
**cpu** | **int** | unit is millicores (m). 1000m &#x3D; 1 cpu | [optional] [default to 500]
**memory** | **int** | unit is MB. 1024 MB &#x3D; 1GB | [optional] [default to 512]
**max_nb_restart** | **int** | Maximum number of restart allowed before the job is considered as failed 0 means that no restart/crash of the job is allowed  | [optional] [default to 0]
**max_duration_seconds** | **int** | Maximum number of seconds allowed for the job to run before killing it and mark it as failed  | [optional] 
**auto_preview** | **bool** | Indicates if the &#39;environment preview option&#39; is enabled for this container.   If enabled, a preview environment will be automatically cloned when &#x60;/preview&#x60; endpoint is called.   If not specified, it takes the value of the &#x60;auto_preview&#x60; property from the associated environment.  | [optional] 
**port** | **int** | Port where to run readiness and liveliness probes checks. The port will not be exposed externally | [optional] 
**source** | [**JobRequestAllOfSource**](JobRequestAllOfSource.md) |  | [optional] 
**healthchecks** | [**Healthcheck**](Healthcheck.md) |  | 
**schedule** | [**JobRequestAllOfSchedule**](JobRequestAllOfSchedule.md) |  | [optional] 
**auto_deploy** | **bool** | Specify if the job will be automatically updated after receiving a new image tag or a new commit according to the source type.  The new image tag shall be communicated via the \&quot;Auto Deploy job\&quot; endpoint https://api-doc.qovery.com/#tag/Jobs/operation/autoDeployJobEnvironments  | [optional] 

## Example

```python
from qovery.models.job_request import JobRequest

# TODO update the JSON string below
json = "{}"
# create an instance of JobRequest from a JSON string
job_request_instance = JobRequest.from_json(json)
# print the JSON string representation of the object
print JobRequest.to_json()

# convert the object into a dict
job_request_dict = job_request_instance.to_dict()
# create an instance of JobRequest from a dict
job_request_form_dict = job_request.from_dict(job_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


