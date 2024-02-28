# ProjectCurrentCost


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**consumed_time_in_seconds** | **int** |  | 
**cost** | [**Cost**](Cost.md) |  | 
**environments** | [**List[GenericObjectCurrentCost]**](GenericObjectCurrentCost.md) |  | [optional] 

## Example

```python
from qovery.models.project_current_cost import ProjectCurrentCost

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectCurrentCost from a JSON string
project_current_cost_instance = ProjectCurrentCost.from_json(json)
# print the JSON string representation of the object
print ProjectCurrentCost.to_json()

# convert the object into a dict
project_current_cost_dict = project_current_cost_instance.to_dict()
# create an instance of ProjectCurrentCost from a dict
project_current_cost_form_dict = project_current_cost.from_dict(project_current_cost_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


