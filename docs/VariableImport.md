# VariableImport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_variables_to_import** | **float** |  | 
**successful_imported_variables** | [**List[VariableImportSuccessfulImportedVariablesInner]**](VariableImportSuccessfulImportedVariablesInner.md) |  | 

## Example

```python
from qovery.models.variable_import import VariableImport

# TODO update the JSON string below
json = "{}"
# create an instance of VariableImport from a JSON string
variable_import_instance = VariableImport.from_json(json)
# print the JSON string representation of the object
print VariableImport.to_json()

# convert the object into a dict
variable_import_dict = variable_import_instance.to_dict()
# create an instance of VariableImport from a dict
variable_import_form_dict = variable_import.from_dict(variable_import_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


