# ServiceResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | uuid of the associated service (application, database, job, gateway...) | 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**type** | [**ServiceTypeEnum**](ServiceTypeEnum.md) |  | [optional] 
**name** | **str** | name of the service | [optional] 
**deployed_commit_id** | **str** | Git commit ID corresponding to the deployed version of the application | [optional] 
**last_updated_by** | **str** | uuid of the user that made the last update | [optional] 
**consumed_resources_in_percent** | **float** | global overview of resources consumption of the service | [optional] 
**service_typology** | **str** | describes the typology of service (container, postgresl, redis...) | [optional] 
**service_version** | **str** | for databases this field exposes the database version | [optional] 
**to_update** | **bool** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


