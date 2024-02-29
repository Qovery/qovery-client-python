# ServiceStorageStorageInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**type** | [**StorageTypeEnum**](StorageTypeEnum.md) |  | 
**size** | **int** | unit is GB | 
**mount_point** | **str** |  | 

## Example

```python
from qovery.models.service_storage_storage_inner import ServiceStorageStorageInner

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceStorageStorageInner from a JSON string
service_storage_storage_inner_instance = ServiceStorageStorageInner.from_json(json)
# print the JSON string representation of the object
print ServiceStorageStorageInner.to_json()

# convert the object into a dict
service_storage_storage_inner_dict = service_storage_storage_inner_instance.to_dict()
# create an instance of ServiceStorageStorageInner from a dict
service_storage_storage_inner_form_dict = service_storage_storage_inner.from_dict(service_storage_storage_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


