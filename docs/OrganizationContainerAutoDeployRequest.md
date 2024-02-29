# OrganizationContainerAutoDeployRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_name** | **str** | the container image name to deploy | [optional] 
**tag** | **str** | the new tag to deploy | [optional] 

## Example

```python
from qovery.models.organization_container_auto_deploy_request import OrganizationContainerAutoDeployRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationContainerAutoDeployRequest from a JSON string
organization_container_auto_deploy_request_instance = OrganizationContainerAutoDeployRequest.from_json(json)
# print the JSON string representation of the object
print OrganizationContainerAutoDeployRequest.to_json()

# convert the object into a dict
organization_container_auto_deploy_request_dict = organization_container_auto_deploy_request_instance.to_dict()
# create an instance of OrganizationContainerAutoDeployRequest from a dict
organization_container_auto_deploy_request_form_dict = organization_container_auto_deploy_request.from_dict(organization_container_auto_deploy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


