# ContainerRegistryRequestConfig

This field is dependent of the container registry kind: * `ECR` needs in the config: region, access_key_id, secret_access_key * `SCALEWAY_CR` needs in the config: region, scaleway_access_key, scaleway_secret_key * `DOCKER_HUB` needs in the config (optional): username, password * `GITHUB_CR` needs in the config (optional): username, password * `GITLAB_CR` needs in the config (optional): username, password * `PUBLIC_ECR` doesn't need credentials info * `GENERIC_CR` needs in the config (optional): username, password * `DOCR` is not supported anymore 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key_id** | **str** | Required if kind is &#x60;ECR&#x60; or &#x60;PUBLIC_ECR&#x60; | [optional] 
**secret_access_key** | **str** | Required if kind is &#x60;ECR&#x60; or &#x60;PUBLIC_ECR&#x60; | [optional] 
**region** | **str** | Required if kind is &#x60;ECR&#x60; or &#x60;SCALEWAY_CR&#x60; | [optional] 
**scaleway_access_key** | **str** | Required if kind is &#x60;SCALEWAY_CR&#x60; | [optional] 
**scaleway_secret_key** | **str** | Required if kind is &#x60;SCALEWAY_CR&#x60; | [optional] 
**username** | **str** | optional, for kind &#x60;DOCKER_HUB&#x60;   We encourage you to set credentials for Docker Hub due to the limits on the pull rate  | [optional] 
**password** | **str** | optional, for kind &#x60;DOCKER_HUB&#x60;   We encourage you to set credentials for Docker Hub due to the limits on the pull rate  | [optional] 

## Example

```python
from qovery.models.container_registry_request_config import ContainerRegistryRequestConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ContainerRegistryRequestConfig from a JSON string
container_registry_request_config_instance = ContainerRegistryRequestConfig.from_json(json)
# print the JSON string representation of the object
print ContainerRegistryRequestConfig.to_json()

# convert the object into a dict
container_registry_request_config_dict = container_registry_request_config_instance.to_dict()
# create an instance of ContainerRegistryRequestConfig from a dict
container_registry_request_config_form_dict = container_registry_request_config.from_dict(container_registry_request_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


