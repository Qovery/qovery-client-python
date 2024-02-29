# ContainerRegistryResponseList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ContainerRegistryResponse]**](ContainerRegistryResponse.md) |  | [optional] 

## Example

```python
from qovery.models.container_registry_response_list import ContainerRegistryResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of ContainerRegistryResponseList from a JSON string
container_registry_response_list_instance = ContainerRegistryResponseList.from_json(json)
# print the JSON string representation of the object
print ContainerRegistryResponseList.to_json()

# convert the object into a dict
container_registry_response_list_dict = container_registry_response_list_instance.to_dict()
# create an instance of ContainerRegistryResponseList from a dict
container_registry_response_list_form_dict = container_registry_response_list.from_dict(container_registry_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


