# ClusterBase


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name is case-insensitive | 
**cloud_provider** | [**CloudProviderEnum**](CloudProviderEnum.md) |  | 
**region** | **str** |  | 
**description** | **str** |  | [optional] 
**auto_update** | **bool** |  | [optional] 
**cpu** | **int** | unit is millicores (m). 1000m &#x3D; 1 cpu | [optional]  if omitted the server will use the default value of 250
**memory** | **int** | unit is MB. 1024 MB &#x3D; 1GB | [optional]  if omitted the server will use the default value of 256
**min_running_nodes** | **int** |  | [optional]  if omitted the server will use the default value of 1
**max_running_nodes** | **int** |  | [optional]  if omitted the server will use the default value of 1
**instance_type** | **str** | the instance type to be used for this cluster. The list of values can be retrieved via the endpoint /{CloudProvider}/instanceType | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


