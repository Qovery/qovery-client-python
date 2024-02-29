# OrganizationCurrentCost


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan** | [**PlanEnum**](PlanEnum.md) |  | [optional] 
**remaining_trial_day** | **int** | number of days remaining before the end of the trial period | [optional] 
**renewal_at** | **datetime** | date when the current plan will be renewed | [optional] [readonly] 
**cost** | [**Cost**](Cost.md) |  | [optional] 

## Example

```python
from qovery.models.organization_current_cost import OrganizationCurrentCost

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationCurrentCost from a JSON string
organization_current_cost_instance = OrganizationCurrentCost.from_json(json)
# print the JSON string representation of the object
print OrganizationCurrentCost.to_json()

# convert the object into a dict
organization_current_cost_dict = organization_current_cost_instance.to_dict()
# create an instance of OrganizationCurrentCost from a dict
organization_current_cost_form_dict = organization_current_cost.from_dict(organization_current_cost_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


