# ContainerResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**storage** | [**[ApplicationStorageStorageInner]**](ApplicationStorageStorageInner.md) |  | [optional] 
**ports** | [**[ApplicationPortPortsInner]**](ApplicationPortPortsInner.md) |  | [optional] 
**environment** | [**ReferenceObject**](ReferenceObject.md) |  | [optional] 
**maximum_cpu** | **int** | Maximum cpu that can be allocated to the container based on organization cluster configuration. unit is millicores (m). 1000m &#x3D; 1 cpu | [optional]  if omitted the server will use the default value of 250
**maximum_memory** | **int** | Maximum memory that can be allocated to the container based on organization cluster configuration. unit is MB. 1024 MB &#x3D; 1GB | [optional]  if omitted the server will use the default value of 256
**name** | **str** | name is case insensitive | [optional] 
**description** | **str, none_type** | give a description to this container | [optional] 
**registry_id** | **str** | id of the linked registry | [optional] 
**image_name** | **str** | name of the image container | [optional] 
**arguments** | **str** |  | [optional] 
**cpu** | **int** | unit is millicores (m). 1000m &#x3D; 1 cpu | [optional]  if omitted the server will use the default value of 250
**memory** | **int** | unit is MB. 1024 MB &#x3D; 1GB | [optional]  if omitted the server will use the default value of 256
**min_running_instances** | **int** | Minimum number of instances running. This resource auto-scale based on the CPU and Memory consumption. Note: 0 means that there is no container running.  | [optional]  if omitted the server will use the default value of 1
**max_running_instances** | **int** | Maximum number of instances running. This resource auto-scale based on the CPU and Memory consumption. Note: -1 means that there is no limit.  | [optional]  if omitted the server will use the default value of 1
**healthcheck** | [**Healthcheck**](Healthcheck.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


