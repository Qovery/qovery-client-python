# EnvironmentVariableRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | key is case sensitive. | 
**value** | **str** | value of the env variable. | [optional] 
**mount_path** | **str** | should be set for file only. variable mount path makes variable a file (where file should be mounted). | [optional] 

## Example

```python
from qovery.models.environment_variable_request import EnvironmentVariableRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentVariableRequest from a JSON string
environment_variable_request_instance = EnvironmentVariableRequest.from_json(json)
# print the JSON string representation of the object
print EnvironmentVariableRequest.to_json()

# convert the object into a dict
environment_variable_request_dict = environment_variable_request_instance.to_dict()
# create an instance of EnvironmentVariableRequest from a dict
environment_variable_request_form_dict = environment_variable_request.from_dict(environment_variable_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


