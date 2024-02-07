# ManagedDatabaseInstanceTypeResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ManagedDatabaseInstanceTypeResponse]**](ManagedDatabaseInstanceTypeResponse.md) |  | [optional] 

## Example

```python
from qovery.models.managed_database_instance_type_response_list import ManagedDatabaseInstanceTypeResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedDatabaseInstanceTypeResponseList from a JSON string
managed_database_instance_type_response_list_instance = ManagedDatabaseInstanceTypeResponseList.from_json(json)
# print the JSON string representation of the object
print ManagedDatabaseInstanceTypeResponseList.to_json()

# convert the object into a dict
managed_database_instance_type_response_list_dict = managed_database_instance_type_response_list_instance.to_dict()
# create an instance of ManagedDatabaseInstanceTypeResponseList from a dict
managed_database_instance_type_response_list_form_dict = managed_database_instance_type_response_list.from_dict(managed_database_instance_type_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


