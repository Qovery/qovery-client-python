# DatabaseRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name is case insensitive | 
**description** | **str** | give a description to this database | [optional] 
**type** | [**DatabaseTypeEnum**](DatabaseTypeEnum.md) |  | 
**version** | **str** |  | 
**mode** | [**DatabaseModeEnum**](DatabaseModeEnum.md) |  | 
**accessibility** | [**DatabaseAccessibilityEnum**](DatabaseAccessibilityEnum.md) |  | [optional] 
**cpu** | **int** | unit is millicores (m). 1000m &#x3D; 1 cpu This field will be ignored for managed DB (instance type will be used instead).  | [optional] [default to 250]
**instance_type** | **str** | Database instance type to be used for this database. The list of values can be retrieved via the endpoint /{CloudProvider}/managedDatabase/instanceType/{region}/{dbType}. This field SHOULD NOT be set for container DB. | [optional] 
**memory** | **int** | unit is MB. 1024 MB &#x3D; 1GB This field will be ignored for managed DB (instance type will be used instead). Default value is linked to the database type: - MANAGED: &#x60;100&#x60; - CONTAINER   - POSTGRES: &#x60;100&#x60;   - REDIS: &#x60;100&#x60;   - MYSQL: &#x60;512&#x60;   - MONGODB: &#x60;256&#x60;  | [optional] 
**storage** | **int** | unit is GB | [optional] [default to 10]

## Example

```python
from qovery.models.database_request import DatabaseRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseRequest from a JSON string
database_request_instance = DatabaseRequest.from_json(json)
# print the JSON string representation of the object
print DatabaseRequest.to_json()

# convert the object into a dict
database_request_dict = database_request_instance.to_dict()
# create an instance of DatabaseRequest from a dict
database_request_form_dict = database_request.from_dict(database_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


