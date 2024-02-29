# CreditCardResponseList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[CreditCard]**](CreditCard.md) |  | [optional] 

## Example

```python
from qovery.models.credit_card_response_list import CreditCardResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of CreditCardResponseList from a JSON string
credit_card_response_list_instance = CreditCardResponseList.from_json(json)
# print the JSON string representation of the object
print CreditCardResponseList.to_json()

# convert the object into a dict
credit_card_response_list_dict = credit_card_response_list_instance.to_dict()
# create an instance of CreditCardResponseList from a dict
credit_card_response_list_form_dict = credit_card_response_list.from_dict(credit_card_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


