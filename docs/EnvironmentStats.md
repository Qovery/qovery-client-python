# EnvironmentStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**service_total_number** | **float** |  | [optional] 

## Example

```python
from qovery.models.environment_stats import EnvironmentStats

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentStats from a JSON string
environment_stats_instance = EnvironmentStats.from_json(json)
# print the JSON string representation of the object
print EnvironmentStats.to_json()

# convert the object into a dict
environment_stats_dict = environment_stats_instance.to_dict()
# create an instance of EnvironmentStats from a dict
environment_stats_form_dict = environment_stats.from_dict(environment_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


