# OrganizationCustomRoleUpdateRequestProjectPermissionsInnerPermissionsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment_type** | [**EnvironmentModeEnum**](EnvironmentModeEnum.md) |  | [optional] 
**permission** | [**OrganizationCustomRoleProjectPermission**](OrganizationCustomRoleProjectPermission.md) |  | [optional] 

## Example

```python
from qovery.models.organization_custom_role_update_request_project_permissions_inner_permissions_inner import OrganizationCustomRoleUpdateRequestProjectPermissionsInnerPermissionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationCustomRoleUpdateRequestProjectPermissionsInnerPermissionsInner from a JSON string
organization_custom_role_update_request_project_permissions_inner_permissions_inner_instance = OrganizationCustomRoleUpdateRequestProjectPermissionsInnerPermissionsInner.from_json(json)
# print the JSON string representation of the object
print OrganizationCustomRoleUpdateRequestProjectPermissionsInnerPermissionsInner.to_json()

# convert the object into a dict
organization_custom_role_update_request_project_permissions_inner_permissions_inner_dict = organization_custom_role_update_request_project_permissions_inner_permissions_inner_instance.to_dict()
# create an instance of OrganizationCustomRoleUpdateRequestProjectPermissionsInnerPermissionsInner from a dict
organization_custom_role_update_request_project_permissions_inner_permissions_inner_form_dict = organization_custom_role_update_request_project_permissions_inner_permissions_inner.from_dict(organization_custom_role_update_request_project_permissions_inner_permissions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


