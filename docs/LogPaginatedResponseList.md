# LogPaginatedResponseList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **float** |  | 
**page_size** | **float** |  | 
**results** | [**List[Log]**](Log.md) |  | [optional] 

## Example

```python
from qovery.models.log_paginated_response_list import LogPaginatedResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of LogPaginatedResponseList from a JSON string
log_paginated_response_list_instance = LogPaginatedResponseList.from_json(json)
# print the JSON string representation of the object
print LogPaginatedResponseList.to_json()

# convert the object into a dict
log_paginated_response_list_dict = log_paginated_response_list_instance.to_dict()
# create an instance of LogPaginatedResponseList from a dict
log_paginated_response_list_form_dict = log_paginated_response_list.from_dict(log_paginated_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


