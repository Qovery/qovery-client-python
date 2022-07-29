# ContainerRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name is case insensitive | 
**registry_id** | **str** | id of the linked registry | 
**image_name** | **str** | name of the image container | 
**tag** | **str** | tag of the image container | 
**storage** | [**[ServiceStorageRequestStorageInner]**](ServiceStorageRequestStorageInner.md) |  | [optional] 
**ports** | [**[ServicePortRequestPortsInner]**](ServicePortRequestPortsInner.md) |  | [optional] 
**arguments** | **[str]** |  | [optional] 
**entrypoint** | **str** | optional entrypoint when launching container | [optional] 
**cpu** | **int** | unit is millicores (m). 1000m &#x3D; 1 cpu | [optional]  if omitted the server will use the default value of 500
**memory** | **int** | unit is MB. 1024 MB &#x3D; 1GB | [optional]  if omitted the server will use the default value of 512
**min_running_instances** | **int** | Minimum number of instances running. This resource auto-scale based on the CPU and Memory consumption. Note: 0 means that there is no container running.  | [optional]  if omitted the server will use the default value of 1
**max_running_instances** | **int** | Maximum number of instances running. This resource auto-scale based on the CPU and Memory consumption. Note: -1 means that there is no limit.  | [optional]  if omitted the server will use the default value of 1
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


