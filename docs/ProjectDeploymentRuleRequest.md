# ProjectDeploymentRuleRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name is case insensitive | 
**mode** | **str** |  | 
**cluster_id** | **str** |  | 
**auto_deploy** | **bool** |  | 
**auto_stop** | **bool** |  | 
**start_time** | **datetime** | specify value only if auto_stop &#x3D; false | 
**stop_time** | **datetime** | specify value only if auto_stop &#x3D; false | 
**weekdays** | **[str]** | specify value only if auto_stop &#x3D; false | 
**wildcard** | **str, none_type** | wildcard pattern composed of &#39;?&#39; and/or &#39;*&#39; used to target new created environments | 
**timezone** | **str** | specify value only if auto_stop &#x3D; false | defaults to "Europe/London"
**description** | **str, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


