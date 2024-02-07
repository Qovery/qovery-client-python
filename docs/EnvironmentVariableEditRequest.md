# EnvironmentVariableEditRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | key is case sensitive | 
**value** | **str** | value of the env variable. | [optional] 

## Example

```python
from qovery.models.environment_variable_edit_request import EnvironmentVariableEditRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentVariableEditRequest from a JSON string
environment_variable_edit_request_instance = EnvironmentVariableEditRequest.from_json(json)
# print the JSON string representation of the object
print EnvironmentVariableEditRequest.to_json()

# convert the object into a dict
environment_variable_edit_request_dict = environment_variable_edit_request_instance.to_dict()
# create an instance of EnvironmentVariableEditRequest from a dict
environment_variable_edit_request_form_dict = environment_variable_edit_request.from_dict(environment_variable_edit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


