# DatabaseEditRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name is case-insensitive | [optional] 
**description** | **str** | give a description to this database | [optional] 
**version** | **str** |  | [optional] 
**accessibility** | [**DatabaseAccessibilityEnum**](DatabaseAccessibilityEnum.md) |  | [optional] 
**cpu** | **int** | unit is millicores (m). 1000m &#x3D; 1 cpu. This field will be ignored for managed DB (instance type will be used instead).  | [optional] [default to 250]
**memory** | **int** | unit is MB. 1024 MB &#x3D; 1GB This field will be ignored for managed DB (instance type will be used instead). Default value is linked to the database type: - MANAGED: 100 - CONTAINER   - POSTGRES: 100   - REDIS: 100   - MYSQL: 512   - MONGODB: 256  | [optional] 
**storage** | **int** | unit is GB | [optional] 
**instance_type** | **str** | Database instance type to be used for this database. The list of values can be retrieved via the endpoint /{CloudProvider}/managedDatabase/instanceType/{region}/{dbType}. This field SHOULD NOT be set for container DB. | [optional] 

## Example

```python
from qovery.models.database_edit_request import DatabaseEditRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseEditRequest from a JSON string
database_edit_request_instance = DatabaseEditRequest.from_json(json)
# print the JSON string representation of the object
print DatabaseEditRequest.to_json()

# convert the object into a dict
database_edit_request_dict = database_edit_request_instance.to_dict()
# create an instance of DatabaseEditRequest from a dict
database_edit_request_form_dict = database_edit_request.from_dict(database_edit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


