# EnvironmentVariableAlias


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
from qovery.models.environment_variable_alias import EnvironmentVariableAlias

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentVariableAlias from a JSON string
environment_variable_alias_instance = EnvironmentVariableAlias.from_json(json)
# print the JSON string representation of the object
print EnvironmentVariableAlias.to_json()

# convert the object into a dict
environment_variable_alias_dict = environment_variable_alias_instance.to_dict()
# create an instance of EnvironmentVariableAlias from a dict
environment_variable_alias_form_dict = environment_variable_alias.from_dict(environment_variable_alias_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


