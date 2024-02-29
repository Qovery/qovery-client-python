# EnvironmentLogScope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**EnvironmentLogTypeEnum**](EnvironmentLogTypeEnum.md) |  | [optional] 
**name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from qovery.models.environment_log_scope import EnvironmentLogScope

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentLogScope from a JSON string
environment_log_scope_instance = EnvironmentLogScope.from_json(json)
# print the JSON string representation of the object
print EnvironmentLogScope.to_json()

# convert the object into a dict
environment_log_scope_dict = environment_log_scope_instance.to_dict()
# create an instance of EnvironmentLogScope from a dict
environment_log_scope_form_dict = environment_log_scope.from_dict(environment_log_scope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


