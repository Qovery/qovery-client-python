# DeploymentStageWithServicesStatuses


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applications** | [**List[Status]**](Status.md) |  | [optional] 
**containers** | [**List[Status]**](Status.md) |  | [optional] 
**jobs** | [**List[Status]**](Status.md) |  | [optional] 
**databases** | [**List[Status]**](Status.md) |  | [optional] 
**helms** | [**List[Status]**](Status.md) |  | [optional] 
**stage** | [**Stage**](Stage.md) |  | [optional] 

## Example

```python
from qovery.models.deployment_stage_with_services_statuses import DeploymentStageWithServicesStatuses

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentStageWithServicesStatuses from a JSON string
deployment_stage_with_services_statuses_instance = DeploymentStageWithServicesStatuses.from_json(json)
# print the JSON string representation of the object
print DeploymentStageWithServicesStatuses.to_json()

# convert the object into a dict
deployment_stage_with_services_statuses_dict = deployment_stage_with_services_statuses_instance.to_dict()
# create an instance of DeploymentStageWithServicesStatuses from a dict
deployment_stage_with_services_statuses_form_dict = deployment_stage_with_services_statuses.from_dict(deployment_stage_with_services_statuses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


