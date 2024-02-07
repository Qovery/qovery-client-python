# BackupResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Backup]**](Backup.md) |  | [optional] 

## Example

```python
from qovery.models.backup_response_list import BackupResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of BackupResponseList from a JSON string
backup_response_list_instance = BackupResponseList.from_json(json)
# print the JSON string representation of the object
print BackupResponseList.to_json()

# convert the object into a dict
backup_response_list_dict = backup_response_list_instance.to_dict()
# create an instance of BackupResponseList from a dict
backup_response_list_form_dict = backup_response_list.from_dict(backup_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


