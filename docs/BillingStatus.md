# BillingStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_valid** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from qovery.models.billing_status import BillingStatus

# TODO update the JSON string below
json = "{}"
# create an instance of BillingStatus from a JSON string
billing_status_instance = BillingStatus.from_json(json)
# print the JSON string representation of the object
print BillingStatus.to_json()

# convert the object into a dict
billing_status_dict = billing_status_instance.to_dict()
# create an instance of BillingStatus from a dict
billing_status_form_dict = billing_status.from_dict(billing_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


