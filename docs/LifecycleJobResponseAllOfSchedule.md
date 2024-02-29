# LifecycleJobResponseAllOfSchedule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**on_start** | [**JobRequestAllOfScheduleOnStart**](JobRequestAllOfScheduleOnStart.md) |  | [optional] 
**on_stop** | [**JobRequestAllOfScheduleOnStart**](JobRequestAllOfScheduleOnStart.md) |  | [optional] 
**on_delete** | [**JobRequestAllOfScheduleOnStart**](JobRequestAllOfScheduleOnStart.md) |  | [optional] 

## Example

```python
from qovery.models.lifecycle_job_response_all_of_schedule import LifecycleJobResponseAllOfSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of LifecycleJobResponseAllOfSchedule from a JSON string
lifecycle_job_response_all_of_schedule_instance = LifecycleJobResponseAllOfSchedule.from_json(json)
# print the JSON string representation of the object
print LifecycleJobResponseAllOfSchedule.to_json()

# convert the object into a dict
lifecycle_job_response_all_of_schedule_dict = lifecycle_job_response_all_of_schedule_instance.to_dict()
# create an instance of LifecycleJobResponseAllOfSchedule from a dict
lifecycle_job_response_all_of_schedule_form_dict = lifecycle_job_response_all_of_schedule.from_dict(lifecycle_job_response_all_of_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


