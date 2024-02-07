# CreditCardRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** |  | 
**cvv** | **str** |  | 
**expiry_month** | **int** |  | 
**expiry_year** | **int** |  | 

## Example

```python
from qovery.models.credit_card_request import CreditCardRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreditCardRequest from a JSON string
credit_card_request_instance = CreditCardRequest.from_json(json)
# print the JSON string representation of the object
print CreditCardRequest.to_json()

# convert the object into a dict
credit_card_request_dict = credit_card_request_instance.to_dict()
# create an instance of CreditCardRequest from a dict
credit_card_request_form_dict = credit_card_request.from_dict(credit_card_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


