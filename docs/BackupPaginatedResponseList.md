# BackupPaginatedResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **float** |  | 
**page_size** | **float** |  | 
**results** | [**List[Backup]**](Backup.md) |  | [optional] 

## Example

```python
from qovery.models.backup_paginated_response_list import BackupPaginatedResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of BackupPaginatedResponseList from a JSON string
backup_paginated_response_list_instance = BackupPaginatedResponseList.from_json(json)
# print the JSON string representation of the object
print BackupPaginatedResponseList.to_json()

# convert the object into a dict
backup_paginated_response_list_dict = backup_paginated_response_list_instance.to_dict()
# create an instance of BackupPaginatedResponseList from a dict
backup_paginated_response_list_form_dict = backup_paginated_response_list.from_dict(backup_paginated_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


