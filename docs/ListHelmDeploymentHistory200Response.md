# ListHelmDeploymentHistory200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **float** |  | 
**page_size** | **float** |  | 
**results** | [**List[DeploymentHistoryHelmResponse]**](DeploymentHistoryHelmResponse.md) |  | [optional] 

## Example

```python
from qovery.models.list_helm_deployment_history200_response import ListHelmDeploymentHistory200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListHelmDeploymentHistory200Response from a JSON string
list_helm_deployment_history200_response_instance = ListHelmDeploymentHistory200Response.from_json(json)
# print the JSON string representation of the object
print ListHelmDeploymentHistory200Response.to_json()

# convert the object into a dict
list_helm_deployment_history200_response_dict = list_helm_deployment_history200_response_instance.to_dict()
# create an instance of ListHelmDeploymentHistory200Response from a dict
list_helm_deployment_history200_response_form_dict = list_helm_deployment_history200_response.from_dict(list_helm_deployment_history200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


