# BudgetThreshold


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_in_cents** | **int** |  | [optional] 
**total** | **float** |  | [optional] 
**currency_code** | **str** |  | [optional] 

## Example

```python
from qovery.models.budget_threshold import BudgetThreshold

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetThreshold from a JSON string
budget_threshold_instance = BudgetThreshold.from_json(json)
# print the JSON string representation of the object
print BudgetThreshold.to_json()

# convert the object into a dict
budget_threshold_dict = budget_threshold_instance.to_dict()
# create an instance of BudgetThreshold from a dict
budget_threshold_form_dict = budget_threshold.from_dict(budget_threshold_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


