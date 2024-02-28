# JobResponseList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[JobResponse]**](JobResponse.md) |  | [optional] 

## Example

```python
from qovery.models.job_response_list import JobResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of JobResponseList from a JSON string
job_response_list_instance = JobResponseList.from_json(json)
# print the JSON string representation of the object
print JobResponseList.to_json()

# convert the object into a dict
job_response_list_dict = job_response_list_instance.to_dict()
# create an instance of JobResponseList from a dict
job_response_list_form_dict = job_response_list.from_dict(job_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


