# EnvironmentLogResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_at** | **datetime** |  | 
**message** | **str, none_type** | Log message | 
**scope** | [**EnvironmentLogResponseScope**](EnvironmentLogResponseScope.md) |  | [optional] 
**state** | **str** | Status is a state machine. It starts with &#x60;BUILDING&#x60; or &#x60;DEPLOYING&#x60; state (or &#x60;INITIALIZED&#x60;if auto-deploy is deactivated). Then finish with &#x60;*_ERROR&#x60; or any termination state.  | [optional] 
**execution_id** | **str** | Only for errors. Helps Qovery team to investigate. | [optional] 
**hint** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


