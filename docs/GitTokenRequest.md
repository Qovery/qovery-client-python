# GitTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**type** | [**GitProviderEnum**](GitProviderEnum.md) |  | 
**token** | **str** | The token from your git provider side | 
**workspace** | **str** | Mandatory only for BITBUCKET git provider, to allow us to fetch repositories at creation/edition of a service | [optional] 

## Example

```python
from qovery.models.git_token_request import GitTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GitTokenRequest from a JSON string
git_token_request_instance = GitTokenRequest.from_json(json)
# print the JSON string representation of the object
print GitTokenRequest.to_json()

# convert the object into a dict
git_token_request_dict = git_token_request_instance.to_dict()
# create an instance of GitTokenRequest from a dict
git_token_request_form_dict = git_token_request.from_dict(git_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


