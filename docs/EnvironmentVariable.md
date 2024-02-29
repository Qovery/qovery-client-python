# EnvironmentVariable


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**key** | **str** | key is case sensitive. | 
**value** | **str** | value of the env variable. | [optional] 
**mount_path** | **str** | should be set for file only. variable mount path makes variable a file (where file should be mounted). | [optional] 
**overridden_variable** | [**EnvironmentVariableOverride**](EnvironmentVariableOverride.md) |  | [optional] 
**aliased_variable** | [**EnvironmentVariableAlias**](EnvironmentVariableAlias.md) |  | [optional] 
**scope** | [**APIVariableScopeEnum**](APIVariableScopeEnum.md) |  | 
**variable_type** | [**APIVariableTypeEnum**](APIVariableTypeEnum.md) |  | [optional] 
**service_id** | **str** |  | [optional] 
**service_name** | **str** |  | [optional] 
**service_type** | [**LinkedServiceTypeEnum**](LinkedServiceTypeEnum.md) |  | [optional] 
**owned_by** | **str** | Entity that created/own the variable (i.e: Qovery, Doppler) | [optional] 

## Example

```python
from qovery.models.environment_variable import EnvironmentVariable

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentVariable from a JSON string
environment_variable_instance = EnvironmentVariable.from_json(json)
# print the JSON string representation of the object
print EnvironmentVariable.to_json()

# convert the object into a dict
environment_variable_dict = environment_variable_instance.to_dict()
# create an instance of EnvironmentVariable from a dict
environment_variable_form_dict = environment_variable.from_dict(environment_variable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


