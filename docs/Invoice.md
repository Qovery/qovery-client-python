# Invoice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_in_cents** | **int** |  | 
**total** | **float** |  | 
**currency_code** | **str** |  | 
**id** | **str** |  | 
**created_at** | **datetime** |  | 
**status** | [**InvoiceStatusEnum**](InvoiceStatusEnum.md) |  | 

## Example

```python
from qovery.models.invoice import Invoice

# TODO update the JSON string below
json = "{}"
# create an instance of Invoice from a JSON string
invoice_instance = Invoice.from_json(json)
# print the JSON string representation of the object
print Invoice.to_json()

# convert the object into a dict
invoice_dict = invoice_instance.to_dict()
# create an instance of Invoice from a dict
invoice_form_dict = invoice.from_dict(invoice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


