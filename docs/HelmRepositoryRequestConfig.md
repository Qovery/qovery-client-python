# HelmRepositoryRequestConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skip_tls_verification** | **bool** | Bypass tls certificate verification when connecting to repository | [optional]  if omitted the server will use the default value of False
**username** | **str** | Required if the repository is private | [optional] 
**password** | **str** | Required if the repository is private | [optional] 
**access_key_id** | **str** | Required if kind is &#x60;ECR&#x60; or &#x60;PUBLIC_ECR&#x60; | [optional] 
**secret_access_key** | **str** | Required if kind is &#x60;ECR&#x60; or &#x60;PUBLIC_ECR&#x60; | [optional] 
**region** | **str** | Required if kind is &#x60;ECR&#x60; or &#x60;SCALEWAY_CR&#x60; | [optional] 
**scaleway_access_key** | **str** | Required if kind is &#x60;SCALEWAY_CR&#x60; | [optional] 
**scaleway_secret_key** | **str** | Required if kind is &#x60;SCALEWAY_CR&#x60; | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


