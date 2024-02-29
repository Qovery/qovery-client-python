# ClusterRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name is case-insensitive | 
**description** | **str** |  | [optional] 
**region** | **str** |  | 
**cloud_provider** | [**CloudProviderEnum**](CloudProviderEnum.md) |  | 
**cloud_provider_credentials** | [**ClusterCloudProviderInfoRequest**](ClusterCloudProviderInfoRequest.md) |  | [optional] 
**min_running_nodes** | **int** |  | [optional] [default to 1]
**max_running_nodes** | **int** |  | [optional] [default to 1]
**disk_size** | **int** | Unit is in GB. The disk size to be used for the node configuration | [optional] [default to 40]
**instance_type** | **str** | the instance type to be used for this cluster. The list of values can be retrieved via the endpoint /{CloudProvider}/instanceType | [optional] 
**kubernetes** | [**KubernetesEnum**](KubernetesEnum.md) |  | [optional] 
**production** | **bool** | specific flag to indicate that this cluster is a production one | [optional] 
**ssh_keys** | **List[str]** | Indicate your public ssh_key to remotely connect to your EC2 instance. | [optional] 
**kubeconfig** | **str** | If the cluster is a self managed one. The kubeconfig to use to connect to it | [optional] 
**features** | [**List[ClusterRequestFeaturesInner]**](ClusterRequestFeaturesInner.md) |  | [optional] 

## Example

```python
from qovery.models.cluster_request import ClusterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterRequest from a JSON string
cluster_request_instance = ClusterRequest.from_json(json)
# print the JSON string representation of the object
print ClusterRequest.to_json()

# convert the object into a dict
cluster_request_dict = cluster_request_instance.to_dict()
# create an instance of ClusterRequest from a dict
cluster_request_form_dict = cluster_request.from_dict(cluster_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


