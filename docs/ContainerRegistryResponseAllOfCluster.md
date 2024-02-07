# ContainerRegistryResponseAllOfCluster


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the cluster of which the registry belongs to | 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**name** | **str** | Name of the cluster of which the registry belongs to | [optional] 

## Example

```python
from qovery.models.container_registry_response_all_of_cluster import ContainerRegistryResponseAllOfCluster

# TODO update the JSON string below
json = "{}"
# create an instance of ContainerRegistryResponseAllOfCluster from a JSON string
container_registry_response_all_of_cluster_instance = ContainerRegistryResponseAllOfCluster.from_json(json)
# print the JSON string representation of the object
print ContainerRegistryResponseAllOfCluster.to_json()

# convert the object into a dict
container_registry_response_all_of_cluster_dict = container_registry_response_all_of_cluster_instance.to_dict()
# create an instance of ContainerRegistryResponseAllOfCluster from a dict
container_registry_response_all_of_cluster_form_dict = container_registry_response_all_of_cluster.from_dict(container_registry_response_all_of_cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


