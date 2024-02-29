# HelmGitRepositoryRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | application git repository URL | 
**branch** | **str** | Name of the branch to use. This is optional If not specified, then the branch used is the &#x60;main&#x60; or &#x60;master&#x60; one  | [optional] 
**root_path** | **str** | indicates the root path of the application. | [optional] [default to '/']
**git_token_id** | **str** | The git token id on Qovery side | [optional] 

## Example

```python
from qovery.models.helm_git_repository_request import HelmGitRepositoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HelmGitRepositoryRequest from a JSON string
helm_git_repository_request_instance = HelmGitRepositoryRequest.from_json(json)
# print the JSON string representation of the object
print HelmGitRepositoryRequest.to_json()

# convert the object into a dict
helm_git_repository_request_dict = helm_git_repository_request_instance.to_dict()
# create an instance of HelmGitRepositoryRequest from a dict
helm_git_repository_request_form_dict = helm_git_repository_request.from_dict(helm_git_repository_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


