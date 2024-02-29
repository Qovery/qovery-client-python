# EnvironmentVariableOverride


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**key** | **str** |  | 
**value** | **str** |  | 
**mount_path** | **str** |  | 
**scope** | [**APIVariableScopeEnum**](APIVariableScopeEnum.md) |  | 
**variable_type** | [**APIVariableTypeEnum**](APIVariableTypeEnum.md) |  | 

## Example

```python
from qovery.models.environment_variable_override import EnvironmentVariableOverride

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentVariableOverride from a JSON string
environment_variable_override_instance = EnvironmentVariableOverride.from_json(json)
# print the JSON string representation of the object
print EnvironmentVariableOverride.to_json()

# convert the object into a dict
environment_variable_override_dict = environment_variable_override_instance.to_dict()
# create an instance of EnvironmentVariableOverride from a dict
environment_variable_override_form_dict = environment_variable_override.from_dict(environment_variable_override_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


