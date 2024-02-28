# EnvironmentVariableResponseList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[EnvironmentVariable]**](EnvironmentVariable.md) |  | [optional] 

## Example

```python
from qovery.models.environment_variable_response_list import EnvironmentVariableResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentVariableResponseList from a JSON string
environment_variable_response_list_instance = EnvironmentVariableResponseList.from_json(json)
# print the JSON string representation of the object
print EnvironmentVariableResponseList.to_json()

# convert the object into a dict
environment_variable_response_list_dict = environment_variable_response_list_instance.to_dict()
# create an instance of EnvironmentVariableResponseList from a dict
environment_variable_response_list_form_dict = environment_variable_response_list.from_dict(environment_variable_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


