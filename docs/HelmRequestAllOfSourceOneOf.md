# HelmRequestAllOfSourceOneOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**git_repository** | [**HelmGitRepositoryRequest**](HelmGitRepositoryRequest.md) |  | [optional] 

## Example

```python
from qovery.models.helm_request_all_of_source_one_of import HelmRequestAllOfSourceOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of HelmRequestAllOfSourceOneOf from a JSON string
helm_request_all_of_source_one_of_instance = HelmRequestAllOfSourceOneOf.from_json(json)
# print the JSON string representation of the object
print HelmRequestAllOfSourceOneOf.to_json()

# convert the object into a dict
helm_request_all_of_source_one_of_dict = helm_request_all_of_source_one_of_instance.to_dict()
# create an instance of HelmRequestAllOfSourceOneOf from a dict
helm_request_all_of_source_one_of_form_dict = helm_request_all_of_source_one_of.from_dict(helm_request_all_of_source_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


