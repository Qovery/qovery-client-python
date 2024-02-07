# VariableResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**key** | **str** |  | 
**value** | **str** |  | 
**mount_path** | **str** |  | [optional] 
**overridden_variable** | [**VariableOverride**](VariableOverride.md) |  | [optional] 
**aliased_variable** | [**VariableAlias**](VariableAlias.md) |  | [optional] 
**scope** | [**APIVariableScopeEnum**](APIVariableScopeEnum.md) |  | 
**variable_type** | [**APIVariableTypeEnum**](APIVariableTypeEnum.md) |  | [optional] 
**service_id** | **str** | The id of the service referenced by this variable. | [optional] 
**service_name** | **str** | The name of the service referenced by this variable. | [optional] 
**service_type** | [**LinkedServiceTypeEnum**](LinkedServiceTypeEnum.md) |  | [optional] 
**owned_by** | **str** | Entity that created/own the variable (i.e: Qovery, Doppler) | [optional] 
**is_secret** | **bool** |  | 

## Example

```python
from qovery.models.variable_response import VariableResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VariableResponse from a JSON string
variable_response_instance = VariableResponse.from_json(json)
# print the JSON string representation of the object
print VariableResponse.to_json()

# convert the object into a dict
variable_response_dict = variable_response_instance.to_dict()
# create an instance of VariableResponse from a dict
variable_response_form_dict = variable_response.from_dict(variable_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


