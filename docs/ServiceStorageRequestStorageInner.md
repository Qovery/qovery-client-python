# ServiceStorageRequestStorageInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | [**StorageTypeEnum**](StorageTypeEnum.md) |  | 
**size** | **int** | unit is GB Minimum size is 4 GB  | 
**mount_point** | **str** |  | 

## Example

```python
from qovery.models.service_storage_request_storage_inner import ServiceStorageRequestStorageInner

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceStorageRequestStorageInner from a JSON string
service_storage_request_storage_inner_instance = ServiceStorageRequestStorageInner.from_json(json)
# print the JSON string representation of the object
print ServiceStorageRequestStorageInner.to_json()

# convert the object into a dict
service_storage_request_storage_inner_dict = service_storage_request_storage_inner_instance.to_dict()
# create an instance of ServiceStorageRequestStorageInner from a dict
service_storage_request_storage_inner_form_dict = service_storage_request_storage_inner.from_dict(service_storage_request_storage_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


