# GitRepositoryBranchResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[GitRepositoryBranch]**](GitRepositoryBranch.md) |  | [optional] 

## Example

```python
from qovery.models.git_repository_branch_response_list import GitRepositoryBranchResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of GitRepositoryBranchResponseList from a JSON string
git_repository_branch_response_list_instance = GitRepositoryBranchResponseList.from_json(json)
# print the JSON string representation of the object
print GitRepositoryBranchResponseList.to_json()

# convert the object into a dict
git_repository_branch_response_list_dict = git_repository_branch_response_list_instance.to_dict()
# create an instance of GitRepositoryBranchResponseList from a dict
git_repository_branch_response_list_form_dict = git_repository_branch_response_list.from_dict(git_repository_branch_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


