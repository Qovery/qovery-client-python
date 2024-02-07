# HelmDeployRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chart_version** | **str** | version of the chart to deploy. Cannot be set if &#x60;git_commit_id&#x60; is defined  | [optional] 
**git_commit_id** | **str** | Commit to deploy for chart source. Cannot be set if &#x60;version&#x60; is defined  | [optional] 
**values_override_git_commit_id** | **str** | Commit to deploy for values override  | [optional] 

## Example

```python
from qovery.models.helm_deploy_request import HelmDeployRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HelmDeployRequest from a JSON string
helm_deploy_request_instance = HelmDeployRequest.from_json(json)
# print the JSON string representation of the object
print HelmDeployRequest.to_json()

# convert the object into a dict
helm_deploy_request_dict = helm_deploy_request_instance.to_dict()
# create an instance of HelmDeployRequest from a dict
helm_deploy_request_form_dict = helm_deploy_request.from_dict(helm_deploy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


