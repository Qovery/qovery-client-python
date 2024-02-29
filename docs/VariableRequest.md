# VariableRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | the key of the environment variable | 
**value** | **str** | the value of the environment variable | 
**mount_path** | **str** | the path where the file will be mounted (only if type &#x3D;file) | [optional] 
**is_secret** | **bool** | if true, the variable will be considered as a secret and will not be accessible after its creation. Only your applications will be able to access its value at build and run time. | 
**variable_scope** | [**APIVariableScopeEnum**](APIVariableScopeEnum.md) |  | 
**variable_parent_id** | **str** | based on the selected scope, it contains the ID of the service, environment or project where the variable is attached | 

## Example

```python
from qovery.models.variable_request import VariableRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VariableRequest from a JSON string
variable_request_instance = VariableRequest.from_json(json)
# print the JSON string representation of the object
print VariableRequest.to_json()

# convert the object into a dict
variable_request_dict = variable_request_instance.to_dict()
# create an instance of VariableRequest from a dict
variable_request_form_dict = variable_request.from_dict(variable_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


