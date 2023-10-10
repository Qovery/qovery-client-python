# VariableResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**scope** | [**APIVariableScopeEnum**](APIVariableScopeEnum.md) |  | 
**updated_at** | **datetime** |  | [optional] [readonly] 
**overridden_variable** | [**VariableOverride**](VariableOverride.md) |  | [optional] 
**aliased_variable** | [**VariableAlias**](VariableAlias.md) |  | [optional] 
**variable_type** | [**APIVariableTypeEnum**](APIVariableTypeEnum.md) |  | [optional] 
**service_id** | **str** | The id of the service referenced by this variable. | [optional] 
**service_name** | **str** | The name of the service referenced by this variable. | [optional] 
**service_type** | [**LinkedServiceTypeEnum**](LinkedServiceTypeEnum.md) |  | [optional] 
**owned_by** | **str** | Entity that created/own the variable (i.e: Qovery, Doppler) | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


