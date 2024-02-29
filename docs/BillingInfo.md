# BillingInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**email** | **str** | email used for billing, and to receive all invoices by email | [optional] 
**address** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**zip** | **str** |  | [optional] 
**state** | **str** | only for US | [optional] 
**country_code** | **str** | ISO code of the country | [optional] 
**company** | **str** | name of the company to bill | [optional] 
**vat_number** | **str** |  | [optional] 

## Example

```python
from qovery.models.billing_info import BillingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of BillingInfo from a JSON string
billing_info_instance = BillingInfo.from_json(json)
# print the JSON string representation of the object
print BillingInfo.to_json()

# convert the object into a dict
billing_info_dict = billing_info_instance.to_dict()
# create an instance of BillingInfo from a dict
billing_info_form_dict = billing_info.from_dict(billing_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


