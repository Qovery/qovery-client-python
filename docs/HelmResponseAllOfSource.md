# HelmResponseAllOfSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**git** | [**HelmResponseAllOfSourceOneOfGit**](HelmResponseAllOfSourceOneOfGit.md) |  | [optional] 
**repository** | [**HelmResponseAllOfSourceOneOf1Repository**](HelmResponseAllOfSourceOneOf1Repository.md) |  | [optional] 

## Example

```python
from qovery.models.helm_response_all_of_source import HelmResponseAllOfSource

# TODO update the JSON string below
json = "{}"
# create an instance of HelmResponseAllOfSource from a JSON string
helm_response_all_of_source_instance = HelmResponseAllOfSource.from_json(json)
# print the JSON string representation of the object
print HelmResponseAllOfSource.to_json()

# convert the object into a dict
helm_response_all_of_source_dict = helm_response_all_of_source_instance.to_dict()
# create an instance of HelmResponseAllOfSource from a dict
helm_response_all_of_source_form_dict = helm_response_all_of_source.from_dict(helm_response_all_of_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


