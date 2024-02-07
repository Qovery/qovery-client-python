# DeploymentHistoryJobResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**name** | **str** | name of the job | [optional] 
**status** | [**StateEnum**](StateEnum.md) |  | [optional] 
**image_name** | **str** |  | [optional] 
**tag** | **str** |  | [optional] 
**commit** | [**Commit**](Commit.md) |  | [optional] 
**schedule** | [**DeploymentHistoryJobResponseAllOfSchedule**](DeploymentHistoryJobResponseAllOfSchedule.md) |  | [optional] 
**arguments** | **List[str]** |  | [optional] 
**entrypoint** | **str** |  | [optional] 

## Example

```python
from qovery.models.deployment_history_job_response import DeploymentHistoryJobResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentHistoryJobResponse from a JSON string
deployment_history_job_response_instance = DeploymentHistoryJobResponse.from_json(json)
# print the JSON string representation of the object
print DeploymentHistoryJobResponse.to_json()

# convert the object into a dict
deployment_history_job_response_dict = deployment_history_job_response_instance.to_dict()
# create an instance of DeploymentHistoryJobResponse from a dict
deployment_history_job_response_form_dict = deployment_history_job_response.from_dict(deployment_history_job_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


