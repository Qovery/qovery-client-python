# CurrentCost


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan** | [**PlanEnum**](PlanEnum.md) |  | [optional] 
**remaining_trial_day** | **int** | number of days remaining before the end of the trial period | [optional] 
**renewal_at** | **datetime** | date when the current plan will be renewed | [optional] [readonly] 
**cost** | [**Cost**](Cost.md) |  | [optional] 

## Example

```python
from qovery.models.current_cost import CurrentCost

# TODO update the JSON string below
json = "{}"
# create an instance of CurrentCost from a JSON string
current_cost_instance = CurrentCost.from_json(json)
# print the JSON string representation of the object
print CurrentCost.to_json()

# convert the object into a dict
current_cost_dict = current_cost_instance.to_dict()
# create an instance of CurrentCost from a dict
current_cost_form_dict = current_cost.from_dict(current_cost_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


