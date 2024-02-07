# HelmResponseAllOfValuesOverrideFileGit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**git_repository** | [**ApplicationGitRepository**](ApplicationGitRepository.md) |  | 
**paths** | **List[str]** | List of path inside your git repository to locate values file. Must start by a / | 

## Example

```python
from qovery.models.helm_response_all_of_values_override_file_git import HelmResponseAllOfValuesOverrideFileGit

# TODO update the JSON string below
json = "{}"
# create an instance of HelmResponseAllOfValuesOverrideFileGit from a JSON string
helm_response_all_of_values_override_file_git_instance = HelmResponseAllOfValuesOverrideFileGit.from_json(json)
# print the JSON string representation of the object
print HelmResponseAllOfValuesOverrideFileGit.to_json()

# convert the object into a dict
helm_response_all_of_values_override_file_git_dict = helm_response_all_of_values_override_file_git_instance.to_dict()
# create an instance of HelmResponseAllOfValuesOverrideFileGit from a dict
helm_response_all_of_values_override_file_git_form_dict = helm_response_all_of_values_override_file_git.from_dict(helm_response_all_of_values_override_file_git_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


