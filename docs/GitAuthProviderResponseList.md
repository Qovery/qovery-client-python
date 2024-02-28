# GitAuthProviderResponseList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[GitAuthProvider]**](GitAuthProvider.md) |  | [optional] 

## Example

```python
from qovery.models.git_auth_provider_response_list import GitAuthProviderResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of GitAuthProviderResponseList from a JSON string
git_auth_provider_response_list_instance = GitAuthProviderResponseList.from_json(json)
# print the JSON string representation of the object
print GitAuthProviderResponseList.to_json()

# convert the object into a dict
git_auth_provider_response_list_dict = git_auth_provider_response_list_instance.to_dict()
# create an instance of GitAuthProviderResponseList from a dict
git_auth_provider_response_list_form_dict = git_auth_provider_response_list.from_dict(git_auth_provider_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


