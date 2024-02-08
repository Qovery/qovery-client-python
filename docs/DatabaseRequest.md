# DatabaseRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name is case insensitive | 
**type** | [**DatabaseTypeEnum**](DatabaseTypeEnum.md) |  | 
**version** | **str** |  | 
**mode** | [**DatabaseModeEnum**](DatabaseModeEnum.md) |  | 
**description** | **str** | give a description to this database | [optional] 
**accessibility** | [**DatabaseAccessibilityEnum**](DatabaseAccessibilityEnum.md) |  | [optional] 
**cpu** | **int** | unit is millicores (m). 1000m &#x3D; 1 cpu This field will be ignored for managed DB (instance type will be used instead).  | [optional]  if omitted the server will use the default value of 250
**instance_type** | **str** | Database instance type to be used for this database. The list of values can be retrieved via the endpoint /{CloudProvider}/managedDatabase/instanceType/{region}/{dbType}. This field SHOULD NOT be set for container DB. | [optional] 
**memory** | **int** | unit is MB. 1024 MB &#x3D; 1GB This field will be ignored for managed DB (instance type will be used instead). Default value is linked to the database type: - MANAGED: &#x60;100&#x60; - CONTAINER   - POSTGRES: &#x60;100&#x60;   - REDIS: &#x60;100&#x60;   - MYSQL: &#x60;512&#x60;   - MONGODB: &#x60;256&#x60;  | [optional] 
**storage** | **int** | unit is GB | [optional]  if omitted the server will use the default value of 10
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


