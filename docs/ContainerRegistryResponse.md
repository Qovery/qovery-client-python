# ContainerRegistryResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**kind** | [**ContainerRegistryKindEnum**](ContainerRegistryKindEnum.md) |  | [optional] 
**description** | **str** |  | [optional] 
**url** | **str** | URL of the container registry | [optional] 
**cluster** | [**ContainerRegistryResponseAllOfCluster**](ContainerRegistryResponseAllOfCluster.md) |  | [optional] 

## Example

```python
from qovery.models.container_registry_response import ContainerRegistryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContainerRegistryResponse from a JSON string
container_registry_response_instance = ContainerRegistryResponse.from_json(json)
# print the JSON string representation of the object
print ContainerRegistryResponse.to_json()

# convert the object into a dict
container_registry_response_dict = container_registry_response_instance.to_dict()
# create an instance of ContainerRegistryResponse from a dict
container_registry_response_form_dict = container_registry_response.from_dict(container_registry_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


