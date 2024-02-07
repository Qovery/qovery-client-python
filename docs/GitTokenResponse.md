# GitTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**type** | [**GitProviderEnum**](GitProviderEnum.md) |  | 
**expired_at** | **date** |  | [optional] 
**workspace** | **str** | Mandatory only for BITBUCKET git provider | [optional] 
**associated_services_count** | **float** | The number of services using this git token | 

## Example

```python
from qovery.models.git_token_response import GitTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GitTokenResponse from a JSON string
git_token_response_instance = GitTokenResponse.from_json(json)
# print the JSON string representation of the object
print GitTokenResponse.to_json()

# convert the object into a dict
git_token_response_dict = git_token_response_instance.to_dict()
# create an instance of GitTokenResponse from a dict
git_token_response_form_dict = git_token_response.from_dict(git_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


