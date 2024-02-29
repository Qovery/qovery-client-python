# ContainerRegistryRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**kind** | [**ContainerRegistryKindEnum**](ContainerRegistryKindEnum.md) |  | 
**description** | **str** |  | [optional] 
**url** | **str** | URL of the container registry: * For &#x60;DOCKER_HUB&#x60;: it must be &#x60;https://docker.io&#x60; (default with &#39;https://docker.io&#39; if no url provided for &#x60;DOCKER_HUB&#x60;) * For &#x60;GITHUB_CR&#x60;: it must be &#x60;https://ghcr.io&#x60; (default with &#39;https://ghcr.io&#39; if no url provided for &#x60;GITHUB_CR&#x60;) * For &#x60;GITLAB_CR&#x60;: it must be &#x60;https://registry.gitlab.com&#x60; (default with &#39;https://registry.gitlab.com&#39; if no url provided for &#x60;GITLAB_CR&#x60;) * For others: it&#39;s required and must start by &#x60;https://&#x60;  | [optional] 
**config** | [**ContainerRegistryRequestConfig**](ContainerRegistryRequestConfig.md) |  | 

## Example

```python
from qovery.models.container_registry_request import ContainerRegistryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContainerRegistryRequest from a JSON string
container_registry_request_instance = ContainerRegistryRequest.from_json(json)
# print the JSON string representation of the object
print ContainerRegistryRequest.to_json()

# convert the object into a dict
container_registry_request_dict = container_registry_request_instance.to_dict()
# create an instance of ContainerRegistryRequest from a dict
container_registry_request_form_dict = container_registry_request.from_dict(container_registry_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


