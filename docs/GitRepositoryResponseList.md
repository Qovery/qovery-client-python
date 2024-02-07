# GitRepositoryResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[GitRepository]**](GitRepository.md) |  | [optional] 

## Example

```python
from qovery.models.git_repository_response_list import GitRepositoryResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of GitRepositoryResponseList from a JSON string
git_repository_response_list_instance = GitRepositoryResponseList.from_json(json)
# print the JSON string representation of the object
print GitRepositoryResponseList.to_json()

# convert the object into a dict
git_repository_response_list_dict = git_repository_response_list_instance.to_dict()
# create an instance of GitRepositoryResponseList from a dict
git_repository_response_list_form_dict = git_repository_response_list.from_dict(git_repository_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


