# EnvironmentStatusesWithStages


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | [**EnvironmentStatus**](EnvironmentStatus.md) |  | [optional] 
**stages** | [**List[DeploymentStageWithServicesStatuses]**](DeploymentStageWithServicesStatuses.md) |  | [optional] 

## Example

```python
from qovery.models.environment_statuses_with_stages import EnvironmentStatusesWithStages

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentStatusesWithStages from a JSON string
environment_statuses_with_stages_instance = EnvironmentStatusesWithStages.from_json(json)
# print the JSON string representation of the object
print EnvironmentStatusesWithStages.to_json()

# convert the object into a dict
environment_statuses_with_stages_dict = environment_statuses_with_stages_instance.to_dict()
# create an instance of EnvironmentStatusesWithStages from a dict
environment_statuses_with_stages_form_dict = environment_statuses_with_stages.from_dict(environment_statuses_with_stages_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


