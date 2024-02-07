# DatabaseResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Database]**](Database.md) |  | [optional] 

## Example

```python
from qovery.models.database_response_list import DatabaseResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseResponseList from a JSON string
database_response_list_instance = DatabaseResponseList.from_json(json)
# print the JSON string representation of the object
print DatabaseResponseList.to_json()

# convert the object into a dict
database_response_list_dict = database_response_list_instance.to_dict()
# create an instance of DatabaseResponseList from a dict
database_response_list_form_dict = database_response_list.from_dict(database_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


