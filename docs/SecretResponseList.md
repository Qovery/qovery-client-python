# SecretResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Secret]**](Secret.md) |  | [optional] 

## Example

```python
from qovery.models.secret_response_list import SecretResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of SecretResponseList from a JSON string
secret_response_list_instance = SecretResponseList.from_json(json)
# print the JSON string representation of the object
print SecretResponseList.to_json()

# convert the object into a dict
secret_response_list_dict = secret_response_list_instance.to_dict()
# create an instance of SecretResponseList from a dict
secret_response_list_form_dict = secret_response_list.from_dict(secret_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


