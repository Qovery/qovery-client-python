# DatabaseConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database_type** | [**DatabaseTypeEnum**](DatabaseTypeEnum.md) |  | [optional] 
**version** | [**List[DatabaseVersionMode]**](DatabaseVersionMode.md) |  | [optional] 

## Example

```python
from qovery.models.database_configuration import DatabaseConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseConfiguration from a JSON string
database_configuration_instance = DatabaseConfiguration.from_json(json)
# print the JSON string representation of the object
print DatabaseConfiguration.to_json()

# convert the object into a dict
database_configuration_dict = database_configuration_instance.to_dict()
# create an instance of DatabaseConfiguration from a dict
database_configuration_form_dict = database_configuration.from_dict(database_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


