# JobRequestAllOfSourceDocker


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dockerfile_path** | **str** | The path of the associated Dockerfile. Only if you are using build_mode &#x3D; DOCKER | [optional] 
**git_repository** | [**ApplicationGitRepositoryRequest**](ApplicationGitRepositoryRequest.md) |  | [optional] 

## Example

```python
from qovery.models.job_request_all_of_source_docker import JobRequestAllOfSourceDocker

# TODO update the JSON string below
json = "{}"
# create an instance of JobRequestAllOfSourceDocker from a JSON string
job_request_all_of_source_docker_instance = JobRequestAllOfSourceDocker.from_json(json)
# print the JSON string representation of the object
print JobRequestAllOfSourceDocker.to_json()

# convert the object into a dict
job_request_all_of_source_docker_dict = job_request_all_of_source_docker_instance.to_dict()
# create an instance of JobRequestAllOfSourceDocker from a dict
job_request_all_of_source_docker_form_dict = job_request_all_of_source_docker.from_dict(job_request_all_of_source_docker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


