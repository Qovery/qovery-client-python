# EnvironmentLogsMessage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**safe_message** | **str** |  | [optional] 
**full_details** | **str** |  | [optional] 

## Example

```python
from qovery.models.environment_logs_message import EnvironmentLogsMessage

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentLogsMessage from a JSON string
environment_logs_message_instance = EnvironmentLogsMessage.from_json(json)
# print the JSON string representation of the object
print EnvironmentLogsMessage.to_json()

# convert the object into a dict
environment_logs_message_dict = environment_logs_message_instance.to_dict()
# create an instance of EnvironmentLogsMessage from a dict
environment_logs_message_form_dict = environment_logs_message.from_dict(environment_logs_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


