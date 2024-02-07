# ListJobDeploymentHistory200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **float** |  | 
**page_size** | **float** |  | 
**results** | [**List[DeploymentHistoryJobResponse]**](DeploymentHistoryJobResponse.md) |  | [optional] 

## Example

```python
from qovery.models.list_job_deployment_history200_response import ListJobDeploymentHistory200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListJobDeploymentHistory200Response from a JSON string
list_job_deployment_history200_response_instance = ListJobDeploymentHistory200Response.from_json(json)
# print the JSON string representation of the object
print ListJobDeploymentHistory200Response.to_json()

# convert the object into a dict
list_job_deployment_history200_response_dict = list_job_deployment_history200_response_instance.to_dict()
# create an instance of ListJobDeploymentHistory200Response from a dict
list_job_deployment_history200_response_form_dict = list_job_deployment_history200_response.from_dict(list_job_deployment_history200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


