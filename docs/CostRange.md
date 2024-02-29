# CostRange


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_cost_in_cents** | **int** |  | [optional] 
**min_cost** | **float** |  | [optional] 
**max_cost_in_cents** | **int** |  | [optional] 
**max_cost** | **float** |  | [optional] 
**currency_code** | **str** |  | 

## Example

```python
from qovery.models.cost_range import CostRange

# TODO update the JSON string below
json = "{}"
# create an instance of CostRange from a JSON string
cost_range_instance = CostRange.from_json(json)
# print the JSON string representation of the object
print CostRange.to_json()

# convert the object into a dict
cost_range_dict = cost_range_instance.to_dict()
# create an instance of CostRange from a dict
cost_range_form_dict = cost_range.from_dict(cost_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


