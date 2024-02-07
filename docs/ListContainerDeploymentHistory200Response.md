# ListContainerDeploymentHistory200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **float** |  | 
**page_size** | **float** |  | 
**results** | [**List[DeploymentHistoryContainer]**](DeploymentHistoryContainer.md) |  | [optional] 

## Example

```python
from qovery.models.list_container_deployment_history200_response import ListContainerDeploymentHistory200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListContainerDeploymentHistory200Response from a JSON string
list_container_deployment_history200_response_instance = ListContainerDeploymentHistory200Response.from_json(json)
# print the JSON string representation of the object
print ListContainerDeploymentHistory200Response.to_json()

# convert the object into a dict
list_container_deployment_history200_response_dict = list_container_deployment_history200_response_instance.to_dict()
# create an instance of ListContainerDeploymentHistory200Response from a dict
list_container_deployment_history200_response_form_dict = list_container_deployment_history200_response.from_dict(list_container_deployment_history200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


