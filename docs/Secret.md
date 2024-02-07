# Secret


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**key** | **str** | key is case sensitive | 
**overridden_secret** | [**SecretOverride**](SecretOverride.md) |  | [optional] 
**aliased_secret** | [**SecretAlias**](SecretAlias.md) |  | [optional] 
**scope** | [**APIVariableScopeEnum**](APIVariableScopeEnum.md) |  | 
**variable_type** | [**APIVariableTypeEnum**](APIVariableTypeEnum.md) |  | [optional] 
**service_id** | **str** |  | [optional] 
**service_name** | **str** |  | [optional] 
**service_type** | [**LinkedServiceTypeEnum**](LinkedServiceTypeEnum.md) |  | [optional] 
**owned_by** | **str** | Entity that created/own the variable (i.e: Qovery, Doppler) | [optional] 

## Example

```python
from qovery.models.secret import Secret

# TODO update the JSON string below
json = "{}"
# create an instance of Secret from a JSON string
secret_instance = Secret.from_json(json)
# print the JSON string representation of the object
print Secret.to_json()

# convert the object into a dict
secret_dict = secret_instance.to_dict()
# create an instance of Secret from a dict
secret_form_dict = secret.from_dict(secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


