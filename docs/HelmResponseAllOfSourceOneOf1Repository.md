# HelmResponseAllOfSourceOneOf1Repository


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chart_name** | **str** | The name of the chart in the repository | 
**chart_version** | **str** | The version of the chart to use | 
**repository** | [**HelmResponseAllOfSourceOneOf1RepositoryRepository**](HelmResponseAllOfSourceOneOf1RepositoryRepository.md) |  | 

## Example

```python
from qovery.models.helm_response_all_of_source_one_of1_repository import HelmResponseAllOfSourceOneOf1Repository

# TODO update the JSON string below
json = "{}"
# create an instance of HelmResponseAllOfSourceOneOf1Repository from a JSON string
helm_response_all_of_source_one_of1_repository_instance = HelmResponseAllOfSourceOneOf1Repository.from_json(json)
# print the JSON string representation of the object
print HelmResponseAllOfSourceOneOf1Repository.to_json()

# convert the object into a dict
helm_response_all_of_source_one_of1_repository_dict = helm_response_all_of_source_one_of1_repository_instance.to_dict()
# create an instance of HelmResponseAllOfSourceOneOf1Repository from a dict
helm_response_all_of_source_one_of1_repository_form_dict = helm_response_all_of_source_one_of1_repository.from_dict(helm_response_all_of_source_one_of1_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


