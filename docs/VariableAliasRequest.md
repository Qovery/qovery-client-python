# VariableAliasRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | the value to be used as Alias of the targeted environment variable. | 
**alias_scope** | [**APIVariableScopeEnum**](APIVariableScopeEnum.md) |  | 
**alias_parent_id** | **str** | the id of the variable that is aliased. | 

## Example

```python
from qovery.models.variable_alias_request import VariableAliasRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VariableAliasRequest from a JSON string
variable_alias_request_instance = VariableAliasRequest.from_json(json)
# print the JSON string representation of the object
print VariableAliasRequest.to_json()

# convert the object into a dict
variable_alias_request_dict = variable_alias_request_instance.to_dict()
# create an instance of VariableAliasRequest from a dict
variable_alias_request_form_dict = variable_alias_request.from_dict(variable_alias_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


