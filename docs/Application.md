# Application


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**storage** | [**List[ServiceStorageStorageInner]**](ServiceStorageStorageInner.md) |  | [optional] 
**environment** | [**ReferenceObject**](ReferenceObject.md) |  | 
**git_repository** | [**ApplicationGitRepository**](ApplicationGitRepository.md) |  | [optional] 
**maximum_cpu** | **int** | Maximum cpu that can be allocated to the application based on organization cluster configuration. unit is millicores (m). 1000m &#x3D; 1 cpu | [optional] 
**maximum_memory** | **int** | Maximum memory that can be allocated to the application based on organization cluster configuration. unit is MB. 1024 MB &#x3D; 1GB | [optional] 
**name** | **str** | name is case insensitive | 
**description** | **str** | give a description to this application | [optional] 
**build_mode** | [**BuildModeEnum**](BuildModeEnum.md) |  | [optional] 
**dockerfile_path** | **str** | The path of the associated Dockerfile. Only if you are using build_mode &#x3D; DOCKER | [optional] 
**buildpack_language** | [**BuildPackLanguageEnum**](BuildPackLanguageEnum.md) |  | [optional] 
**cpu** | **int** | unit is millicores (m). 1000m &#x3D; 1 cpu | [optional] 
**memory** | **int** | unit is MB. 1024 MB &#x3D; 1GB | [optional] 
**min_running_instances** | **int** | Minimum number of instances running. This resource auto-scale based on the CPU and Memory consumption. Note: 0 means that there is no application running.  | [optional] [default to 1]
**max_running_instances** | **int** | Maximum number of instances running. This resource auto-scale based on the CPU and Memory consumption. Note: -1 means that there is no limit.  | [optional] [default to 1]
**healthchecks** | [**Healthcheck**](Healthcheck.md) |  | 
**auto_preview** | **bool** | Specify if the environment preview option is activated or not for this application.   If activated, a preview environment will be automatically cloned at each pull request.   If not specified, it takes the value of the &#x60;auto_preview&#x60; property from the associated environment.  | [optional] [default to True]
**ports** | [**List[ServicePort]**](ServicePort.md) |  | [optional] 
**arguments** | **List[str]** |  | [optional] 
**entrypoint** | **str** | optional entrypoint when launching container | [optional] 
**auto_deploy** | **bool** | Specify if the application will be automatically updated after receiving a new commit. | [optional] 

## Example

```python
from qovery.models.application import Application

# TODO update the JSON string below
json = "{}"
# create an instance of Application from a JSON string
application_instance = Application.from_json(json)
# print the JSON string representation of the object
print Application.to_json()

# convert the object into a dict
application_dict = application_instance.to_dict()
# create an instance of Application from a dict
application_form_dict = application.from_dict(application_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


