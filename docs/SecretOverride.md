# SecretOverride


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
from qovery.models.secret_override import SecretOverride

# TODO update the JSON string below
json = "{}"
# create an instance of SecretOverride from a JSON string
secret_override_instance = SecretOverride.from_json(json)
# print the JSON string representation of the object
print SecretOverride.to_json()

# convert the object into a dict
secret_override_dict = secret_override_instance.to_dict()
# create an instance of SecretOverride from a dict
secret_override_form_dict = secret_override.from_dict(secret_override_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


