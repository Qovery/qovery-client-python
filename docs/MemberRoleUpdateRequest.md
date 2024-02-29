# MemberRoleUpdateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | specify the git provider user id | 
**role_id** | **str** |  | 

## Example

```python
from qovery.models.member_role_update_request import MemberRoleUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MemberRoleUpdateRequest from a JSON string
member_role_update_request_instance = MemberRoleUpdateRequest.from_json(json)
# print the JSON string representation of the object
print MemberRoleUpdateRequest.to_json()

# convert the object into a dict
member_role_update_request_dict = member_role_update_request_instance.to_dict()
# create an instance of MemberRoleUpdateRequest from a dict
member_role_update_request_form_dict = member_role_update_request.from_dict(member_role_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


