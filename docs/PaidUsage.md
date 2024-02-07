# PaidUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_deployments_per_month** | **int** |  | [optional] 
**consumed_deployments** | **int** |  | [optional] 
**monthly_plan_cost** | **float** |  | [optional] 
**monthly_plan_cost_in_cents** | **int** |  | [optional] 
**remaining_deployments** | **int** |  | [optional] 
**deployments_exceeded** | **bool** |  | [optional] 
**renewal_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from qovery.models.paid_usage import PaidUsage

# TODO update the JSON string below
json = "{}"
# create an instance of PaidUsage from a JSON string
paid_usage_instance = PaidUsage.from_json(json)
# print the JSON string representation of the object
print PaidUsage.to_json()

# convert the object into a dict
paid_usage_dict = paid_usage_instance.to_dict()
# create an instance of PaidUsage from a dict
paid_usage_form_dict = paid_usage.from_dict(paid_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


