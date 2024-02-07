# SecretAlias


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**key** | **str** |  | 
**mount_path** | **str** |  | 
**scope** | [**APIVariableScopeEnum**](APIVariableScopeEnum.md) |  | 
**variable_type** | [**APIVariableTypeEnum**](APIVariableTypeEnum.md) |  | 

## Example

```python
from qovery.models.secret_alias import SecretAlias

# TODO update the JSON string below
json = "{}"
# create an instance of SecretAlias from a JSON string
secret_alias_instance = SecretAlias.from_json(json)
# print the JSON string representation of the object
print SecretAlias.to_json()

# convert the object into a dict
secret_alias_dict = secret_alias_instance.to_dict()
# create an instance of SecretAlias from a dict
secret_alias_form_dict = secret_alias.from_dict(secret_alias_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


