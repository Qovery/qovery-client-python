# ContainerRegistryRequestConfig

This field is dependent of the container registry kind: * `ECR` needs in the config: region, access_key_id, secret_access_key * `SCALEWAY_CR` needs in the config: region, scaleway_access_key, scaleway_secret_key * `DOCKER_HUB` needs in the config: username, password * `PUBLIC_ECR` needs in the config: access_key_id, secret_access_key * `DOCR` is not supported anymore 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key_id** | **str** | Required if kind is &#x60;ECR&#x60; or &#x60;PUBLIC_ECR&#x60; | [optional] 
**secret_access_key** | **str** | Required if kind is &#x60;ECR&#x60; or &#x60;PUBLIC_ECR&#x60; | [optional] 
**region** | **str** | Required if kind is &#x60;ECR&#x60; or &#x60;SCALEWAY_CR&#x60; | [optional] 
**scaleway_access_key** | **str** | Required if kind is &#x60;SCALEWAY_CR&#x60; | [optional] 
**scaleway_secret_key** | **str** | Required if kind is &#x60;SCALEWAY_CR&#x60; | [optional] 
**username** | **str** | Required if kind is &#x60;DOCKER_HUB&#x60; | [optional] 
**password** | **str** | Required if kind is &#x60;DOCKER_HUB&#x60; | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


