# ContainerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**storage** | [**List[ServiceStorageStorageInner]**](ServiceStorageStorageInner.md) |  | [optional] 
**image_name** | **str** | The image name pattern differs according to chosen container registry provider: * &#x60;ECR&#x60;: &#x60;repository&#x60; * &#x60;SCALEWAY_CR&#x60;: &#x60;namespace/image&#x60; * &#x60;DOCKER_HUB&#x60;: &#x60;image&#x60; or &#x60;repository/image&#x60; * &#x60;PUBLIC_ECR&#x60;: &#x60;registry_alias/repository&#x60;  | 
**tag** | **str** | tag of the image container | 
**registry_id** | **str** | tag of the image container | [optional] 
**registry** | [**ContainerRegistryProviderDetailsResponse**](ContainerRegistryProviderDetailsResponse.md) |  | 
**environment** | [**ReferenceObject**](ReferenceObject.md) |  | 
**maximum_cpu** | **int** | Maximum cpu that can be allocated to the container based on organization cluster configuration. unit is millicores (m). 1000m &#x3D; 1 cpu | 
**maximum_memory** | **int** | Maximum memory that can be allocated to the container based on organization cluster configuration. unit is MB. 1024 MB &#x3D; 1GB | 
**name** | **str** | name is case insensitive | 
**description** | **str** | give a description to this container | [optional] 
**arguments** | **List[str]** |  | [optional] 
**entrypoint** | **str** | optional entrypoint when launching container | [optional] 
**cpu** | **int** | unit is millicores (m). 1000m &#x3D; 1 cpu | 
**memory** | **int** | unit is MB. 1024 MB &#x3D; 1GB | 
**min_running_instances** | **int** | Minimum number of instances running. This resource auto-scale based on the CPU and Memory consumption. Note: 0 means that there is no container running.  | [default to 1]
**max_running_instances** | **int** | Maximum number of instances running. This resource auto-scale based on the CPU and Memory consumption. Note: -1 means that there is no limit.  | [default to 1]
**healthchecks** | [**Healthcheck**](Healthcheck.md) |  | 
**auto_preview** | **bool** | Indicates if the &#39;environment preview option&#39; is enabled for this container.   If enabled, a preview environment will be automatically cloned when &#x60;/preview&#x60; endpoint is called.   If not specified, it takes the value of the &#x60;auto_preview&#x60; property from the associated environment.  | 
**ports** | [**List[ServicePort]**](ServicePort.md) |  | [optional] 
**auto_deploy** | **bool** | Specify if the container will be automatically updated after receiving a new image tag.  The new image tag shall be communicated via the \&quot;Auto Deploy container\&quot; endpoint https://api-doc.qovery.com/#tag/Containers/operation/autoDeployContainerEnvironments  | [optional] 

## Example

```python
from qovery.models.container_response import ContainerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ContainerResponse from a JSON string
container_response_instance = ContainerResponse.from_json(json)
# print the JSON string representation of the object
print ContainerResponse.to_json()

# convert the object into a dict
container_response_dict = container_response_instance.to_dict()
# create an instance of ContainerResponse from a dict
container_response_form_dict = container_response.from_dict(container_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


