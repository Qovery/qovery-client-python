# ClusterInstanceTypeResponseListResultsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**name** | **str** |  | 
**cpu** | **int** |  | 
**ram_in_gb** | **int** |  | 
**bandwidth_in_gbps** | **str** |  | 
**bandwidth_guarantee** | **str** |  | 
**architecture** | **str** |  | [optional] 

## Example

```python
from qovery.models.cluster_instance_type_response_list_results_inner import ClusterInstanceTypeResponseListResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterInstanceTypeResponseListResultsInner from a JSON string
cluster_instance_type_response_list_results_inner_instance = ClusterInstanceTypeResponseListResultsInner.from_json(json)
# print the JSON string representation of the object
print ClusterInstanceTypeResponseListResultsInner.to_json()

# convert the object into a dict
cluster_instance_type_response_list_results_inner_dict = cluster_instance_type_response_list_results_inner_instance.to_dict()
# create an instance of ClusterInstanceTypeResponseListResultsInner from a dict
cluster_instance_type_response_list_results_inner_form_dict = cluster_instance_type_response_list_results_inner.from_dict(cluster_instance_type_response_list_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


