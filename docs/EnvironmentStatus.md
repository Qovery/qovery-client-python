# EnvironmentStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**state** | [**StateEnum**](StateEnum.md) |  | 
**last_deployment_date** | **datetime** |  | [optional] 
**last_deployment_state** | [**StateEnum**](StateEnum.md) |  | 
**last_deployment_id** | **str** |  | [optional] 
**total_deployment_duration_in_seconds** | **int** |  | [optional] 
**origin** | [**EnvironmentStatusEventOriginEnum**](EnvironmentStatusEventOriginEnum.md) |  | [optional] 
**triggered_by** | **str** |  | [optional] 

## Example

```python
from qovery.models.environment_status import EnvironmentStatus

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentStatus from a JSON string
environment_status_instance = EnvironmentStatus.from_json(json)
# print the JSON string representation of the object
print EnvironmentStatus.to_json()

# convert the object into a dict
environment_status_dict = environment_status_instance.to_dict()
# create an instance of EnvironmentStatus from a dict
environment_status_form_dict = environment_status.from_dict(environment_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


