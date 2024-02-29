# VariableImportRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**overwrite** | **bool** |  | [default to False]
**vars** | [**List[VariableImportRequestVarsInner]**](VariableImportRequestVarsInner.md) |  | 

## Example

```python
from qovery.models.variable_import_request import VariableImportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VariableImportRequest from a JSON string
variable_import_request_instance = VariableImportRequest.from_json(json)
# print the JSON string representation of the object
print VariableImportRequest.to_json()

# convert the object into a dict
variable_import_request_dict = variable_import_request_instance.to_dict()
# create an instance of VariableImportRequest from a dict
variable_import_request_form_dict = variable_import_request.from_dict(variable_import_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


