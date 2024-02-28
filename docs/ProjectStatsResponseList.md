# ProjectStatsResponseList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ProjectStats]**](ProjectStats.md) |  | [optional] 

## Example

```python
from qovery.models.project_stats_response_list import ProjectStatsResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectStatsResponseList from a JSON string
project_stats_response_list_instance = ProjectStatsResponseList.from_json(json)
# print the JSON string representation of the object
print ProjectStatsResponseList.to_json()

# convert the object into a dict
project_stats_response_list_dict = project_stats_response_list_instance.to_dict()
# create an instance of ProjectStatsResponseList from a dict
project_stats_response_list_form_dict = project_stats_response_list.from_dict(project_stats_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


