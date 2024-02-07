# CommitResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Commit]**](Commit.md) |  | [optional] 

## Example

```python
from qovery.models.commit_response_list import CommitResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of CommitResponseList from a JSON string
commit_response_list_instance = CommitResponseList.from_json(json)
# print the JSON string representation of the object
print CommitResponseList.to_json()

# convert the object into a dict
commit_response_list_dict = commit_response_list_instance.to_dict()
# create an instance of CommitResponseList from a dict
commit_response_list_form_dict = commit_response_list.from_dict(commit_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


