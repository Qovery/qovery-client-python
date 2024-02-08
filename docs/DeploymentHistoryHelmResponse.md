# DeploymentHistoryHelmResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**name** | **str** | name of the helm | [optional] 
**status** | [**StateEnum**](StateEnum.md) |  | [optional] 
**commit** | [**Commit**](Commit.md) |  | [optional] 
**repository** | [**DeploymentHistoryHelmResponseAllOfRepository**](DeploymentHistoryHelmResponseAllOfRepository.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


