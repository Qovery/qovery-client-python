# HelmRepositoryRequestConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | Required if the repository is private | [optional] 
**password** | **str** | Required if the repository is private | [optional] 
**access_key_id** | **str** | Required if kind is &#x60;ECR&#x60; or &#x60;PUBLIC_ECR&#x60; | [optional] 
**secret_access_key** | **str** | Required if kind is &#x60;ECR&#x60; or &#x60;PUBLIC_ECR&#x60; | [optional] 
**region** | **str** | Required if kind is &#x60;ECR&#x60; or &#x60;SCALEWAY_CR&#x60; | [optional] 
**scaleway_access_key** | **str** | Required if kind is &#x60;SCALEWAY_CR&#x60; | [optional] 
**scaleway_secret_key** | **str** | Required if kind is &#x60;SCALEWAY_CR&#x60; | [optional] 

## Example

```python
from qovery.models.helm_repository_request_config import HelmRepositoryRequestConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HelmRepositoryRequestConfig from a JSON string
helm_repository_request_config_instance = HelmRepositoryRequestConfig.from_json(json)
# print the JSON string representation of the object
print HelmRepositoryRequestConfig.to_json()

# convert the object into a dict
helm_repository_request_config_dict = helm_repository_request_config_instance.to_dict()
# create an instance of HelmRepositoryRequestConfig from a dict
helm_repository_request_config_form_dict = helm_repository_request_config.from_dict(helm_repository_request_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


