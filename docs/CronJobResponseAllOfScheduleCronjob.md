# CronJobResponseAllOfScheduleCronjob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arguments** | **List[str]** |  | [optional] 
**entrypoint** | **str** | optional entrypoint when launching container | [optional] 
**timezone** | **str** | tz identifier at which the schedule at will be executed | 
**scheduled_at** | **str** | Can only be set if the event is CRON.   Represent the cron format for the job schedule without seconds.   For example: &#x60;* * * * *&#x60; represent the cron to launch the job every minute.   See https://crontab.guru/ to WISIWIG interface.   Timezone is UT  | 

## Example

```python
from qovery.models.cron_job_response_all_of_schedule_cronjob import CronJobResponseAllOfScheduleCronjob

# TODO update the JSON string below
json = "{}"
# create an instance of CronJobResponseAllOfScheduleCronjob from a JSON string
cron_job_response_all_of_schedule_cronjob_instance = CronJobResponseAllOfScheduleCronjob.from_json(json)
# print the JSON string representation of the object
print CronJobResponseAllOfScheduleCronjob.to_json()

# convert the object into a dict
cron_job_response_all_of_schedule_cronjob_dict = cron_job_response_all_of_schedule_cronjob_instance.to_dict()
# create an instance of CronJobResponseAllOfScheduleCronjob from a dict
cron_job_response_all_of_schedule_cronjob_form_dict = cron_job_response_all_of_schedule_cronjob.from_dict(cron_job_response_all_of_schedule_cronjob_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


