# DeployAllRequestApplicationsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_id** | **str** | id of the application to be deployed. | 
**git_commit_id** | **str** | Commit ID to deploy. Can be empty only if the service has been already deployed (in this case the service version won&#39;t be changed) | [optional] 

## Example

```python
from qovery.models.deploy_all_request_applications_inner import DeployAllRequestApplicationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DeployAllRequestApplicationsInner from a JSON string
deploy_all_request_applications_inner_instance = DeployAllRequestApplicationsInner.from_json(json)
# print the JSON string representation of the object
print DeployAllRequestApplicationsInner.to_json()

# convert the object into a dict
deploy_all_request_applications_inner_dict = deploy_all_request_applications_inner_instance.to_dict()
# create an instance of DeployAllRequestApplicationsInner from a dict
deploy_all_request_applications_inner_form_dict = deploy_all_request_applications_inner.from_dict(deploy_all_request_applications_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


