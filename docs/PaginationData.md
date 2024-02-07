# PaginationData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **float** |  | 
**page_size** | **float** |  | 

## Example

```python
from qovery.models.pagination_data import PaginationData

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationData from a JSON string
pagination_data_instance = PaginationData.from_json(json)
# print the JSON string representation of the object
print PaginationData.to_json()

# convert the object into a dict
pagination_data_dict = pagination_data_instance.to_dict()
# create an instance of PaginationData from a dict
pagination_data_form_dict = pagination_data.from_dict(pagination_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


