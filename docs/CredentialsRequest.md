# CredentialsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from qovery.models.credentials_request import CredentialsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialsRequest from a JSON string
credentials_request_instance = CredentialsRequest.from_json(json)
# print the JSON string representation of the object
print CredentialsRequest.to_json()

# convert the object into a dict
credentials_request_dict = credentials_request_instance.to_dict()
# create an instance of CredentialsRequest from a dict
credentials_request_form_dict = credentials_request.from_dict(credentials_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


