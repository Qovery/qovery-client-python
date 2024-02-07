# AccountInfoEditRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**communication_email** | **str** | The email to be used for official Qovery communications | [optional] 

## Example

```python
from qovery.models.account_info_edit_request import AccountInfoEditRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AccountInfoEditRequest from a JSON string
account_info_edit_request_instance = AccountInfoEditRequest.from_json(json)
# print the JSON string representation of the object
print AccountInfoEditRequest.to_json()

# convert the object into a dict
account_info_edit_request_dict = account_info_edit_request_instance.to_dict()
# create an instance of AccountInfoEditRequest from a dict
account_info_edit_request_form_dict = account_info_edit_request.from_dict(account_info_edit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


