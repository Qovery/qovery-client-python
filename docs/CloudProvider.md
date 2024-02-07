# CloudProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**short_name** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**logo_url** | **str** |  | [optional] 
**regions** | [**List[ClusterRegion]**](ClusterRegion.md) |  | [optional] 

## Example

```python
from qovery.models.cloud_provider import CloudProvider

# TODO update the JSON string below
json = "{}"
# create an instance of CloudProvider from a JSON string
cloud_provider_instance = CloudProvider.from_json(json)
# print the JSON string representation of the object
print CloudProvider.to_json()

# convert the object into a dict
cloud_provider_dict = cloud_provider_instance.to_dict()
# create an instance of CloudProvider from a dict
cloud_provider_form_dict = cloud_provider.from_dict(cloud_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


