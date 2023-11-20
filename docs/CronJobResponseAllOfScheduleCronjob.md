# CronJobResponseAllOfScheduleCronjob


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scheduled_at** | **str** | Can only be set if the event is CRON.   Represent the cron format for the job schedule without seconds.   For example: &#x60;* * * * *&#x60; represent the cron to launch the job every minute.   See https://crontab.guru/ to WISIWIG interface.   Timezone is UT  | 
**arguments** | **[str]** |  | [optional] 
**entrypoint** | **str** | optional entrypoint when launching container | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


