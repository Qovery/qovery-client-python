# ContainerDeployRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_tag** | **str** | Image tag to deploy | 

## Example

```python
from qovery.models.container_deploy_request import ContainerDeployRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContainerDeployRequest from a JSON string
container_deploy_request_instance = ContainerDeployRequest.from_json(json)
# print the JSON string representation of the object
print ContainerDeployRequest.to_json()

# convert the object into a dict
container_deploy_request_dict = container_deploy_request_instance.to_dict()
# create an instance of ContainerDeployRequest from a dict
container_deploy_request_form_dict = container_deploy_request.from_dict(container_deploy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


