# ContainerRegistryProviderDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**url** | **str** | URL of the container registry | 
**kind** | [**ContainerRegistryKindEnum**](ContainerRegistryKindEnum.md) |  | 

## Example

```python
from qovery.models.container_registry_provider_details_response import ContainerRegistryProviderDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContainerRegistryProviderDetailsResponse from a JSON string
container_registry_provider_details_response_instance = ContainerRegistryProviderDetailsResponse.from_json(json)
# print the JSON string representation of the object
print ContainerRegistryProviderDetailsResponse.to_json()

# convert the object into a dict
container_registry_provider_details_response_dict = container_registry_provider_details_response_instance.to_dict()
# create an instance of ContainerRegistryProviderDetailsResponse from a dict
container_registry_provider_details_response_form_dict = container_registry_provider_details_response.from_dict(container_registry_provider_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


