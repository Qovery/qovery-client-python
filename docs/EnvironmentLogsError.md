# EnvironmentLogsError


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag** | **str** |  | [optional] 
**user_log_message** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**hint_message** | **str** |  | [optional] 
**underlying_error** | [**EnvironmentLogsErrorUnderlyingError**](EnvironmentLogsErrorUnderlyingError.md) |  | [optional] 

## Example

```python
from qovery.models.environment_logs_error import EnvironmentLogsError

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentLogsError from a JSON string
environment_logs_error_instance = EnvironmentLogsError.from_json(json)
# print the JSON string representation of the object
print EnvironmentLogsError.to_json()

# convert the object into a dict
environment_logs_error_dict = environment_logs_error_instance.to_dict()
# create an instance of EnvironmentLogsError from a dict
environment_logs_error_form_dict = environment_logs_error.from_dict(environment_logs_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


