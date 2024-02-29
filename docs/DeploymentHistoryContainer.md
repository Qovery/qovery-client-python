# DeploymentHistoryContainer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**name** | **str** | name of the container | [optional] 
**status** | [**StateEnum**](StateEnum.md) |  | [optional] 
**image_name** | **str** |  | [optional] 
**tag** | **str** |  | [optional] 
**arguments** | **List[str]** |  | [optional] 
**entrypoint** | **str** |  | [optional] 

## Example

```python
from qovery.models.deployment_history_container import DeploymentHistoryContainer

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentHistoryContainer from a JSON string
deployment_history_container_instance = DeploymentHistoryContainer.from_json(json)
# print the JSON string representation of the object
print DeploymentHistoryContainer.to_json()

# convert the object into a dict
deployment_history_container_dict = deployment_history_container_instance.to_dict()
# create an instance of DeploymentHistoryContainer from a dict
deployment_history_container_form_dict = deployment_history_container.from_dict(deployment_history_container_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


