# AvailableHelmRepositoryResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[AvailableHelmRepositoryResponse]**](AvailableHelmRepositoryResponse.md) |  | [optional] 

## Example

```python
from qovery.models.available_helm_repository_response_list import AvailableHelmRepositoryResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableHelmRepositoryResponseList from a JSON string
available_helm_repository_response_list_instance = AvailableHelmRepositoryResponseList.from_json(json)
# print the JSON string representation of the object
print AvailableHelmRepositoryResponseList.to_json()

# convert the object into a dict
available_helm_repository_response_list_dict = available_helm_repository_response_list_instance.to_dict()
# create an instance of AvailableHelmRepositoryResponseList from a dict
available_helm_repository_response_list_form_dict = available_helm_repository_response_list.from_dict(available_helm_repository_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


