# DeploymentHistoryEnvironment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**status** | [**StateEnum**](StateEnum.md) |  | [optional] 
**origin** | [**OrganizationEventOrigin**](OrganizationEventOrigin.md) |  | [optional] 
**triggered_by** | **str** |  | [optional] 
**applications** | [**List[DeploymentHistoryApplication]**](DeploymentHistoryApplication.md) |  | [optional] 
**containers** | [**List[DeploymentHistoryContainer]**](DeploymentHistoryContainer.md) |  | [optional] 
**databases** | [**List[DeploymentHistoryDatabase]**](DeploymentHistoryDatabase.md) |  | [optional] 
**jobs** | [**List[DeploymentHistoryJobResponse]**](DeploymentHistoryJobResponse.md) |  | [optional] 
**helms** | [**List[DeploymentHistoryHelmResponse]**](DeploymentHistoryHelmResponse.md) |  | [optional] 

## Example

```python
from qovery.models.deployment_history_environment import DeploymentHistoryEnvironment

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentHistoryEnvironment from a JSON string
deployment_history_environment_instance = DeploymentHistoryEnvironment.from_json(json)
# print the JSON string representation of the object
print DeploymentHistoryEnvironment.to_json()

# convert the object into a dict
deployment_history_environment_dict = deployment_history_environment_instance.to_dict()
# create an instance of DeploymentHistoryEnvironment from a dict
deployment_history_environment_form_dict = deployment_history_environment.from_dict(deployment_history_environment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


