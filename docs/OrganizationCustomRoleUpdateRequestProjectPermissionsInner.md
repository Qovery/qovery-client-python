# OrganizationCustomRoleUpdateRequestProjectPermissionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | [optional] 
**is_admin** | **bool** | If &#x60;is_admin&#x60; is &#x60;true&#x60;, the user is: - automatically &#x60;MANAGER&#x60; for each environment type - allowed to manage project deployment rules - able to delete the project    Note that &#x60;permissions&#x60; can then be ignored for this project  | [optional] [default to False]
**permissions** | [**List[OrganizationCustomRoleUpdateRequestProjectPermissionsInnerPermissionsInner]**](OrganizationCustomRoleUpdateRequestProjectPermissionsInnerPermissionsInner.md) | Mandatory if &#x60;is_admin&#x60; is &#x60;false&#x60;   Should contain an entry for every environment type: - &#x60;DEVELOPMENT&#x60; - &#x60;PREVIEW&#x60; - &#x60;STAGING&#x60; - &#x60;PRODUCTION&#x60;  | [optional] 

## Example

```python
from qovery.models.organization_custom_role_update_request_project_permissions_inner import OrganizationCustomRoleUpdateRequestProjectPermissionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationCustomRoleUpdateRequestProjectPermissionsInner from a JSON string
organization_custom_role_update_request_project_permissions_inner_instance = OrganizationCustomRoleUpdateRequestProjectPermissionsInner.from_json(json)
# print the JSON string representation of the object
print OrganizationCustomRoleUpdateRequestProjectPermissionsInner.to_json()

# convert the object into a dict
organization_custom_role_update_request_project_permissions_inner_dict = organization_custom_role_update_request_project_permissions_inner_instance.to_dict()
# create an instance of OrganizationCustomRoleUpdateRequestProjectPermissionsInner from a dict
organization_custom_role_update_request_project_permissions_inner_form_dict = organization_custom_role_update_request_project_permissions_inner.from_dict(organization_custom_role_update_request_project_permissions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


