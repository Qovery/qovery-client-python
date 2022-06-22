# Cluster


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**name** | **str** | name is case-insensitive | 
**region** | **str** |  | 
**cloud_provider** | [**CloudProviderEnum**](CloudProviderEnum.md) |  | 
**updated_at** | **datetime** |  | [optional] [readonly] 
**description** | **str** |  | [optional] 
**min_running_nodes** | **int** |  | [optional]  if omitted the server will use the default value of 1
**max_running_nodes** | **int** |  | [optional]  if omitted the server will use the default value of 1
**disk_size** | **int** | Unit is in GB. The disk size to be used for the node configuration | [optional]  if omitted the server will use the default value of 20
**instance_type** | **str** | the instance type to be used for this cluster. The list of values can be retrieved via the endpoint /{CloudProvider}/instanceType | [optional] 
**kubernetes** | [**KubernetesEnum**](KubernetesEnum.md) |  | [optional] 
**cpu** | **int** | unit is millicores (m). 1000m &#x3D; 1 cpu | [optional] 
**memory** | **int** | unit is MB. 1024 MB &#x3D; 1GB | [optional] 
**estimated_cloud_provider_cost** | **int** | This is an estimation of the cost this cluster will represent on your cloud proider bill, based on your current configuration | [optional] 
**status** | [**StateEnum**](StateEnum.md) |  | [optional] 
**has_access** | **bool** |  | [optional] 
**version** | **str** |  | [optional] 
**is_default** | **bool** |  | [optional] 
**production** | **bool** | specific flag to indicate that this cluster is a production one | [optional] 
**ssh_keys** | [**ClusterAllOfSshKeys**](ClusterAllOfSshKeys.md) |  | [optional] 
**features** | [**[ClusterAllOfFeatures]**](ClusterAllOfFeatures.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


