# DeploymentHistory


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**name** | **str** | name of the service | [optional] 
**commit** | [**Commit**](Commit.md) |  | [optional] 
**status** | [**DeploymentHistoryStatusEnum**](DeploymentHistoryStatusEnum.md) |  | [optional] 

## Example

```python
from qovery.models.deployment_history import DeploymentHistory

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentHistory from a JSON string
deployment_history_instance = DeploymentHistory.from_json(json)
# print the JSON string representation of the object
print DeploymentHistory.to_json()

# convert the object into a dict
deployment_history_dict = deployment_history_instance.to_dict()
# create an instance of DeploymentHistory from a dict
deployment_history_form_dict = deployment_history.from_dict(deployment_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


