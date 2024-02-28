# ClusterRegion


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**country_code** | **str** |  | 
**country** | **str** |  | 
**city** | **str** |  | 

## Example

```python
from qovery.models.cluster_region import ClusterRegion

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterRegion from a JSON string
cluster_region_instance = ClusterRegion.from_json(json)
# print the JSON string representation of the object
print ClusterRegion.to_json()

# convert the object into a dict
cluster_region_dict = cluster_region_instance.to_dict()
# create an instance of ClusterRegion from a dict
cluster_region_form_dict = cluster_region.from_dict(cluster_region_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


