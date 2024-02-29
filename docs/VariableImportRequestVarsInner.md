# VariableImportRequestVarsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**value** | **str** |  | 
**scope** | [**APIVariableScopeEnum**](APIVariableScopeEnum.md) |  | 
**is_secret** | **bool** |  | 

## Example

```python
from qovery.models.variable_import_request_vars_inner import VariableImportRequestVarsInner

# TODO update the JSON string below
json = "{}"
# create an instance of VariableImportRequestVarsInner from a JSON string
variable_import_request_vars_inner_instance = VariableImportRequestVarsInner.from_json(json)
# print the JSON string representation of the object
print VariableImportRequestVarsInner.to_json()

# convert the object into a dict
variable_import_request_vars_inner_dict = variable_import_request_vars_inner_instance.to_dict()
# create an instance of VariableImportRequestVarsInner from a dict
variable_import_request_vars_inner_form_dict = variable_import_request_vars_inner.from_dict(variable_import_request_vars_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


