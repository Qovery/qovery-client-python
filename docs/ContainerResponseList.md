# ContainerResponseList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ContainerResponse]**](ContainerResponse.md) |  | [optional] 

## Example

```python
from qovery.models.container_response_list import ContainerResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of ContainerResponseList from a JSON string
container_response_list_instance = ContainerResponseList.from_json(json)
# print the JSON string representation of the object
print ContainerResponseList.to_json()

# convert the object into a dict
container_response_list_dict = container_response_list_instance.to_dict()
# create an instance of ContainerResponseList from a dict
container_response_list_form_dict = container_response_list.from_dict(container_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


