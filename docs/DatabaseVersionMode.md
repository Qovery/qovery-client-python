# DatabaseVersionMode


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**supported_mode** | [**DatabaseModeEnum**](DatabaseModeEnum.md) |  | [optional] 

## Example

```python
from qovery.models.database_version_mode import DatabaseVersionMode

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseVersionMode from a JSON string
database_version_mode_instance = DatabaseVersionMode.from_json(json)
# print the JSON string representation of the object
print DatabaseVersionMode.to_json()

# convert the object into a dict
database_version_mode_dict = database_version_mode_instance.to_dict()
# create an instance of DatabaseVersionMode from a dict
database_version_mode_form_dict = database_version_mode.from_dict(database_version_mode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


