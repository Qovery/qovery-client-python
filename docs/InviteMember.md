# InviteMember


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**email** | **str** |  | 
**role** | [**InviteMemberRoleEnum**](InviteMemberRoleEnum.md) |  | 
**invitation_link** | **str** |  | 
**invitation_status** | [**InviteStatusEnum**](InviteStatusEnum.md) |  | 
**organization_name** | **str** |  | [optional] 
**inviter** | **str** |  | 
**logo_url** | **str** |  | [optional] 
**role_id** | **str** |  | [optional] 
**role_name** | **str** |  | [optional] 

## Example

```python
from qovery.models.invite_member import InviteMember

# TODO update the JSON string below
json = "{}"
# create an instance of InviteMember from a JSON string
invite_member_instance = InviteMember.from_json(json)
# print the JSON string representation of the object
print InviteMember.to_json()

# convert the object into a dict
invite_member_dict = invite_member_instance.to_dict()
# create an instance of InviteMember from a dict
invite_member_form_dict = invite_member.from_dict(invite_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


