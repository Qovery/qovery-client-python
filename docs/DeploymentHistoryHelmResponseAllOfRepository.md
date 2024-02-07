# DeploymentHistoryHelmResponseAllOfRepository

If the chart source if from a repository, the chart name and its version

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chart_name** | **str** |  | [optional] 
**chart_version** | **str** |  | [optional] 

## Example

```python
from qovery.models.deployment_history_helm_response_all_of_repository import DeploymentHistoryHelmResponseAllOfRepository

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentHistoryHelmResponseAllOfRepository from a JSON string
deployment_history_helm_response_all_of_repository_instance = DeploymentHistoryHelmResponseAllOfRepository.from_json(json)
# print the JSON string representation of the object
print DeploymentHistoryHelmResponseAllOfRepository.to_json()

# convert the object into a dict
deployment_history_helm_response_all_of_repository_dict = deployment_history_helm_response_all_of_repository_instance.to_dict()
# create an instance of DeploymentHistoryHelmResponseAllOfRepository from a dict
deployment_history_helm_response_all_of_repository_form_dict = deployment_history_helm_response_all_of_repository.from_dict(deployment_history_helm_response_all_of_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


