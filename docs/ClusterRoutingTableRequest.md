# ClusterRoutingTableRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**routes** | [**List[ClusterRoutingTableResultsInner]**](ClusterRoutingTableResultsInner.md) |  | 

## Example

```python
from qovery.models.cluster_routing_table_request import ClusterRoutingTableRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterRoutingTableRequest from a JSON string
cluster_routing_table_request_instance = ClusterRoutingTableRequest.from_json(json)
# print the JSON string representation of the object
print ClusterRoutingTableRequest.to_json()

# convert the object into a dict
cluster_routing_table_request_dict = cluster_routing_table_request_instance.to_dict()
# create an instance of ClusterRoutingTableRequest from a dict
cluster_routing_table_request_form_dict = cluster_routing_table_request.from_dict(cluster_routing_table_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


