# JobRequestAllOfSchedule

If you want to define a Cron job, only the `cronjob` property must be filled   A Lifecycle job should contain at least one property `on_XXX` among the 3 properties: `on_start`, `on_stop`, `on_delete` 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**on_start** | [**JobRequestAllOfScheduleOnStart**](JobRequestAllOfScheduleOnStart.md) |  | [optional] 
**on_stop** | [**JobRequestAllOfScheduleOnStart**](JobRequestAllOfScheduleOnStart.md) |  | [optional] 
**on_delete** | [**JobRequestAllOfScheduleOnStart**](JobRequestAllOfScheduleOnStart.md) |  | [optional] 
**cronjob** | [**JobRequestAllOfScheduleCronjob**](JobRequestAllOfScheduleCronjob.md) |  | [optional] 

## Example

```python
from qovery.models.job_request_all_of_schedule import JobRequestAllOfSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of JobRequestAllOfSchedule from a JSON string
job_request_all_of_schedule_instance = JobRequestAllOfSchedule.from_json(json)
# print the JSON string representation of the object
print JobRequestAllOfSchedule.to_json()

# convert the object into a dict
job_request_all_of_schedule_dict = job_request_all_of_schedule_instance.to_dict()
# create an instance of JobRequestAllOfSchedule from a dict
job_request_all_of_schedule_form_dict = job_request_all_of_schedule.from_dict(job_request_all_of_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


