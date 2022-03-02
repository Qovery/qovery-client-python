# ClusterResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_at** | **datetime** |  | [readonly] 
**name** | **str** | name is case-insensitive | 
**cloud_provider** | **str** |  | 
**region** | **str** |  | 
**updated_at** | **datetime** |  | [optional] [readonly] 
**description** | **str, none_type** |  | [optional] 
**auto_update** | **bool** |  | [optional] 
**cpu** | **int** | unit is millicores (m). 1000m &#x3D; 1 cpu | [optional]  if omitted the server will use the default value of 250
**memory** | **int** | unit is MB. 1024 MB &#x3D; 1GB | [optional]  if omitted the server will use the default value of 256
**min_running_nodes** | **int** |  | [optional]  if omitted the server will use the default value of 1
**max_running_nodes** | **int** |  | [optional]  if omitted the server will use the default value of 1
**title** | **str** |  | [optional] 
**cost_per_month_in_cents** | **int, none_type** |  | [optional] 
**cost_per_month** | **float, none_type** |  | [optional] 
**currency_code** | **str, none_type** |  | [optional] 
**value_type** | **str** |  | [optional]  if omitted the server will use the default value of "BOOLEAN"
**value** | **str, none_type** |  | [optional] 
**is_value_updatable** | **bool** |  | [optional]  if omitted the server will use the default value of False
**accepted_values** | **[bool, date, datetime, dict, float, int, list, str, none_type]** |  | [optional] 
**estimated_cloud_provider_cost** | **int** | This is an estimation of the cost this cluster will represent on your cloud proider bill, based on your current configuration | [optional] 
**status** | **str** |  | [optional] 
**has_access** | **bool** |  | [optional] 
**version** | **str** |  | [optional] 
**is_default** | **bool** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


