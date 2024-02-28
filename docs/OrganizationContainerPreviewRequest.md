# OrganizationContainerPreviewRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_name** | **str** | the container image name to trigger preview environment | [optional] 
**tag** | **str** | the tag to be used in the preview environment | [optional] 

## Example

```python
from qovery.models.organization_container_preview_request import OrganizationContainerPreviewRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationContainerPreviewRequest from a JSON string
organization_container_preview_request_instance = OrganizationContainerPreviewRequest.from_json(json)
# print the JSON string representation of the object
print OrganizationContainerPreviewRequest.to_json()

# convert the object into a dict
organization_container_preview_request_dict = organization_container_preview_request_instance.to_dict()
# create an instance of OrganizationContainerPreviewRequest from a dict
organization_container_preview_request_form_dict = organization_container_preview_request.from_dict(organization_container_preview_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


