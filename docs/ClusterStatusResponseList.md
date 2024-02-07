# ClusterStatusResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ClusterStatusGet]**](ClusterStatusGet.md) |  | [optional] 

## Example

```python
from qovery.models.cluster_status_response_list import ClusterStatusResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterStatusResponseList from a JSON string
cluster_status_response_list_instance = ClusterStatusResponseList.from_json(json)
# print the JSON string representation of the object
print ClusterStatusResponseList.to_json()

# convert the object into a dict
cluster_status_response_list_dict = cluster_status_response_list_instance.to_dict()
# create an instance of ClusterStatusResponseList from a dict
cluster_status_response_list_form_dict = cluster_status_response_list.from_dict(cluster_status_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


