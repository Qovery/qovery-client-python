# InviteMemberResponseList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[InviteMember]**](InviteMember.md) |  | [optional] 

## Example

```python
from qovery.models.invite_member_response_list import InviteMemberResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of InviteMemberResponseList from a JSON string
invite_member_response_list_instance = InviteMemberResponseList.from_json(json)
# print the JSON string representation of the object
print InviteMemberResponseList.to_json()

# convert the object into a dict
invite_member_response_list_dict = invite_member_response_list_instance.to_dict()
# create an instance of InviteMemberResponseList from a dict
invite_member_response_list_form_dict = invite_member_response_list.from_dict(invite_member_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


