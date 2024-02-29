# UserResponseList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[User]**](User.md) |  | [optional] 

## Example

```python
from qovery.models.user_response_list import UserResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of UserResponseList from a JSON string
user_response_list_instance = UserResponseList.from_json(json)
# print the JSON string representation of the object
print UserResponseList.to_json()

# convert the object into a dict
user_response_list_dict = user_response_list_instance.to_dict()
# create an instance of UserResponseList from a dict
user_response_list_form_dict = user_response_list.from_dict(user_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


