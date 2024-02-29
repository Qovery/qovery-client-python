# HelmRepositoryResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**name** | **str** |  | 
**kind** | [**HelmRepositoryKindEnum**](HelmRepositoryKindEnum.md) |  | [optional] 
**description** | **str** |  | [optional] 
**url** | **str** | URL of the helm repository | [optional] 
**skip_tls_verification** | **bool** | Bypass tls certificate verification when connecting to repository | [optional] 

## Example

```python
from qovery.models.helm_repository_response import HelmRepositoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HelmRepositoryResponse from a JSON string
helm_repository_response_instance = HelmRepositoryResponse.from_json(json)
# print the JSON string representation of the object
print HelmRepositoryResponse.to_json()

# convert the object into a dict
helm_repository_response_dict = helm_repository_response_instance.to_dict()
# create an instance of HelmRepositoryResponse from a dict
helm_repository_response_form_dict = helm_repository_response.from_dict(helm_repository_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


