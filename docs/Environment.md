# Environment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**name** | **str** | name is case insensitive | 
**project** | [**ReferenceObject**](ReferenceObject.md) |  | 
**cloud_provider** | [**EnvironmentAllOfCloudProvider**](EnvironmentAllOfCloudProvider.md) |  | 
**mode** | [**EnvironmentModeEnum**](EnvironmentModeEnum.md) |  | 
**cluster_id** | **str** |  | 
**updated_at** | **datetime** |  | [optional] [readonly] 
**organization** | [**ReferenceObject**](ReferenceObject.md) |  | [optional] 
**last_updated_by** | **str** | uuid of the user that made the last update | [optional] 
**cluster_name** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


