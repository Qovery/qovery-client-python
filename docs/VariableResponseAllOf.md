# VariableResponseAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | [**APIVariableScopeEnum**](APIVariableScopeEnum.md) |  | 
**overridden_variable** | [**VariableOverride**](VariableOverride.md) |  | [optional] 
**aliased_variable** | [**VariableAlias**](VariableAlias.md) |  | [optional] 
**variable_type** | [**APIVariableTypeEnum**](APIVariableTypeEnum.md) |  | [optional] 
**service_id** | **str** | present only for &#x60;BUILT_IN&#x60; variable | [optional] 
**service_name** | **str** | present only for &#x60;BUILT_IN&#x60; variable | [optional] 
**service_type** | [**LinkedServiceTypeEnum**](LinkedServiceTypeEnum.md) |  | [optional] 
**owned_by** | **str** | Entity that created/own the variable (i.e: Qovery, Doppler) | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


