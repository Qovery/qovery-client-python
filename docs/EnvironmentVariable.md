# EnvironmentVariable


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**key** | **str** | key is case sensitive | 
**value** | **str** | value of the env variable. | 
**scope** | [**APIVariableScopeEnum**](APIVariableScopeEnum.md) |  | 
**updated_at** | **datetime** |  | [optional] [readonly] 
**overridden_variable** | [**EnvironmentVariableAllOfOverriddenVariable**](EnvironmentVariableAllOfOverriddenVariable.md) |  | [optional] 
**aliased_variable** | [**EnvironmentVariableAllOfAliasedVariable**](EnvironmentVariableAllOfAliasedVariable.md) |  | [optional] 
**service_id** | **str** | present only for &#x60;BUILT_IN&#x60; variable | [optional] 
**service_name** | **str** | present only for &#x60;BUILT_IN&#x60; variable | [optional] 
**service_type** | [**LinkedServiceTypeEnum**](LinkedServiceTypeEnum.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


