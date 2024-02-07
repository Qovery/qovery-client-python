# HelmRequestAllOfSourceOneOf1HelmRepository


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository** | **str** | The id of the helm repository | [optional] 
**chart_name** | **str** | The name of the chart in the repository | [optional] 
**chart_version** | **str** | The version of the chart to use | [optional] 

## Example

```python
from qovery.models.helm_request_all_of_source_one_of1_helm_repository import HelmRequestAllOfSourceOneOf1HelmRepository

# TODO update the JSON string below
json = "{}"
# create an instance of HelmRequestAllOfSourceOneOf1HelmRepository from a JSON string
helm_request_all_of_source_one_of1_helm_repository_instance = HelmRequestAllOfSourceOneOf1HelmRepository.from_json(json)
# print the JSON string representation of the object
print HelmRequestAllOfSourceOneOf1HelmRepository.to_json()

# convert the object into a dict
helm_request_all_of_source_one_of1_helm_repository_dict = helm_request_all_of_source_one_of1_helm_repository_instance.to_dict()
# create an instance of HelmRequestAllOfSourceOneOf1HelmRepository from a dict
helm_request_all_of_source_one_of1_helm_repository_form_dict = helm_request_all_of_source_one_of1_helm_repository.from_dict(helm_request_all_of_source_one_of1_helm_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


