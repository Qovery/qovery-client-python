# JobScheduleEvent

On which event the job is going to run.   ON_START means when a deployment is requested for the environment   ON_STOP means when a stop of the environment is requested   ON_DELETE means when an environment delete is requested CRON means at a scheduled interval   

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | On which event the job is going to run.   ON_START means when a deployment is requested for the environment   ON_STOP means when a stop of the environment is requested   ON_DELETE means when an environment delete is requested CRON means at a scheduled interval    |  must be one of ["ON_START", "ON_STOP", "ON_DELETE", "CRON", ]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


