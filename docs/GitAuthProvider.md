# GitAuthProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**owner** | **str** |  | 
**use_bot** | **bool** |  | [optional] 

## Example

```python
from qovery.models.git_auth_provider import GitAuthProvider

# TODO update the JSON string below
json = "{}"
# create an instance of GitAuthProvider from a JSON string
git_auth_provider_instance = GitAuthProvider.from_json(json)
# print the JSON string representation of the object
print GitAuthProvider.to_json()

# convert the object into a dict
git_auth_provider_dict = git_auth_provider_instance.to_dict()
# create an instance of GitAuthProvider from a dict
git_auth_provider_form_dict = git_auth_provider.from_dict(git_auth_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


