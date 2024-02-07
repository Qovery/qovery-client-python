# ServiceStorage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage** | [**List[ServiceStorageStorageInner]**](ServiceStorageStorageInner.md) |  | [optional] 

## Example

```python
from qovery.models.service_storage import ServiceStorage

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceStorage from a JSON string
service_storage_instance = ServiceStorage.from_json(json)
# print the JSON string representation of the object
print ServiceStorage.to_json()

# convert the object into a dict
service_storage_dict = service_storage_instance.to_dict()
# create an instance of ServiceStorage from a dict
service_storage_form_dict = service_storage.from_dict(service_storage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


