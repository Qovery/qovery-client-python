# JobRequestAllOfSchedule

If you want to define a Cron job, only the `cronjob` property must be filled   A Lifecycle job should contain at least one property `on_XXX` among the 3 properties: `on_start`, `on_stop`, `on_delete` 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**on_start** | [**JobRequestAllOfScheduleOnStart**](JobRequestAllOfScheduleOnStart.md) |  | [optional] 
**on_stop** | [**JobRequestAllOfScheduleOnStart**](JobRequestAllOfScheduleOnStart.md) |  | [optional] 
**on_delete** | [**JobRequestAllOfScheduleOnStart**](JobRequestAllOfScheduleOnStart.md) |  | [optional] 
**cronjob** | [**JobRequestAllOfScheduleCronjob**](JobRequestAllOfScheduleCronjob.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


