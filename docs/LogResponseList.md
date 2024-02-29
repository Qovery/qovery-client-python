# LogResponseList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Log]**](Log.md) |  | [optional] 

## Example

```python
from qovery.models.log_response_list import LogResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of LogResponseList from a JSON string
log_response_list_instance = LogResponseList.from_json(json)
# print the JSON string representation of the object
print LogResponseList.to_json()

# convert the object into a dict
log_response_list_dict = log_response_list_instance.to_dict()
# create an instance of LogResponseList from a dict
log_response_list_form_dict = log_response_list.from_dict(log_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


