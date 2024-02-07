# CommitPaginatedResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **float** |  | 
**page_size** | **float** |  | 
**results** | [**List[Commit]**](Commit.md) |  | [optional] 

## Example

```python
from qovery.models.commit_paginated_response_list import CommitPaginatedResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of CommitPaginatedResponseList from a JSON string
commit_paginated_response_list_instance = CommitPaginatedResponseList.from_json(json)
# print the JSON string representation of the object
print CommitPaginatedResponseList.to_json()

# convert the object into a dict
commit_paginated_response_list_dict = commit_paginated_response_list_instance.to_dict()
# create an instance of CommitPaginatedResponseList from a dict
commit_paginated_response_list_form_dict = commit_paginated_response_list.from_dict(commit_paginated_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


