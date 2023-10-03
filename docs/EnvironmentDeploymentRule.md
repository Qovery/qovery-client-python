# EnvironmentDeploymentRule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**timezone** | **str** |  | 
**start_time** | **datetime** |  | 
**stop_time** | **datetime** |  | 
**weekdays** | [**[WeekdayEnum]**](WeekdayEnum.md) |  | 
**updated_at** | **datetime** |  | [optional] [readonly] 
**on_demand_preview** | **bool** |  | [optional]  if omitted the server will use the default value of False
**auto_stop** | **bool** |  | [optional]  if omitted the server will use the default value of False
**auto_preview** | **bool** |  | [optional]  if omitted the server will use the default value of False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


