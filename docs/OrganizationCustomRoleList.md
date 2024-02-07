# OrganizationCustomRoleList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[OrganizationCustomRole]**](OrganizationCustomRole.md) |  | [optional] 

## Example

```python
from qovery.models.organization_custom_role_list import OrganizationCustomRoleList

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationCustomRoleList from a JSON string
organization_custom_role_list_instance = OrganizationCustomRoleList.from_json(json)
# print the JSON string representation of the object
print OrganizationCustomRoleList.to_json()

# convert the object into a dict
organization_custom_role_list_dict = organization_custom_role_list_instance.to_dict()
# create an instance of OrganizationCustomRoleList from a dict
organization_custom_role_list_form_dict = organization_custom_role_list.from_dict(organization_custom_role_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


