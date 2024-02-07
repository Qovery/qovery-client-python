# OrganizationCustomRoleUpdateRequestClusterPermissionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** |  | [optional] 
**permission** | [**OrganizationCustomRoleClusterPermission**](OrganizationCustomRoleClusterPermission.md) |  | [optional] 

## Example

```python
from qovery.models.organization_custom_role_update_request_cluster_permissions_inner import OrganizationCustomRoleUpdateRequestClusterPermissionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationCustomRoleUpdateRequestClusterPermissionsInner from a JSON string
organization_custom_role_update_request_cluster_permissions_inner_instance = OrganizationCustomRoleUpdateRequestClusterPermissionsInner.from_json(json)
# print the JSON string representation of the object
print OrganizationCustomRoleUpdateRequestClusterPermissionsInner.to_json()

# convert the object into a dict
organization_custom_role_update_request_cluster_permissions_inner_dict = organization_custom_role_update_request_cluster_permissions_inner_instance.to_dict()
# create an instance of OrganizationCustomRoleUpdateRequestClusterPermissionsInner from a dict
organization_custom_role_update_request_cluster_permissions_inner_form_dict = organization_custom_role_update_request_cluster_permissions_inner.from_dict(organization_custom_role_update_request_cluster_permissions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


