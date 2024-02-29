# EnvironmentLogResponseList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[EnvironmentLog]**](EnvironmentLog.md) |  | [optional] 

## Example

```python
from qovery.models.environment_log_response_list import EnvironmentLogResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentLogResponseList from a JSON string
environment_log_response_list_instance = EnvironmentLogResponseList.from_json(json)
# print the JSON string representation of the object
print EnvironmentLogResponseList.to_json()

# convert the object into a dict
environment_log_response_list_dict = environment_log_response_list_instance.to_dict()
# create an instance of EnvironmentLogResponseList from a dict
environment_log_response_list_form_dict = environment_log_response_list.from_dict(environment_log_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


