# OrganizationEditRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name is case insensitive | 
**description** | **str** |  | [optional] 
**website_url** | **str** |  | [optional] 
**repository** | **str** |  | [optional] 
**logo_url** | **str** |  | [optional] 
**icon_url** | **str** |  | [optional] 
**admin_emails** | **List[str]** |  | [optional] 

## Example

```python
from qovery.models.organization_edit_request import OrganizationEditRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationEditRequest from a JSON string
organization_edit_request_instance = OrganizationEditRequest.from_json(json)
# print the JSON string representation of the object
print OrganizationEditRequest.to_json()

# convert the object into a dict
organization_edit_request_dict = organization_edit_request_instance.to_dict()
# create an instance of OrganizationEditRequest from a dict
organization_edit_request_form_dict = organization_edit_request.from_dict(organization_edit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


