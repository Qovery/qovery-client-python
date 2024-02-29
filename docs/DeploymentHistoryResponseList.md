# DeploymentHistoryResponseList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[DeploymentHistory]**](DeploymentHistory.md) |  | [optional] 

## Example

```python
from qovery.models.deployment_history_response_list import DeploymentHistoryResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentHistoryResponseList from a JSON string
deployment_history_response_list_instance = DeploymentHistoryResponseList.from_json(json)
# print the JSON string representation of the object
print DeploymentHistoryResponseList.to_json()

# convert the object into a dict
deployment_history_response_list_dict = deployment_history_response_list_instance.to_dict()
# create an instance of DeploymentHistoryResponseList from a dict
deployment_history_response_list_form_dict = deployment_history_response_list.from_dict(deployment_history_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


