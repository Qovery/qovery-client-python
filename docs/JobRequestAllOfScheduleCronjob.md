# JobRequestAllOfScheduleCronjob


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arguments** | **List[str]** |  | [optional] 
**entrypoint** | **str** | optional entrypoint when launching container | [optional] 
**timezone** | **str** | Specify a timezone identifier to run the schedule at. By default Etc/UTC | [optional] 
**scheduled_at** | **str** | Can only be set if the event is CRON.   Represent the cron format for the job schedule without seconds.   For example: &#x60;* * * * *&#x60; represent the cron to launch the job every minute.   See https://crontab.guru/ to WISIWIG interface.   Timezone is UTC  | 

## Example

```python
from qovery.models.job_request_all_of_schedule_cronjob import JobRequestAllOfScheduleCronjob

# TODO update the JSON string below
json = "{}"
# create an instance of JobRequestAllOfScheduleCronjob from a JSON string
job_request_all_of_schedule_cronjob_instance = JobRequestAllOfScheduleCronjob.from_json(json)
# print the JSON string representation of the object
print JobRequestAllOfScheduleCronjob.to_json()

# convert the object into a dict
job_request_all_of_schedule_cronjob_dict = job_request_all_of_schedule_cronjob_instance.to_dict()
# create an instance of JobRequestAllOfScheduleCronjob from a dict
job_request_all_of_schedule_cronjob_form_dict = job_request_all_of_schedule_cronjob.from_dict(job_request_all_of_schedule_cronjob_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


