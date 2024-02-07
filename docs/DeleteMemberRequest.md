# DeleteMemberRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 

## Example

```python
from qovery.models.delete_member_request import DeleteMemberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteMemberRequest from a JSON string
delete_member_request_instance = DeleteMemberRequest.from_json(json)
# print the JSON string representation of the object
print DeleteMemberRequest.to_json()

# convert the object into a dict
delete_member_request_dict = delete_member_request_instance.to_dict()
# create an instance of DeleteMemberRequest from a dict
delete_member_request_form_dict = delete_member_request.from_dict(delete_member_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


