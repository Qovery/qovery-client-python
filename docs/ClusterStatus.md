# ClusterStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** |  | [optional] 
**status** | [**ClusterStateEnum**](ClusterStateEnum.md) |  | [optional] 
**is_deployed** | **bool** |  | [optional] 

## Example

```python
from qovery.models.cluster_status import ClusterStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterStatus from a JSON string
cluster_status_instance = ClusterStatus.from_json(json)
# print the JSON string representation of the object
print ClusterStatus.to_json()

# convert the object into a dict
cluster_status_dict = cluster_status_instance.to_dict()
# create an instance of ClusterStatus from a dict
cluster_status_form_dict = cluster_status.from_dict(cluster_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


