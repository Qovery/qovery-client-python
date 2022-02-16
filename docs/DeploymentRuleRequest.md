# DeploymentRuleRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name is case insensitive | 
**mode** | **str** |  | 
**cluster** | **str** |  | 
**auto_stop** | **bool** |  | defaults to False
**description** | **str** |  | [optional] 
**auto_deploy** | **bool** |  | [optional]  if omitted the server will use the default value of True
**timezone** | **str** | specify value only if auto_stop &#x3D; false | [optional]  if omitted the server will use the default value of "Europe/London"
**start_time** | **datetime, none_type** | specify value only if auto_stop &#x3D; false | [optional] 
**stop_time** | **datetime, none_type** | specify value only if auto_stop &#x3D; false | [optional] 
**weekdays** | **[str], none_type** | specify value only if auto_stop &#x3D; false | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


