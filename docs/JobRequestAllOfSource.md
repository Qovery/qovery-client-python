# JobRequestAllOfSource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | [**JobRequestAllOfSourceImage**](JobRequestAllOfSourceImage.md) |  | [optional] 
**docker** | [**JobRequestAllOfSourceDocker**](JobRequestAllOfSourceDocker.md) |  | [optional] 

## Example

```python
from qovery.models.job_request_all_of_source import JobRequestAllOfSource

# TODO update the JSON string below
json = "{}"
# create an instance of JobRequestAllOfSource from a JSON string
job_request_all_of_source_instance = JobRequestAllOfSource.from_json(json)
# print the JSON string representation of the object
print JobRequestAllOfSource.to_json()

# convert the object into a dict
job_request_all_of_source_dict = job_request_all_of_source_instance.to_dict()
# create an instance of JobRequestAllOfSource from a dict
job_request_all_of_source_form_dict = job_request_all_of_source.from_dict(job_request_all_of_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


