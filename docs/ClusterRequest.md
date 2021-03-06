# ClusterRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name is case-insensitive | 
**region** | **str** |  | 
**cloud_provider** | [**CloudProviderEnum**](CloudProviderEnum.md) |  | 
**description** | **str** |  | [optional] 
**min_running_nodes** | **int** |  | [optional]  if omitted the server will use the default value of 1
**max_running_nodes** | **int** |  | [optional]  if omitted the server will use the default value of 1
**disk_size** | **int** | Unit is in GB. The disk size to be used for the node configuration | [optional]  if omitted the server will use the default value of 20
**instance_type** | **str** | the instance type to be used for this cluster. The list of values can be retrieved via the endpoint /{CloudProvider}/instanceType | [optional] 
**kubernetes** | [**KubernetesEnum**](KubernetesEnum.md) |  | [optional] 
**production** | **bool** | specific flag to indicate that this cluster is a production one | [optional] 
**ssh_keys** | **[str]** | Indicate your public ssh_key to remotely connect to your EC2 instance. | [optional] 
**features** | [**[ClusterRequestFeaturesInner]**](ClusterRequestFeaturesInner.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


