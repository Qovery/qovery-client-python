# DeploymentHistoryJobResponseAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name of the job | [optional] 
**status** | [**DeploymentHistoryStatusEnum**](DeploymentHistoryStatusEnum.md) |  | [optional] 
**image_name** | **str** |  | [optional] 
**tag** | **str** |  | [optional] 
**commit** | [**Commit**](Commit.md) |  | [optional] 
**schedule** | [**JobRequestAllOfSchedule**](JobRequestAllOfSchedule.md) |  | [optional] 
**arguments** | **[str]** |  | [optional] 
**entrypoint** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

