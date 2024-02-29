# EnvironmentLog


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_at** | **datetime** |  | 
**scope** | [**EnvironmentLogScope**](EnvironmentLogScope.md) |  | [optional] 
**state** | [**StatusKindEnum**](StatusKindEnum.md) |  | [optional] 
**message** | **str** | Log message | 
**execution_id** | **str** | Only for errors. Helps Qovery team to investigate. | [optional] 
**hint** | **str** |  | [optional] 

## Example

```python
from qovery.models.environment_log import EnvironmentLog

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentLog from a JSON string
environment_log_instance = EnvironmentLog.from_json(json)
# print the JSON string representation of the object
print EnvironmentLog.to_json()

# convert the object into a dict
environment_log_dict = environment_log_instance.to_dict()
# create an instance of EnvironmentLog from a dict
environment_log_form_dict = environment_log.from_dict(environment_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


