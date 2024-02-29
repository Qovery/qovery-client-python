# AvailableHelmRepositoryResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | [**HelmRepositoryKindEnum**](HelmRepositoryKindEnum.md) |  | 
**required_config** | **Dict[str, object]** |  | 
**is_mandatory** | **bool** |  | 

## Example

```python
from qovery.models.available_helm_repository_response import AvailableHelmRepositoryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableHelmRepositoryResponse from a JSON string
available_helm_repository_response_instance = AvailableHelmRepositoryResponse.from_json(json)
# print the JSON string representation of the object
print AvailableHelmRepositoryResponse.to_json()

# convert the object into a dict
available_helm_repository_response_dict = available_helm_repository_response_instance.to_dict()
# create an instance of AvailableHelmRepositoryResponse from a dict
available_helm_repository_response_form_dict = available_helm_repository_response.from_dict(available_helm_repository_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


