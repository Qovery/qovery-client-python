# ManagedDatabaseTypeResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ManagedDatabaseTypeResponse]**](ManagedDatabaseTypeResponse.md) |  | [optional] 

## Example

```python
from qovery.models.managed_database_type_response_list import ManagedDatabaseTypeResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedDatabaseTypeResponseList from a JSON string
managed_database_type_response_list_instance = ManagedDatabaseTypeResponseList.from_json(json)
# print the JSON string representation of the object
print ManagedDatabaseTypeResponseList.to_json()

# convert the object into a dict
managed_database_type_response_list_dict = managed_database_type_response_list_instance.to_dict()
# create an instance of ManagedDatabaseTypeResponseList from a dict
managed_database_type_response_list_form_dict = managed_database_type_response_list.from_dict(managed_database_type_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


