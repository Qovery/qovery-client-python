# ClusterResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Cluster]**](Cluster.md) |  | [optional] 

## Example

```python
from qovery.models.cluster_response_list import ClusterResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterResponseList from a JSON string
cluster_response_list_instance = ClusterResponseList.from_json(json)
# print the JSON string representation of the object
print ClusterResponseList.to_json()

# convert the object into a dict
cluster_response_list_dict = cluster_response_list_instance.to_dict()
# create an instance of ClusterResponseList from a dict
cluster_response_list_form_dict = cluster_response_list.from_dict(cluster_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


