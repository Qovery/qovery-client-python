# VariableAlias


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**key** | **str** |  | 
**value** | **str** |  | [optional] 
**mount_path** | **str** |  | 
**scope** | [**APIVariableScopeEnum**](APIVariableScopeEnum.md) |  | 
**variable_type** | [**APIVariableTypeEnum**](APIVariableTypeEnum.md) |  | 

## Example

```python
from qovery.models.variable_alias import VariableAlias

# TODO update the JSON string below
json = "{}"
# create an instance of VariableAlias from a JSON string
variable_alias_instance = VariableAlias.from_json(json)
# print the JSON string representation of the object
print VariableAlias.to_json()

# convert the object into a dict
variable_alias_dict = variable_alias_instance.to_dict()
# create an instance of VariableAlias from a dict
variable_alias_form_dict = variable_alias.from_dict(variable_alias_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


