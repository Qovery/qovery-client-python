# GitTokenResponseList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[GitTokenResponse]**](GitTokenResponse.md) |  | [optional] 

## Example

```python
from qovery.models.git_token_response_list import GitTokenResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of GitTokenResponseList from a JSON string
git_token_response_list_instance = GitTokenResponseList.from_json(json)
# print the JSON string representation of the object
print GitTokenResponseList.to_json()

# convert the object into a dict
git_token_response_list_dict = git_token_response_list_instance.to_dict()
# create an instance of GitTokenResponseList from a dict
git_token_response_list_form_dict = git_token_response_list.from_dict(git_token_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


