# ContainerResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**environment** | [**ReferenceObject**](ReferenceObject.md) |  | 
**registry** | [**ReferenceObject**](ReferenceObject.md) |  | 
**maximum_cpu** | **int** | Maximum cpu that can be allocated to the container based on organization cluster configuration. unit is millicores (m). 1000m &#x3D; 1 cpu | 
**maximum_memory** | **int** | Maximum memory that can be allocated to the container based on organization cluster configuration. unit is MB. 1024 MB &#x3D; 1GB | 
**name** | **str** | name is case insensitive | 
**image_name** | **str** | name of the image container | 
**tag** | **str** | tag of the image container | 
**cpu** | **int** | unit is millicores (m). 1000m &#x3D; 1 cpu | 
**memory** | **int** | unit is MB. 1024 MB &#x3D; 1GB | 
**auto_preview** | **bool** | Specify if the environment preview option is activated or not for this container. If activated, a preview environment will be automatically cloned at each pull request.  | 
**min_running_instances** | **int** | Minimum number of instances running. This resource auto-scale based on the CPU and Memory consumption. Note: 0 means that there is no container running.  | defaults to 1
**max_running_instances** | **int** | Maximum number of instances running. This resource auto-scale based on the CPU and Memory consumption. Note: -1 means that there is no limit.  | defaults to 1
**updated_at** | **datetime** |  | [optional] [readonly] 
**storage** | [**[ServiceStorageStorageInner]**](ServiceStorageStorageInner.md) |  | [optional] 
**arguments** | **[str]** |  | [optional] 
**entrypoint** | **str** | optional entrypoint when launching container | [optional] 
**ports** | [**ServicePortResponseList**](ServicePortResponseList.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


