# OrganizationCustomRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**cluster_permissions** | [**List[OrganizationCustomRoleClusterPermissionsInner]**](OrganizationCustomRoleClusterPermissionsInner.md) |  | [optional] 
**project_permissions** | [**List[OrganizationCustomRoleProjectPermissionsInner]**](OrganizationCustomRoleProjectPermissionsInner.md) |  | [optional] 

## Example

```python
from qovery.models.organization_custom_role import OrganizationCustomRole

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationCustomRole from a JSON string
organization_custom_role_instance = OrganizationCustomRole.from_json(json)
# print the JSON string representation of the object
print OrganizationCustomRole.to_json()

# convert the object into a dict
organization_custom_role_dict = organization_custom_role_instance.to_dict()
# create an instance of OrganizationCustomRole from a dict
organization_custom_role_form_dict = organization_custom_role.from_dict(organization_custom_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


