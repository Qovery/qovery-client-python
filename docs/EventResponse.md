# EventResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**user** | [**UserResponse**](UserResponse.md) |  | [optional] 
**commit** | [**CommitResponse**](CommitResponse.md) |  | [optional] 
**status** | [**Status**](Status.md) |  | [optional] 
**type** | **str** | DRAFT - we have to specify here all the possible events | [optional] 
**log** | [**ReferenceObject**](ReferenceObject.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


