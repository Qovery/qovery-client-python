# GitTokenResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**name** | **str** |  | 
**type** | [**GitProviderEnum**](GitProviderEnum.md) |  | 
**associated_services_count** | **float** | The number of services using this git token | 
**updated_at** | **datetime** |  | [optional] [readonly] 
**description** | **str** |  | [optional] 
**expired_at** | **date** |  | [optional] 
**workspace** | **str** | Mandatory only for BITBUCKET git provider | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

