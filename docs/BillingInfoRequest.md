# BillingInfoRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**email** | **str** | email used for billing, and to receive all invoices by email | 
**address** | **str** |  | 
**city** | **str** |  | 
**zip** | **str** |  | 
**state** | **str** | only for US | [optional] 
**country_code** | **str** | ISO code of the country | 
**company** | **str** | name of the company to bill | [optional] 
**vat_number** | **str** |  | [optional] 

## Example

```python
from qovery.models.billing_info_request import BillingInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BillingInfoRequest from a JSON string
billing_info_request_instance = BillingInfoRequest.from_json(json)
# print the JSON string representation of the object
print BillingInfoRequest.to_json()

# convert the object into a dict
billing_info_request_dict = billing_info_request_instance.to_dict()
# create an instance of BillingInfoRequest from a dict
billing_info_request_form_dict = billing_info_request.from_dict(billing_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


