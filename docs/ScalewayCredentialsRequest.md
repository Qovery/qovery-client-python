# ScalewayCredentialsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**scaleway_access_key** | **str** |  | 
**scaleway_secret_key** | **str** |  | 
**scaleway_project_id** | **str** |  | 
**scaleway_organization_id** | **str** |  | 

## Example

```python
from qovery.models.scaleway_credentials_request import ScalewayCredentialsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ScalewayCredentialsRequest from a JSON string
scaleway_credentials_request_instance = ScalewayCredentialsRequest.from_json(json)
# print the JSON string representation of the object
print ScalewayCredentialsRequest.to_json()

# convert the object into a dict
scaleway_credentials_request_dict = scaleway_credentials_request_instance.to_dict()
# create an instance of ScalewayCredentialsRequest from a dict
scaleway_credentials_request_form_dict = scaleway_credentials_request.from_dict(scaleway_credentials_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


