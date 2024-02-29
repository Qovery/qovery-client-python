# EnvironmentStatsResponseList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[EnvironmentStats]**](EnvironmentStats.md) |  | [optional] 

## Example

```python
from qovery.models.environment_stats_response_list import EnvironmentStatsResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentStatsResponseList from a JSON string
environment_stats_response_list_instance = EnvironmentStatsResponseList.from_json(json)
# print the JSON string representation of the object
print EnvironmentStatsResponseList.to_json()

# convert the object into a dict
environment_stats_response_list_dict = environment_stats_response_list_instance.to_dict()
# create an instance of EnvironmentStatsResponseList from a dict
environment_stats_response_list_form_dict = environment_stats_response_list.from_dict(environment_stats_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


