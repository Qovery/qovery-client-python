# VariableEditRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | the key of the environment variable | 
**value** | **str** | the value of the environment variable | 

## Example

```python
from qovery.models.variable_edit_request import VariableEditRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VariableEditRequest from a JSON string
variable_edit_request_instance = VariableEditRequest.from_json(json)
# print the JSON string representation of the object
print VariableEditRequest.to_json()

# convert the object into a dict
variable_edit_request_dict = variable_edit_request_instance.to_dict()
# create an instance of VariableEditRequest from a dict
variable_edit_request_form_dict = variable_edit_request.from_dict(variable_edit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


