# Database


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**name** | **str** | name is case insensitive | 
**description** | **str** | give a description to this database | [optional] 
**type** | [**DatabaseTypeEnum**](DatabaseTypeEnum.md) |  | 
**version** | **str** |  | 
**mode** | [**DatabaseModeEnum**](DatabaseModeEnum.md) |  | 
**accessibility** | [**DatabaseAccessibilityEnum**](DatabaseAccessibilityEnum.md) |  | [optional] 
**cpu** | **int** | unit is millicores (m). 1000m &#x3D; 1 cpu This field will be ignored for managed DB (instance type will be used instead).  | [optional] [default to 250]
**instance_type** | **str** | Database instance type to be used for this database. The list of values can be retrieved via the endpoint /{CloudProvider}/managedDatabase/instanceType/{region}/{dbType}. This field is null for container DB. | [optional] 
**memory** | **int** | unit is MB. 1024 MB &#x3D; 1GB This field will be ignored for managed DB (instance type will be used instead). Default value is linked to the database type: - MANAGED: &#x60;100&#x60; - CONTAINER   - POSTGRES: &#x60;100&#x60;   - REDIS: &#x60;100&#x60;   - MYSQL: &#x60;512&#x60;   - MONGODB: &#x60;256&#x60;  | [optional] 
**storage** | **int** | unit is GB | [optional] [default to 10]
**environment** | [**ReferenceObject**](ReferenceObject.md) |  | 
**host** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**maximum_cpu** | **int** | Maximum cpu that can be allocated to the database based on organization cluster configuration. unit is millicores (m). 1000m &#x3D; 1 cpu | [optional] 
**maximum_memory** | **int** | Maximum memory that can be allocated to the database based on organization cluster configuration. unit is MB. 1024 MB &#x3D; 1GB | [optional] 
**disk_encrypted** | **bool** | indicates if the database disk is encrypted or not | [optional] 

## Example

```python
from qovery.models.database import Database

# TODO update the JSON string below
json = "{}"
# create an instance of Database from a JSON string
database_instance = Database.from_json(json)
# print the JSON string representation of the object
print Database.to_json()

# convert the object into a dict
database_dict = database_instance.to_dict()
# create an instance of Database from a dict
database_form_dict = database.from_dict(database_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


