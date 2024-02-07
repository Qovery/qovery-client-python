# ProjectStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**service_total_number** | **float** |  | [optional] 
**environment_total_number** | **float** |  | [optional] 

## Example

```python
from qovery.models.project_stats import ProjectStats

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectStats from a JSON string
project_stats_instance = ProjectStats.from_json(json)
# print the JSON string representation of the object
print ProjectStats.to_json()

# convert the object into a dict
project_stats_dict = project_stats_instance.to_dict()
# create an instance of ProjectStats from a dict
project_stats_form_dict = project_stats.from_dict(project_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


