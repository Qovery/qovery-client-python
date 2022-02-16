# EnvironmentDeploymentRuleEditRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_deploy** | **bool** |  | [optional]  if omitted the server will use the default value of True
**auto_delete** | **bool** |  | [optional]  if omitted the server will use the default value of False
**auto_stop** | **bool** |  | [optional]  if omitted the server will use the default value of False
**timezone** | **str** | specify value only if auto_stop &#x3D; false | [optional]  if omitted the server will use the default value of "Europe/London"
**start_time** | **datetime, none_type** | specify value only if auto_stop &#x3D; false | [optional] 
**stop_time** | **datetime, none_type** | specify value only if auto_stop &#x3D; false | [optional] 
**weekdays** | **[str], none_type** | specify value only if auto_stop &#x3D; false | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


