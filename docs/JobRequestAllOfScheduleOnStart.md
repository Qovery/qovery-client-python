# JobRequestAllOfScheduleOnStart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arguments** | **List[str]** |  | [optional] 
**entrypoint** | **str** | optional entrypoint when launching container | [optional] 

## Example

```python
from qovery.models.job_request_all_of_schedule_on_start import JobRequestAllOfScheduleOnStart

# TODO update the JSON string below
json = "{}"
# create an instance of JobRequestAllOfScheduleOnStart from a JSON string
job_request_all_of_schedule_on_start_instance = JobRequestAllOfScheduleOnStart.from_json(json)
# print the JSON string representation of the object
print JobRequestAllOfScheduleOnStart.to_json()

# convert the object into a dict
job_request_all_of_schedule_on_start_dict = job_request_all_of_schedule_on_start_instance.to_dict()
# create an instance of JobRequestAllOfScheduleOnStart from a dict
job_request_all_of_schedule_on_start_form_dict = job_request_all_of_schedule_on_start.from_dict(job_request_all_of_schedule_on_start_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


