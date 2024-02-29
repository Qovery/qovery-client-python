# Commit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**git_commit_id** | **str** |  | 
**tag** | **str** |  | 
**message** | **str** |  | 
**author_name** | **str** |  | 
**author_avatar_url** | **str** |  | [optional] 
**commit_page_url** | **str** |  | [optional] 

## Example

```python
from qovery.models.commit import Commit

# TODO update the JSON string below
json = "{}"
# create an instance of Commit from a JSON string
commit_instance = Commit.from_json(json)
# print the JSON string representation of the object
print Commit.to_json()

# convert the object into a dict
commit_dict = commit_instance.to_dict()
# create an instance of Commit from a dict
commit_form_dict = commit.from_dict(commit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


