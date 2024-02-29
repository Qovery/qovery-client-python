# ApplicationEditRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage** | [**List[ServiceStorageRequestStorageInner]**](ServiceStorageRequestStorageInner.md) |  | [optional] 
**name** | **str** | name is case insensitive | [optional] 
**description** | **str** | give a description to this application | [optional] 
**git_repository** | [**ApplicationGitRepositoryRequest**](ApplicationGitRepositoryRequest.md) |  | [optional] 
**build_mode** | [**BuildModeEnum**](BuildModeEnum.md) |  | [optional] 
**dockerfile_path** | **str** | The path of the associated Dockerfile | [optional] 
**buildpack_language** | [**BuildPackLanguageEnum**](BuildPackLanguageEnum.md) |  | [optional] 
**cpu** | **int** | unit is millicores (m). 1000m &#x3D; 1 cpu | [optional] [default to 500]
**memory** | **int** | unit is MB. 1024 MB &#x3D; 1GB | [optional] [default to 512]
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
from qovery.models.application_edit_request import ApplicationEditRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationEditRequest from a JSON string
application_edit_request_instance = ApplicationEditRequest.from_json(json)
# print the JSON string representation of the object
print ApplicationEditRequest.to_json()

# convert the object into a dict
application_edit_request_dict = application_edit_request_instance.to_dict()
# create an instance of ApplicationEditRequest from a dict
application_edit_request_form_dict = application_edit_request.from_dict(application_edit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


