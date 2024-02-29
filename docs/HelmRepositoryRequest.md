# HelmRepositoryRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**kind** | [**HelmRepositoryKindEnum**](HelmRepositoryKindEnum.md) |  | 
**description** | **str** |  | [optional] 
**url** | **str** | URL of the helm chart repository: * For &#x60;OCI&#x60;: it must start by oci:// * For &#x60;HTTPS&#x60;: it must be start by https://  | [optional] 
**skip_tls_verification** | **bool** | Bypass tls certificate verification when connecting to repository | 
**config** | [**HelmRepositoryRequestConfig**](HelmRepositoryRequestConfig.md) |  | 

## Example

```python
from qovery.models.helm_repository_request import HelmRepositoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HelmRepositoryRequest from a JSON string
helm_repository_request_instance = HelmRepositoryRequest.from_json(json)
# print the JSON string representation of the object
print HelmRepositoryRequest.to_json()

# convert the object into a dict
helm_repository_request_dict = helm_repository_request_instance.to_dict()
# create an instance of HelmRepositoryRequest from a dict
helm_repository_request_form_dict = helm_repository_request.from_dict(helm_repository_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


