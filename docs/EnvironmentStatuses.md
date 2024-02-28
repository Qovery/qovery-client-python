# EnvironmentStatuses


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | [**EnvironmentStatus**](EnvironmentStatus.md) |  | [optional] 
**applications** | [**List[Status]**](Status.md) |  | [optional] 
**containers** | [**List[Status]**](Status.md) |  | [optional] 
**jobs** | [**List[Status]**](Status.md) |  | [optional] 
**databases** | [**List[Status]**](Status.md) |  | [optional] 
**helms** | [**List[Status]**](Status.md) |  | [optional] 

## Example

```python
from qovery.models.environment_statuses import EnvironmentStatuses

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentStatuses from a JSON string
environment_statuses_instance = EnvironmentStatuses.from_json(json)
# print the JSON string representation of the object
print EnvironmentStatuses.to_json()

# convert the object into a dict
environment_statuses_dict = environment_statuses_instance.to_dict()
# create an instance of EnvironmentStatuses from a dict
environment_statuses_form_dict = environment_statuses.from_dict(environment_statuses_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


