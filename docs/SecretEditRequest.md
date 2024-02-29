# SecretEditRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** |  | [optional] 
**key** | **str** |  | 

## Example

```python
from qovery.models.secret_edit_request import SecretEditRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SecretEditRequest from a JSON string
secret_edit_request_instance = SecretEditRequest.from_json(json)
# print the JSON string representation of the object
print SecretEditRequest.to_json()

# convert the object into a dict
secret_edit_request_dict = secret_edit_request_instance.to_dict()
# create an instance of SecretEditRequest from a dict
secret_edit_request_form_dict = secret_edit_request.from_dict(secret_edit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


