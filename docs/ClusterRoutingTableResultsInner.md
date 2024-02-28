# ClusterRoutingTableResultsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination** | **str** |  | 
**target** | **str** |  | 
**description** | **str** |  | 

## Example

```python
from qovery.models.cluster_routing_table_results_inner import ClusterRoutingTableResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterRoutingTableResultsInner from a JSON string
cluster_routing_table_results_inner_instance = ClusterRoutingTableResultsInner.from_json(json)
# print the JSON string representation of the object
print ClusterRoutingTableResultsInner.to_json()

# convert the object into a dict
cluster_routing_table_results_inner_dict = cluster_routing_table_results_inner_instance.to_dict()
# create an instance of ClusterRoutingTableResultsInner from a dict
cluster_routing_table_results_inner_form_dict = cluster_routing_table_results_inner.from_dict(cluster_routing_table_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


