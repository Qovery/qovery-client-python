# VariableResponseList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[VariableResponse]**](VariableResponse.md) |  | [optional] 

## Example

```python
from qovery.models.variable_response_list import VariableResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of VariableResponseList from a JSON string
variable_response_list_instance = VariableResponseList.from_json(json)
# print the JSON string representation of the object
print VariableResponseList.to_json()

# convert the object into a dict
variable_response_list_dict = variable_response_list_instance.to_dict()
# create an instance of VariableResponseList from a dict
variable_response_list_form_dict = variable_response_list.from_dict(variable_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


