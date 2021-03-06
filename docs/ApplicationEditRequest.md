# ApplicationEditRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage** | [**[ApplicationStorageStorageInner]**](ApplicationStorageStorageInner.md) |  | [optional] 
**ports** | [**[ServicePortPortsInner]**](ServicePortPortsInner.md) |  | [optional] 
**name** | **str** | name is case insensitive | [optional] 
**description** | **str** | give a description to this application | [optional] 
**git_repository** | [**ApplicationGitRepositoryRequest**](ApplicationGitRepositoryRequest.md) |  | [optional] 
**build_mode** | [**BuildModeEnum**](BuildModeEnum.md) |  | [optional] 
**dockerfile_path** | **str** | The path of the associated Dockerfile | [optional] 
**buildpack_language** | [**BuildPackLanguageEnum**](BuildPackLanguageEnum.md) |  | [optional] 
**cpu** | **int** | unit is millicores (m). 1000m &#x3D; 1 cpu | [optional]  if omitted the server will use the default value of 250
**memory** | **int** | unit is MB. 1024 MB &#x3D; 1GB | [optional]  if omitted the server will use the default value of 256
**min_running_instances** | **int** | Minimum number of instances running. This resource auto-scale based on the CPU and Memory consumption. Note: 0 means that there is no application running.  | [optional]  if omitted the server will use the default value of 1
**max_running_instances** | **int** | Maximum number of instances running. This resource auto-scale based on the CPU and Memory consumption. Note: -1 means that there is no limit.  | [optional]  if omitted the server will use the default value of 1
**healthcheck** | [**Healthcheck**](Healthcheck.md) |  | [optional] 
**auto_preview** | **bool** | Specify if the environment preview option is activated or not for this application. If activated, a preview environment will be automatically cloned at each pull request.  | [optional]  if omitted the server will use the default value of True
**sticky_session** | **bool** | Specify if the sticky session option (also called persistant session) is activated or not for this application. If activated, user will be redirected by the load balancer to the same instance each time he access to the application.  | [optional]  if omitted the server will use the default value of False
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


