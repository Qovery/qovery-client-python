# DatabaseEditRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name is case-insensitive | [optional] 
**description** | **str** | give a description to this database | [optional] 
**version** | **str** |  | [optional] 
**accessibility** | [**DatabaseAccessibilityEnum**](DatabaseAccessibilityEnum.md) |  | [optional] 
**cpu** | **int** | unit is millicores (m). 1000m &#x3D; 1 cpu. This field will be ignored for managed DB (instance type will be used instead).  | [optional]  if omitted the server will use the default value of 250
**memory** | **int** | unit is MB. 1024 MB &#x3D; 1GB This field will be ignored for managed DB (instance type will be used instead). Default value is linked to the database type: - MANAGED: 100 - CONTAINER   - POSTGRES: 100   - REDIS: 100   - MYSQL: 512   - MONGODB: 256  | [optional] 
**storage** | **int** | unit is GB | [optional] 
**instance_type** | **str** | Database instance type to be used for this database. The list of values can be retrieved via the endpoint /{CloudProvider}/managedDatabase/instanceType/{region}/{dbType}. This field SHOULD NOT be set for container DB. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


