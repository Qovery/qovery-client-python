# InvoiceResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Invoice]**](Invoice.md) |  | [optional] 

## Example

```python
from qovery.models.invoice_response_list import InvoiceResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceResponseList from a JSON string
invoice_response_list_instance = InvoiceResponseList.from_json(json)
# print the JSON string representation of the object
print InvoiceResponseList.to_json()

# convert the object into a dict
invoice_response_list_dict = invoice_response_list_instance.to_dict()
# create an instance of InvoiceResponseList from a dict
invoice_response_list_form_dict = invoice_response_list.from_dict(invoice_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


