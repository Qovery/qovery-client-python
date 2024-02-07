# DeployAllRequestJobsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id of the job to be updated. | [optional] 
**image_tag** | **str** | new tag for the job image. Use only if job is an image source. Can be empty only if the service has been already deployed (in this case the service version won&#39;t be changed) | [optional] 
**git_commit_id** | **str** | Commit ID to deploy. Use only if job is a repository source. Can be empty only if the service has been already deployed (in this case the service version won&#39;t be changed) | [optional] 

## Example

```python
from qovery.models.deploy_all_request_jobs_inner import DeployAllRequestJobsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DeployAllRequestJobsInner from a JSON string
deploy_all_request_jobs_inner_instance = DeployAllRequestJobsInner.from_json(json)
# print the JSON string representation of the object
print DeployAllRequestJobsInner.to_json()

# convert the object into a dict
deploy_all_request_jobs_inner_dict = deploy_all_request_jobs_inner_instance.to_dict()
# create an instance of DeployAllRequestJobsInner from a dict
deploy_all_request_jobs_inner_form_dict = deploy_all_request_jobs_inner.from_dict(deploy_all_request_jobs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


