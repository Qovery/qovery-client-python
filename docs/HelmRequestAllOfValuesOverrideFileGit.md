# HelmRequestAllOfValuesOverrideFileGit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**git_repository** | [**ApplicationGitRepositoryRequest**](ApplicationGitRepositoryRequest.md) |  | 
**paths** | **List[str]** | List of path inside your git repository to locate values file. Must start by a / | 

## Example

```python
from qovery.models.helm_request_all_of_values_override_file_git import HelmRequestAllOfValuesOverrideFileGit

# TODO update the JSON string below
json = "{}"
# create an instance of HelmRequestAllOfValuesOverrideFileGit from a JSON string
helm_request_all_of_values_override_file_git_instance = HelmRequestAllOfValuesOverrideFileGit.from_json(json)
# print the JSON string representation of the object
print HelmRequestAllOfValuesOverrideFileGit.to_json()

# convert the object into a dict
helm_request_all_of_values_override_file_git_dict = helm_request_all_of_values_override_file_git_instance.to_dict()
# create an instance of HelmRequestAllOfValuesOverrideFileGit from a dict
helm_request_all_of_values_override_file_git_form_dict = helm_request_all_of_values_override_file_git.from_dict(helm_request_all_of_values_override_file_git_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


