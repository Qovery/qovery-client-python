# DeploymentHistoryEnvironment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**status** | [**StateEnum**](StateEnum.md) |  | [optional] 
**applications** | [**[DeploymentHistoryApplication]**](DeploymentHistoryApplication.md) |  | [optional] 
**databases** | [**[DeploymentHistoryDatabase]**](DeploymentHistoryDatabase.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


