# Secret


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**scope** | [**EnvironmentVariableScopeEnum**](EnvironmentVariableScopeEnum.md) |  | 
**updated_at** | **datetime** |  | [optional] [readonly] 
**key** | **str** | key is case sensitive | [optional] 
**overridden_secret** | [**OverriddenSecret**](OverriddenSecret.md) |  | [optional] 
**aliased_secret** | [**AliasedSecret**](AliasedSecret.md) |  | [optional] 
**service_id** | **str** | present only for &#x60;BUILT_IN&#x60; variable | [optional] 
**service_name** | **str** | present only for &#x60;BUILT_IN&#x60; variable | [optional] 
**service_type** | [**LinkedServiceTypeEnum**](LinkedServiceTypeEnum.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


