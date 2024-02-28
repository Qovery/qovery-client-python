# ServiceResponseList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Service]**](Service.md) |  | [optional] 

## Example

```python
from qovery.models.service_response_list import ServiceResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceResponseList from a JSON string
service_response_list_instance = ServiceResponseList.from_json(json)
# print the JSON string representation of the object
print ServiceResponseList.to_json()

# convert the object into a dict
service_response_list_dict = service_response_list_instance.to_dict()
# create an instance of ServiceResponseList from a dict
service_response_list_form_dict = service_response_list.from_dict(service_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


