# ContainerRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage** | [**List[ServiceStorageRequestStorageInner]**](ServiceStorageRequestStorageInner.md) |  | [optional] 
**ports** | [**List[ServicePortRequestPortsInner]**](ServicePortRequestPortsInner.md) |  | [optional] 
**name** | **str** | name is case insensitive | 
**description** | **str** | give a description to this container | [optional] 
**registry_id** | **str** | id of the linked registry | 
**image_name** | **str** | The image name pattern differs according to chosen container registry provider:   * &#x60;ECR&#x60;: &#x60;repository&#x60; * &#x60;SCALEWAY_CR&#x60;: &#x60;namespace/image&#x60; * &#x60;DOCKER_HUB&#x60;: &#x60;image&#x60; or &#x60;repository/image&#x60; * &#x60;PUBLIC_ECR&#x60;: &#x60;registry_alias/repository&#x60;  | 
**tag** | **str** | tag of the image container | 
**arguments** | **List[str]** |  | [optional] 
**entrypoint** | **str** | optional entrypoint when launching container | [optional] 
**cpu** | **int** | unit is millicores (m). 1000m &#x3D; 1 cpu | [optional] [default to 500]
**memory** | **int** | unit is MB. 1024 MB &#x3D; 1GB | [optional] [default to 512]
**min_running_instances** | **int** | Minimum number of instances running. This resource auto-scale based on the CPU and Memory consumption. Note: 0 means that there is no container running.  | [optional] [default to 1]
**max_running_instances** | **int** | Maximum number of instances running. This resource auto-scale based on the CPU and Memory consumption. Note: -1 means that there is no limit.  | [optional] [default to 1]
**healthchecks** | [**Healthcheck**](Healthcheck.md) |  | 
**auto_preview** | **bool** | Indicates if the &#39;environment preview option&#39; is enabled for this container.   If enabled, a preview environment will be automatically cloned when &#x60;/preview&#x60; endpoint is called.   If not specified, it takes the value of the &#x60;auto_preview&#x60; property from the associated environment.  | [optional] 
**auto_deploy** | **bool** | Specify if the container will be automatically updated after receiving a new image tag.  The new image tag shall be communicated via the \&quot;Auto Deploy container\&quot; endpoint https://api-doc.qovery.com/#tag/Containers/operation/autoDeployContainerEnvironments  | [optional] 

## Example

```python
from qovery.models.container_request import ContainerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContainerRequest from a JSON string
container_request_instance = ContainerRequest.from_json(json)
# print the JSON string representation of the object
print ContainerRequest.to_json()

# convert the object into a dict
container_request_dict = container_request_instance.to_dict()
# create an instance of ContainerRequest from a dict
container_request_form_dict = container_request.from_dict(container_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


