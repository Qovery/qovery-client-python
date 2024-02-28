# EnvironmentLogs


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**timestamp** | **datetime** |  | 
**details** | [**EnvironmentLogsDetails**](EnvironmentLogsDetails.md) |  | 
**error** | [**EnvironmentLogsError**](EnvironmentLogsError.md) |  | [optional] 
**message** | [**EnvironmentLogsMessage**](EnvironmentLogsMessage.md) |  | [optional] 

## Example

```python
from qovery.models.environment_logs import EnvironmentLogs

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentLogs from a JSON string
environment_logs_instance = EnvironmentLogs.from_json(json)
# print the JSON string representation of the object
print EnvironmentLogs.to_json()

# convert the object into a dict
environment_logs_dict = environment_logs_instance.to_dict()
# create an instance of EnvironmentLogs from a dict
environment_logs_form_dict = environment_logs.from_dict(environment_logs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


