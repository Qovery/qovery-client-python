# EnvironmentVariableResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**key** | **str** | key is case sensitive | 
**value** | **str** | value of the env variable. | 
**scope** | [**EnvironmentVariableScopeEnum**](EnvironmentVariableScopeEnum.md) |  | 
**updated_at** | **datetime** |  | [optional] [readonly] 
**overridden_variable** | [**EnvironmentVariableResponseAllOfOverriddenVariable**](EnvironmentVariableResponseAllOfOverriddenVariable.md) |  | [optional] 
**aliased_variable** | [**EnvironmentVariableResponseAllOfAliasedVariable**](EnvironmentVariableResponseAllOfAliasedVariable.md) |  | [optional] 
**service_name** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


