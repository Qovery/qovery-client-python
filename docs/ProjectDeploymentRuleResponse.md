# ProjectDeploymentRuleResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**name** | **str** | name is case insensitive | 
**mode** | **str** |  | 
**cluster_id** | **str** |  | 
**timezone** | **str** |  | 
**start_time** | **datetime** |  | 
**stop_time** | **datetime** |  | 
**weekdays** | **[str]** |  | 
**wildcard** | **str** | wildcard pattern composed of &#39;?&#39; and/or &#39;*&#39; used to target new created environments | defaults to ""
**priority_index** | **int** | used to select the first deployment rule to match new created environments | [optional] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**description** | **str, none_type** |  | [optional] 
**auto_deploy** | **bool** |  | [optional]  if omitted the server will use the default value of False
**auto_stop** | **bool** |  | [optional]  if omitted the server will use the default value of False
**auto_delete** | **bool** |  | [optional]  if omitted the server will use the default value of False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


