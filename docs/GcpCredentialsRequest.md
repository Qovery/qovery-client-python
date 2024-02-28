# GcpCredentialsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**gcp_credentials** | **str** |  | 

## Example

```python
from qovery.models.gcp_credentials_request import GcpCredentialsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GcpCredentialsRequest from a JSON string
gcp_credentials_request_instance = GcpCredentialsRequest.from_json(json)
# print the JSON string representation of the object
print GcpCredentialsRequest.to_json()

# convert the object into a dict
gcp_credentials_request_dict = gcp_credentials_request_instance.to_dict()
# create an instance of GcpCredentialsRequest from a dict
gcp_credentials_request_form_dict = gcp_credentials_request.from_dict(gcp_credentials_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


