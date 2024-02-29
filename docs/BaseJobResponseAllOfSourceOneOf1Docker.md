# BaseJobResponseAllOfSourceOneOf1Docker


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dockerfile_path** | **str** | The path of the associated Dockerfile. Only if you are using build_mode &#x3D; DOCKER | [optional] 
**git_repository** | [**ApplicationGitRepository**](ApplicationGitRepository.md) |  | [optional] 

## Example

```python
from qovery.models.base_job_response_all_of_source_one_of1_docker import BaseJobResponseAllOfSourceOneOf1Docker

# TODO update the JSON string below
json = "{}"
# create an instance of BaseJobResponseAllOfSourceOneOf1Docker from a JSON string
base_job_response_all_of_source_one_of1_docker_instance = BaseJobResponseAllOfSourceOneOf1Docker.from_json(json)
# print the JSON string representation of the object
print BaseJobResponseAllOfSourceOneOf1Docker.to_json()

# convert the object into a dict
base_job_response_all_of_source_one_of1_docker_dict = base_job_response_all_of_source_one_of1_docker_instance.to_dict()
# create an instance of BaseJobResponseAllOfSourceOneOf1Docker from a dict
base_job_response_all_of_source_one_of1_docker_form_dict = base_job_response_all_of_source_one_of1_docker.from_dict(base_job_response_all_of_source_one_of1_docker_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


