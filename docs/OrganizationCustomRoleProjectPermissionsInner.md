# OrganizationCustomRoleProjectPermissionsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | [optional] 
**project_name** | **str** |  | [optional] 
**is_admin** | **bool** | If &#x60;is_admin&#x60; is &#x60;true&#x60;, the user is: - automatically &#x60;MANAGER&#x60; for each environment type - allowed to manage project deployment rules - able to delete the project    Note that &#x60;permissions&#x60; can then be ignored for this project  | [optional] [default to False]
**permissions** | [**List[OrganizationCustomRoleUpdateRequestProjectPermissionsInnerPermissionsInner]**](OrganizationCustomRoleUpdateRequestProjectPermissionsInnerPermissionsInner.md) |  | [optional] 

## Example

```python
from qovery.models.organization_custom_role_project_permissions_inner import OrganizationCustomRoleProjectPermissionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationCustomRoleProjectPermissionsInner from a JSON string
organization_custom_role_project_permissions_inner_instance = OrganizationCustomRoleProjectPermissionsInner.from_json(json)
# print the JSON string representation of the object
print OrganizationCustomRoleProjectPermissionsInner.to_json()

# convert the object into a dict
organization_custom_role_project_permissions_inner_dict = organization_custom_role_project_permissions_inner_instance.to_dict()
# create an instance of OrganizationCustomRoleProjectPermissionsInner from a dict
organization_custom_role_project_permissions_inner_form_dict = organization_custom_role_project_permissions_inner.from_dict(organization_custom_role_project_permissions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


