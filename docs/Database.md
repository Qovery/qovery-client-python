# Database


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**name** | **str** | name is case insensitive | 
**type** | [**DatabaseTypeEnum**](DatabaseTypeEnum.md) |  | 
**version** | **str** |  | 
**mode** | [**DatabaseModeEnum**](DatabaseModeEnum.md) |  | 
**updated_at** | **datetime** |  | [optional] [readonly] 
**accessibility** | [**DatabaseAccessibilityEnum**](DatabaseAccessibilityEnum.md) |  | [optional] 
**cpu** | **int** | unit is millicores (m). 1000m &#x3D; 1 cpu | [optional]  if omitted the server will use the default value of 250
**memory** | **int** | unit is MB. 1024 MB &#x3D; 1GB | [optional]  if omitted the server will use the default value of 256
**storage** | **int** | unit is MB | [optional]  if omitted the server will use the default value of 10240
**environment** | [**ReferenceObject**](ReferenceObject.md) |  | [optional] 
**host** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**maximum_cpu** | **int** | Maximum cpu that can be allocated to the database based on organization cluster configuration. unit is millicores (m). 1000m &#x3D; 1 cpu | [optional]  if omitted the server will use the default value of 250
**maximum_memory** | **int** | Maximum memory that can be allocated to the database based on organization cluster configuration. unit is MB. 1024 MB &#x3D; 1GB | [optional]  if omitted the server will use the default value of 256
**disk_encrypted** | **bool** | indicates if the database disk is encrypted or not | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


