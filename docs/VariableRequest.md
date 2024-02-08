# VariableRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | the key of the environment variable | 
**value** | **str** | the value of the environment variable | 
**is_secret** | **bool** | if true, the variable will be considered as a secret and will not be accessible after its creation. Only your applications will be able to access its value at build and run time. | 
**variable_scope** | [**APIVariableScopeEnum**](APIVariableScopeEnum.md) |  | 
**variable_parent_id** | **str** | based on the selected scope, it contains the ID of the service, environment or project where the variable is attached | 
**mount_path** | **str, none_type** | the path where the file will be mounted (only if type &#x3D;file) | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


