# ManagedDatabaseInstanceTypeResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 

## Example

```python
from qovery.models.managed_database_instance_type_response import ManagedDatabaseInstanceTypeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ManagedDatabaseInstanceTypeResponse from a JSON string
managed_database_instance_type_response_instance = ManagedDatabaseInstanceTypeResponse.from_json(json)
# print the JSON string representation of the object
print ManagedDatabaseInstanceTypeResponse.to_json()

# convert the object into a dict
managed_database_instance_type_response_dict = managed_database_instance_type_response_instance.to_dict()
# create an instance of ManagedDatabaseInstanceTypeResponse from a dict
managed_database_instance_type_response_form_dict = managed_database_instance_type_response.from_dict(managed_database_instance_type_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


