# JobDeployRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_tag** | **str** | Image tag to deploy.   Cannot be set if &#x60;git_commit_id&#x60; is defined  | [optional] 
**git_commit_id** | **str** | Commit to deploy Cannot be set if &#x60;image_tag&#x60; is defined  | [optional] 

## Example

```python
from qovery.models.job_deploy_request import JobDeployRequest

# TODO update the JSON string below
json = "{}"
# create an instance of JobDeployRequest from a JSON string
job_deploy_request_instance = JobDeployRequest.from_json(json)
# print the JSON string representation of the object
print JobDeployRequest.to_json()

# convert the object into a dict
job_deploy_request_dict = job_deploy_request_instance.to_dict()
# create an instance of JobDeployRequest from a dict
job_deploy_request_form_dict = job_deploy_request.from_dict(job_deploy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


