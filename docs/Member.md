# Member


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**nickname** | **str** |  | [optional] 
**email** | **str** |  | 
**profile_picture_url** | **str** |  | [optional] 
**last_activity_at** | **datetime** | last time the user was connected | [optional] 
**role** | [**InviteMemberRoleEnum**](InviteMemberRoleEnum.md) |  | [optional] 
**role_name** | **str** | the role linked to the user | [optional] 
**role_id** | **str** |  | [optional] 

## Example

```python
from qovery.models.member import Member

# TODO update the JSON string below
json = "{}"
# create an instance of Member from a JSON string
member_instance = Member.from_json(json)
# print the JSON string representation of the object
print Member.to_json()

# convert the object into a dict
member_dict = member_instance.to_dict()
# create an instance of Member from a dict
member_form_dict = member.from_dict(member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


