# DeployAllRequestHelmsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id of the helm to be updated. | [optional] 
**chart_version** | **str** | The new chart version for the Helm source. Use this only if the helm has a Helm repository source. | [optional] 
**git_commit_id** | **str** | The commit Id to deploy. Use this only if the helm has a Git repository source. | [optional] 
**values_override_git_commit_id** | **str** | The commit Id of the override values to deploy. Use only if the helm has a Git override values repository. | [optional] 

## Example

```python
from qovery.models.deploy_all_request_helms_inner import DeployAllRequestHelmsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DeployAllRequestHelmsInner from a JSON string
deploy_all_request_helms_inner_instance = DeployAllRequestHelmsInner.from_json(json)
# print the JSON string representation of the object
print DeployAllRequestHelmsInner.to_json()

# convert the object into a dict
deploy_all_request_helms_inner_dict = deploy_all_request_helms_inner_instance.to_dict()
# create an instance of DeployAllRequestHelmsInner from a dict
deploy_all_request_helms_inner_form_dict = deploy_all_request_helms_inner.from_dict(deploy_all_request_helms_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


