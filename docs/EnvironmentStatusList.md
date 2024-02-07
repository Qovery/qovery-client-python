# EnvironmentStatusList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[EnvironmentStatus]**](EnvironmentStatus.md) |  | [optional] 

## Example

```python
from qovery.models.environment_status_list import EnvironmentStatusList

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentStatusList from a JSON string
environment_status_list_instance = EnvironmentStatusList.from_json(json)
# print the JSON string representation of the object
print EnvironmentStatusList.to_json()

# convert the object into a dict
environment_status_list_dict = environment_status_list_instance.to_dict()
# create an instance of EnvironmentStatusList from a dict
environment_status_list_form_dict = environment_status_list.from_dict(environment_status_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


