# MemberResponseList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Member]**](Member.md) |  | [optional] 

## Example

```python
from qovery.models.member_response_list import MemberResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of MemberResponseList from a JSON string
member_response_list_instance = MemberResponseList.from_json(json)
# print the JSON string representation of the object
print MemberResponseList.to_json()

# convert the object into a dict
member_response_list_dict = member_response_list_instance.to_dict()
# create an instance of MemberResponseList from a dict
member_response_list_form_dict = member_response_list.from_dict(member_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


