# SecretRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | key is case sensitive | 
**value** | **str** | value of the secret. Clear value will never be returned | [optional] 
**mount_path** | **str** | should be set for file only. variable mount path make secret a file (where file should be mounted). | [optional] 

## Example

```python
from qovery.models.secret_request import SecretRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SecretRequest from a JSON string
secret_request_instance = SecretRequest.from_json(json)
# print the JSON string representation of the object
print SecretRequest.to_json()

# convert the object into a dict
secret_request_dict = secret_request_instance.to_dict()
# create an instance of SecretRequest from a dict
secret_request_form_dict = secret_request.from_dict(secret_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


