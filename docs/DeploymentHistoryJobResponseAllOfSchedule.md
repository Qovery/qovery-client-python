# DeploymentHistoryJobResponseAllOfSchedule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**JobScheduleEvent**](JobScheduleEvent.md) |  | [optional] 
**schedule_at** | **str** | Can only be set if the event is CRON. Represent the cron format for the job schedule without seconds. For example: &#x60;* * * * *&#x60; represent the cron to launch the job every minute. See https://crontab.guru/ to WISIWIG interface. Timezone is UTC  | [optional] 

## Example

```python
from qovery.models.deployment_history_job_response_all_of_schedule import DeploymentHistoryJobResponseAllOfSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentHistoryJobResponseAllOfSchedule from a JSON string
deployment_history_job_response_all_of_schedule_instance = DeploymentHistoryJobResponseAllOfSchedule.from_json(json)
# print the JSON string representation of the object
print DeploymentHistoryJobResponseAllOfSchedule.to_json()

# convert the object into a dict
deployment_history_job_response_all_of_schedule_dict = deployment_history_job_response_all_of_schedule_instance.to_dict()
# create an instance of DeploymentHistoryJobResponseAllOfSchedule from a dict
deployment_history_job_response_all_of_schedule_form_dict = deployment_history_job_response_all_of_schedule.from_dict(deployment_history_job_response_all_of_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


