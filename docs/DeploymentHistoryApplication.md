# DeploymentHistoryApplication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**commit** | [**Commit**](Commit.md) |  | [optional] 
**status** | [**StateEnum**](StateEnum.md) |  | [optional] 

## Example

```python
from qovery.models.deployment_history_application import DeploymentHistoryApplication

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentHistoryApplication from a JSON string
deployment_history_application_instance = DeploymentHistoryApplication.from_json(json)
# print the JSON string representation of the object
print DeploymentHistoryApplication.to_json()

# convert the object into a dict
deployment_history_application_dict = deployment_history_application_instance.to_dict()
# create an instance of DeploymentHistoryApplication from a dict
deployment_history_application_form_dict = deployment_history_application.from_dict(deployment_history_application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


