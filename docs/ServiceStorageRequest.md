# ServiceStorageRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage** | [**List[ServiceStorageRequestStorageInner]**](ServiceStorageRequestStorageInner.md) |  | [optional] 

## Example

```python
from qovery.models.service_storage_request import ServiceStorageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceStorageRequest from a JSON string
service_storage_request_instance = ServiceStorageRequest.from_json(json)
# print the JSON string representation of the object
print ServiceStorageRequest.to_json()

# convert the object into a dict
service_storage_request_dict = service_storage_request_instance.to_dict()
# create an instance of ServiceStorageRequest from a dict
service_storage_request_form_dict = service_storage_request.from_dict(service_storage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


