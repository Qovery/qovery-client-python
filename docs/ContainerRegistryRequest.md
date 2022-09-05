# ContainerRegistryRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**kind** | [**ContainerRegistryKindEnum**](ContainerRegistryKindEnum.md) |  | 
**url** | **str** | URL of the container registry: * For &#x60;DOCKER_HUB&#x60;: should be &#x60;https://docker.io&#x60; * For others: must start by &#x60;https://&#x60;  | 
**config** | **{str: (str,)}** | This field is dependent of the container registry kind: * &#x60;ECR&#x60; needs in the config: region, access_key_id, secret_access_key * &#x60;SCALEWAY_CR&#x60; needs in the config: region, scaleway_access_key, scaleway_secret_key * &#x60;DOCKER_HUB&#x60; needs in the config: username, password * &#x60;PUBLIC_ECR&#x60; needs in the config: access_key_id, secret_access_key * &#x60;DOCR&#x60; is not supported anymore  | 
**description** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


