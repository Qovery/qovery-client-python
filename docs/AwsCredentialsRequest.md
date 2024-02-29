# AwsCredentialsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**access_key_id** | **str** |  | 
**secret_access_key** | **str** |  | 

## Example

```python
from qovery.models.aws_credentials_request import AwsCredentialsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AwsCredentialsRequest from a JSON string
aws_credentials_request_instance = AwsCredentialsRequest.from_json(json)
# print the JSON string representation of the object
print AwsCredentialsRequest.to_json()

# convert the object into a dict
aws_credentials_request_dict = aws_credentials_request_instance.to_dict()
# create an instance of AwsCredentialsRequest from a dict
aws_credentials_request_form_dict = aws_credentials_request.from_dict(aws_credentials_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


