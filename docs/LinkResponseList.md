# LinkResponseList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from qovery.models.link_response_list import LinkResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of LinkResponseList from a JSON string
link_response_list_instance = LinkResponseList.from_json(json)
# print the JSON string representation of the object
print LinkResponseList.to_json()

# convert the object into a dict
link_response_list_dict = link_response_list_instance.to_dict()
# create an instance of LinkResponseList from a dict
link_response_list_form_dict = link_response_list.from_dict(link_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


