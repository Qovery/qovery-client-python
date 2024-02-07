# HelmRequestAllOfSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**git_repository** | [**HelmGitRepositoryRequest**](HelmGitRepositoryRequest.md) |  | [optional] 
**helm_repository** | [**HelmRequestAllOfSourceOneOf1HelmRepository**](HelmRequestAllOfSourceOneOf1HelmRepository.md) |  | [optional] 

## Example

```python
from qovery.models.helm_request_all_of_source import HelmRequestAllOfSource

# TODO update the JSON string below
json = "{}"
# create an instance of HelmRequestAllOfSource from a JSON string
helm_request_all_of_source_instance = HelmRequestAllOfSource.from_json(json)
# print the JSON string representation of the object
print HelmRequestAllOfSource.to_json()

# convert the object into a dict
helm_request_all_of_source_dict = helm_request_all_of_source_instance.to_dict()
# create an instance of HelmRequestAllOfSource from a dict
helm_request_all_of_source_form_dict = helm_request_all_of_source.from_dict(helm_request_all_of_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


