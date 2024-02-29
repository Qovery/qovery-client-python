# VariableOverride


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the overriden variable | 
**key** | **str** | The key of the overriden variable | 
**value** | **str** | The value of the overriden variable | [optional] 
**mount_path** | **str** | The mounth path of the overriden variable (only if environment variable type is &#39;file&#39;) | 
**scope** | [**APIVariableScopeEnum**](APIVariableScopeEnum.md) |  | 
**variable_type** | [**APIVariableTypeEnum**](APIVariableTypeEnum.md) |  | 

## Example

```python
from qovery.models.variable_override import VariableOverride

# TODO update the JSON string below
json = "{}"
# create an instance of VariableOverride from a JSON string
variable_override_instance = VariableOverride.from_json(json)
# print the JSON string representation of the object
print VariableOverride.to_json()

# convert the object into a dict
variable_override_dict = variable_override_instance.to_dict()
# create an instance of VariableOverride from a dict
variable_override_form_dict = variable_override.from_dict(variable_override_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


