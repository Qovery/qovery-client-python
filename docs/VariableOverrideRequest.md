# VariableOverrideRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | the value to be used as Override of the targeted environment variable. | 
**override_scope** | [**APIVariableScopeEnum**](APIVariableScopeEnum.md) |  | 
**override_parent_id** | **str** | the id of the variable that is aliased. | 

## Example

```python
from qovery.models.variable_override_request import VariableOverrideRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VariableOverrideRequest from a JSON string
variable_override_request_instance = VariableOverrideRequest.from_json(json)
# print the JSON string representation of the object
print VariableOverrideRequest.to_json()

# convert the object into a dict
variable_override_request_dict = variable_override_request_instance.to_dict()
# create an instance of VariableOverrideRequest from a dict
variable_override_request_form_dict = variable_override_request.from_dict(variable_override_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


