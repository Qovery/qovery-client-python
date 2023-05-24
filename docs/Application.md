# Application


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**storage** | [**[ServiceStorageStorageInner]**](ServiceStorageStorageInner.md) |  | [optional] 
**environment** | [**ReferenceObject**](ReferenceObject.md) |  | [optional] 
**git_repository** | [**ApplicationGitRepository**](ApplicationGitRepository.md) |  | [optional] 
**maximum_cpu** | **int** | Maximum cpu that can be allocated to the application based on organization cluster configuration. unit is millicores (m). 1000m &#x3D; 1 cpu | [optional] 
**maximum_memory** | **int** | Maximum memory that can be allocated to the application based on organization cluster configuration. unit is MB. 1024 MB &#x3D; 1GB | [optional] 
**name** | **str** | name is case insensitive | [optional] 
**description** | **str, none_type** | give a description to this application | [optional] 
**build_mode** | [**BuildModeEnum**](BuildModeEnum.md) |  | [optional] 
**dockerfile_path** | **str, none_type** | The path of the associated Dockerfile. Only if you are using build_mode &#x3D; DOCKER | [optional] 
**buildpack_language** | [**BuildPackLanguageEnum**](BuildPackLanguageEnum.md) |  | [optional] 
**cpu** | **int** | unit is millicores (m). 1000m &#x3D; 1 cpu | [optional] 
**memory** | **int** | unit is MB. 1024 MB &#x3D; 1GB | [optional] 
**min_running_instances** | **int** | Minimum number of instances running. This resource auto-scale based on the CPU and Memory consumption. Note: 0 means that there is no application running.  | [optional]  if omitted the server will use the default value of 1
**max_running_instances** | **int** | Maximum number of instances running. This resource auto-scale based on the CPU and Memory consumption. Note: -1 means that there is no limit.  | [optional]  if omitted the server will use the default value of 1
**healthchecks** | [**Healthcheck**](Healthcheck.md) |  | [optional] 
**auto_preview** | **bool** | Specify if the environment preview option is activated or not for this application.   If activated, a preview environment will be automatically cloned at each pull request.   If not specified, it takes the value of the &#x60;auto_preview&#x60; property from the associated environment.  | [optional]  if omitted the server will use the default value of True
**ports** | [**ServicePortResponseList**](ServicePortResponseList.md) |  | [optional] 
**arguments** | **[str]** |  | [optional] 
**entrypoint** | **str** | optional entrypoint when launching container | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


