# ApplicationGitRepository


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_access** | **bool** |  | [optional] 
**provider** | [**GitProviderEnum**](GitProviderEnum.md) |  | 
**owner** | **str** |  | 
**url** | **str** |  | 
**name** | **str** | repository name | 
**branch** | **str** |  | [optional] 
**root_path** | **str** |  | [optional] 
**deployed_commit_id** | **str** | Git commit ID corresponding to the deployed version of the app | [optional] 
**deployed_commit_date** | **datetime** | Git commit date corresponding to the deployed version of the app | [optional] [readonly] 
**deployed_commit_contributor** | **str** | Git commit user corresponding to the deployed version of the app | [optional] 
**deployed_commit_tag** | **str** |  | [optional] 
**git_token_id** | **str** |  | [optional] 
**git_token_name** | **str** |  | [optional] 

## Example

```python
from qovery.models.application_git_repository import ApplicationGitRepository

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationGitRepository from a JSON string
application_git_repository_instance = ApplicationGitRepository.from_json(json)
# print the JSON string representation of the object
print ApplicationGitRepository.to_json()

# convert the object into a dict
application_git_repository_dict = application_git_repository_instance.to_dict()
# create an instance of ApplicationGitRepository from a dict
application_git_repository_form_dict = application_git_repository.from_dict(application_git_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


