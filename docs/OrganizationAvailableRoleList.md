# OrganizationAvailableRoleList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[OrganizationAvailableRole]**](OrganizationAvailableRole.md) |  | [optional] 

## Example

```python
from qovery.models.organization_available_role_list import OrganizationAvailableRoleList

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationAvailableRoleList from a JSON string
organization_available_role_list_instance = OrganizationAvailableRoleList.from_json(json)
# print the JSON string representation of the object
print OrganizationAvailableRoleList.to_json()

# convert the object into a dict
organization_available_role_list_dict = organization_available_role_list_instance.to_dict()
# create an instance of OrganizationAvailableRoleList from a dict
organization_available_role_list_form_dict = organization_available_role_list.from_dict(organization_available_role_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


