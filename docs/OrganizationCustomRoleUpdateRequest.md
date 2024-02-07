# OrganizationCustomRoleUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**cluster_permissions** | [**List[OrganizationCustomRoleUpdateRequestClusterPermissionsInner]**](OrganizationCustomRoleUpdateRequestClusterPermissionsInner.md) | Should contain an entry for every existing cluster | 
**project_permissions** | [**List[OrganizationCustomRoleUpdateRequestProjectPermissionsInner]**](OrganizationCustomRoleUpdateRequestProjectPermissionsInner.md) | Should contain an entry for every existing project | 

## Example

```python
from qovery.models.organization_custom_role_update_request import OrganizationCustomRoleUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationCustomRoleUpdateRequest from a JSON string
organization_custom_role_update_request_instance = OrganizationCustomRoleUpdateRequest.from_json(json)
# print the JSON string representation of the object
print OrganizationCustomRoleUpdateRequest.to_json()

# convert the object into a dict
organization_custom_role_update_request_dict = organization_custom_role_update_request_instance.to_dict()
# create an instance of OrganizationCustomRoleUpdateRequest from a dict
organization_custom_role_update_request_form_dict = organization_custom_role_update_request.from_dict(organization_custom_role_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


