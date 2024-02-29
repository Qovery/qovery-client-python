# ClusterRegionResponseList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ClusterRegion]**](ClusterRegion.md) |  | [optional] 

## Example

```python
from qovery.models.cluster_region_response_list import ClusterRegionResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterRegionResponseList from a JSON string
cluster_region_response_list_instance = ClusterRegionResponseList.from_json(json)
# print the JSON string representation of the object
print ClusterRegionResponseList.to_json()

# convert the object into a dict
cluster_region_response_list_dict = cluster_region_response_list_instance.to_dict()
# create an instance of ClusterRegionResponseList from a dict
cluster_region_response_list_form_dict = cluster_region_response_list.from_dict(cluster_region_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


