# HelmRepositoryRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**kind** | [**HelmRepositoryKindEnum**](HelmRepositoryKindEnum.md) |  | 
**skip_tls_verification** | **bool** | Bypass tls certificate verification when connecting to repository | 
**config** | [**HelmRepositoryRequestConfig**](HelmRepositoryRequestConfig.md) |  | 
**description** | **str** |  | [optional] 
**url** | **str** | URL of the helm chart repository: * For &#x60;OCI&#x60;: it must start by oci:// * For &#x60;HTTPS&#x60;: it must be start by https://  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


