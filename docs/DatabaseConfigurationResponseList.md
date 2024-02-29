# DatabaseConfigurationResponseList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[DatabaseConfiguration]**](DatabaseConfiguration.md) |  | [optional] 

## Example

```python
from qovery.models.database_configuration_response_list import DatabaseConfigurationResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseConfigurationResponseList from a JSON string
database_configuration_response_list_instance = DatabaseConfigurationResponseList.from_json(json)
# print the JSON string representation of the object
print DatabaseConfigurationResponseList.to_json()

# convert the object into a dict
database_configuration_response_list_dict = database_configuration_response_list_instance.to_dict()
# create an instance of DatabaseConfigurationResponseList from a dict
database_configuration_response_list_form_dict = database_configuration_response_list.from_dict(database_configuration_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


