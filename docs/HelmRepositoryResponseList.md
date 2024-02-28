# HelmRepositoryResponseList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[HelmRepositoryResponse]**](HelmRepositoryResponse.md) |  | [optional] 

## Example

```python
from qovery.models.helm_repository_response_list import HelmRepositoryResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of HelmRepositoryResponseList from a JSON string
helm_repository_response_list_instance = HelmRepositoryResponseList.from_json(json)
# print the JSON string representation of the object
print HelmRepositoryResponseList.to_json()

# convert the object into a dict
helm_repository_response_list_dict = helm_repository_response_list_instance.to_dict()
# create an instance of HelmRepositoryResponseList from a dict
helm_repository_response_list_form_dict = helm_repository_response_list.from_dict(helm_repository_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


