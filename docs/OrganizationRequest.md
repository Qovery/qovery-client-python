# OrganizationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name is case insensitive | 
**description** | **str** |  | [optional] 
**plan** | [**PlanEnum**](PlanEnum.md) |  | 
**website_url** | **str** |  | [optional] 
**repository** | **str** |  | [optional] 
**logo_url** | **str** |  | [optional] 
**icon_url** | **str** |  | [optional] 
**admin_emails** | **List[str]** |  | [optional] 

## Example

```python
from qovery.models.organization_request import OrganizationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationRequest from a JSON string
organization_request_instance = OrganizationRequest.from_json(json)
# print the JSON string representation of the object
print OrganizationRequest.to_json()

# convert the object into a dict
organization_request_dict = organization_request_instance.to_dict()
# create an instance of OrganizationRequest from a dict
organization_request_form_dict = organization_request.from_dict(organization_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


