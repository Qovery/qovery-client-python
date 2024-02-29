# CronJobResponseAllOfSchedule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cronjob** | [**CronJobResponseAllOfScheduleCronjob**](CronJobResponseAllOfScheduleCronjob.md) |  | [optional] 

## Example

```python
from qovery.models.cron_job_response_all_of_schedule import CronJobResponseAllOfSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of CronJobResponseAllOfSchedule from a JSON string
cron_job_response_all_of_schedule_instance = CronJobResponseAllOfSchedule.from_json(json)
# print the JSON string representation of the object
print CronJobResponseAllOfSchedule.to_json()

# convert the object into a dict
cron_job_response_all_of_schedule_dict = cron_job_response_all_of_schedule_instance.to_dict()
# create an instance of CronJobResponseAllOfSchedule from a dict
cron_job_response_all_of_schedule_form_dict = cron_job_response_all_of_schedule.from_dict(cron_job_response_all_of_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


