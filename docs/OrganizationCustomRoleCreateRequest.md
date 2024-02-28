# OrganizationCustomRoleCreateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from qovery.models.organization_custom_role_create_request import OrganizationCustomRoleCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationCustomRoleCreateRequest from a JSON string
organization_custom_role_create_request_instance = OrganizationCustomRoleCreateRequest.from_json(json)
# print the JSON string representation of the object
print OrganizationCustomRoleCreateRequest.to_json()

# convert the object into a dict
organization_custom_role_create_request_dict = organization_custom_role_create_request_instance.to_dict()
# create an instance of OrganizationCustomRoleCreateRequest from a dict
organization_custom_role_create_request_form_dict = organization_custom_role_create_request.from_dict(organization_custom_role_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


