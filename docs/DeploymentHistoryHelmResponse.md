# DeploymentHistoryHelmResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**name** | **str** | name of the helm | [optional] 
**status** | [**StateEnum**](StateEnum.md) |  | [optional] 
**commit** | [**Commit**](Commit.md) |  | [optional] 
**repository** | [**DeploymentHistoryHelmResponseAllOfRepository**](DeploymentHistoryHelmResponseAllOfRepository.md) |  | [optional] 

## Example

```python
from qovery.models.deployment_history_helm_response import DeploymentHistoryHelmResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentHistoryHelmResponse from a JSON string
deployment_history_helm_response_instance = DeploymentHistoryHelmResponse.from_json(json)
# print the JSON string representation of the object
print DeploymentHistoryHelmResponse.to_json()

# convert the object into a dict
deployment_history_helm_response_dict = deployment_history_helm_response_instance.to_dict()
# create an instance of DeploymentHistoryHelmResponse from a dict
deployment_history_helm_response_form_dict = deployment_history_helm_response.from_dict(deployment_history_helm_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


