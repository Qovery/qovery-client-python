# Cluster


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**organization** | [**ReferenceObject**](ReferenceObject.md) |  | 
**name** | **str** | name is case-insensitive | 
**description** | **str** |  | [optional] 
**region** | **str** |  | 
**cloud_provider** | [**CloudProviderEnum**](CloudProviderEnum.md) |  | 
**min_running_nodes** | **int** |  | [optional] [default to 1]
**max_running_nodes** | **int** |  | [optional] [default to 1]
**disk_size** | **int** | Unit is in GB. The disk size to be used for the node configuration | [optional] [default to 20]
**instance_type** | **str** | the instance type to be used for this cluster. The list of values can be retrieved via the endpoint /{CloudProvider}/instanceType | [optional] 
**kubernetes** | [**KubernetesEnum**](KubernetesEnum.md) |  | [optional] 
**cpu** | **int** | unit is millicores (m). 1000m &#x3D; 1 cpu | [optional] 
**memory** | **int** | unit is MB. 1024 MB &#x3D; 1GB | [optional] 
**estimated_cloud_provider_cost** | **int** | This is an estimation of the cost this cluster will represent on your cloud proider bill, based on your current configuration | [optional] 
**status** | [**ClusterStateEnum**](ClusterStateEnum.md) |  | [optional] 
**has_access** | **bool** |  | [optional] 
**version** | **str** |  | [optional] 
**is_default** | **bool** |  | [optional] 
**production** | **bool** | specific flag to indicate that this cluster is a production one | [optional] 
**ssh_keys** | **List[str]** | Indicate your public ssh_key to remotely connect to your EC2 instance. | [optional] 
**features** | [**List[ClusterFeature]**](ClusterFeature.md) |  | [optional] 
**deployment_status** | [**ClusterDeploymentStatusEnum**](ClusterDeploymentStatusEnum.md) |  | [optional] 

## Example

```python
from qovery.models.cluster import Cluster

# TODO update the JSON string below
json = "{}"
# create an instance of Cluster from a JSON string
cluster_instance = Cluster.from_json(json)
# print the JSON string representation of the object
print Cluster.to_json()

# convert the object into a dict
cluster_dict = cluster_instance.to_dict()
# create an instance of Cluster from a dict
cluster_form_dict = cluster.from_dict(cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


