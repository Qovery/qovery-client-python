# BaseJobResponseAllOfSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | [**ContainerSource**](ContainerSource.md) |  | [optional] 
**docker** | [**BaseJobResponseAllOfSourceOneOf1Docker**](BaseJobResponseAllOfSourceOneOf1Docker.md) |  | [optional] 

## Example

```python
from qovery.models.base_job_response_all_of_source import BaseJobResponseAllOfSource

# TODO update the JSON string below
json = "{}"
# create an instance of BaseJobResponseAllOfSource from a JSON string
base_job_response_all_of_source_instance = BaseJobResponseAllOfSource.from_json(json)
# print the JSON string representation of the object
print BaseJobResponseAllOfSource.to_json()

# convert the object into a dict
base_job_response_all_of_source_dict = base_job_response_all_of_source_instance.to_dict()
# create an instance of BaseJobResponseAllOfSource from a dict
base_job_response_all_of_source_form_dict = base_job_response_all_of_source.from_dict(base_job_response_all_of_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


