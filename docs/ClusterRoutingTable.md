# ClusterRoutingTable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ClusterRoutingTableResultsInner]**](ClusterRoutingTableResultsInner.md) |  | [optional] 

## Example

```python
from qovery.models.cluster_routing_table import ClusterRoutingTable

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterRoutingTable from a JSON string
cluster_routing_table_instance = ClusterRoutingTable.from_json(json)
# print the JSON string representation of the object
print ClusterRoutingTable.to_json()

# convert the object into a dict
cluster_routing_table_dict = cluster_routing_table_instance.to_dict()
# create an instance of ClusterRoutingTable from a dict
cluster_routing_table_form_dict = cluster_routing_table.from_dict(cluster_routing_table_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


