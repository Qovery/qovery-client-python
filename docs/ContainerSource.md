# ContainerSource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_name** | **str** | The image name pattern differs according to chosen container registry provider: * &#x60;ECR&#x60;: &#x60;repository&#x60; * &#x60;SCALEWAY_CR&#x60;: &#x60;namespace/image&#x60; * &#x60;DOCKER_HUB&#x60;: &#x60;image&#x60; or &#x60;repository/image&#x60; * &#x60;PUBLIC_ECR&#x60;: &#x60;registry_alias/repository&#x60;  | 
**tag** | **str** | tag of the image container | 
**registry_id** | **str** | tag of the image container | [optional] 
**registry** | [**ContainerRegistryProviderDetailsResponse**](ContainerRegistryProviderDetailsResponse.md) |  | 

## Example

```python
from qovery.models.container_source import ContainerSource

# TODO update the JSON string below
json = "{}"
# create an instance of ContainerSource from a JSON string
container_source_instance = ContainerSource.from_json(json)
# print the JSON string representation of the object
print ContainerSource.to_json()

# convert the object into a dict
container_source_dict = container_source_instance.to_dict()
# create an instance of ContainerSource from a dict
container_source_form_dict = container_source.from_dict(container_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


