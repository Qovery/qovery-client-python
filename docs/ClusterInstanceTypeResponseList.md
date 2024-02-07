# ClusterInstanceTypeResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ClusterInstanceTypeResponseListResultsInner]**](ClusterInstanceTypeResponseListResultsInner.md) |  | [optional] 

## Example

```python
from qovery.models.cluster_instance_type_response_list import ClusterInstanceTypeResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterInstanceTypeResponseList from a JSON string
cluster_instance_type_response_list_instance = ClusterInstanceTypeResponseList.from_json(json)
# print the JSON string representation of the object
print ClusterInstanceTypeResponseList.to_json()

# convert the object into a dict
cluster_instance_type_response_list_dict = cluster_instance_type_response_list_instance.to_dict()
# create an instance of ClusterInstanceTypeResponseList from a dict
cluster_instance_type_response_list_form_dict = cluster_instance_type_response_list.from_dict(cluster_instance_type_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


