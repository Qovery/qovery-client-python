# ClusterStatusGet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** |  | [optional] 
**status** | [**ClusterStateEnum**](ClusterStateEnum.md) |  | [optional] 
**is_deployed** | **bool** |  | [optional] 
**last_execution_id** | **str** |  | [optional] 

## Example

```python
from qovery.models.cluster_status_get import ClusterStatusGet

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterStatusGet from a JSON string
cluster_status_get_instance = ClusterStatusGet.from_json(json)
# print the JSON string representation of the object
print ClusterStatusGet.to_json()

# convert the object into a dict
cluster_status_get_dict = cluster_status_get_instance.to_dict()
# create an instance of ClusterStatusGet from a dict
cluster_status_get_form_dict = cluster_status_get.from_dict(cluster_status_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


