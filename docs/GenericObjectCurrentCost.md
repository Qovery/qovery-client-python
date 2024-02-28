# GenericObjectCurrentCost


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**consumed_time_in_seconds** | **int** |  | 
**cost** | [**Cost**](Cost.md) |  | 

## Example

```python
from qovery.models.generic_object_current_cost import GenericObjectCurrentCost

# TODO update the JSON string below
json = "{}"
# create an instance of GenericObjectCurrentCost from a JSON string
generic_object_current_cost_instance = GenericObjectCurrentCost.from_json(json)
# print the JSON string representation of the object
print GenericObjectCurrentCost.to_json()

# convert the object into a dict
generic_object_current_cost_dict = generic_object_current_cost_instance.to_dict()
# create an instance of GenericObjectCurrentCost from a dict
generic_object_current_cost_form_dict = generic_object_current_cost.from_dict(generic_object_current_cost_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


