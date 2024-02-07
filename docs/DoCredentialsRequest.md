# DoCredentialsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**token** | **str** |  | [optional] 
**spaces_access_id** | **str** |  | [optional] 
**spaces_secret_key** | **str** |  | [optional] 

## Example

```python
from qovery.models.do_credentials_request import DoCredentialsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DoCredentialsRequest from a JSON string
do_credentials_request_instance = DoCredentialsRequest.from_json(json)
# print the JSON string representation of the object
print DoCredentialsRequest.to_json()

# convert the object into a dict
do_credentials_request_dict = do_credentials_request_instance.to_dict()
# create an instance of DoCredentialsRequest from a dict
do_credentials_request_form_dict = do_credentials_request.from_dict(do_credentials_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


