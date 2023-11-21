# DatabaseAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | [**ReferenceObject**](ReferenceObject.md) |  | 
**host** | **str** |  | [optional] 
**port** | **int** |  | [optional] 
**maximum_cpu** | **int** | Maximum cpu that can be allocated to the database based on organization cluster configuration. unit is millicores (m). 1000m &#x3D; 1 cpu | [optional] 
**maximum_memory** | **int** | Maximum memory that can be allocated to the database based on organization cluster configuration. unit is MB. 1024 MB &#x3D; 1GB | [optional] 
**disk_encrypted** | **bool** | indicates if the database disk is encrypted or not | [optional] 
**instance_type** | **str** | Database instance type to be used for this database. The list of values can be retrieved via the endpoint /{CloudProvider}/managedDatabase/instanceType/{region}/{dbType}. This field is null for container DB. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


