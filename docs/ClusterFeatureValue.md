# ClusterFeatureValue


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_vpc_eks_id** | **str** |  | 
**eks_subnets_zone_a_ids** | **List[str]** |  | 
**eks_subnets_zone_b_ids** | **List[str]** |  | 
**eks_subnets_zone_c_ids** | **List[str]** |  | 
**documentdb_subnets_zone_a_ids** | **List[str]** |  | [optional] 
**documentdb_subnets_zone_b_ids** | **List[str]** |  | [optional] 
**documentdb_subnets_zone_c_ids** | **List[str]** |  | [optional] 
**elasticache_subnets_zone_a_ids** | **List[str]** |  | [optional] 
**elasticache_subnets_zone_b_ids** | **List[str]** |  | [optional] 
**elasticache_subnets_zone_c_ids** | **List[str]** |  | [optional] 
**rds_subnets_zone_a_ids** | **List[str]** |  | [optional] 
**rds_subnets_zone_b_ids** | **List[str]** |  | [optional] 
**rds_subnets_zone_c_ids** | **List[str]** |  | [optional] 
**vpc_name** | **str** |  | 
**vpc_project_id** | **str** |  | [optional] 
**subnetwork_name** | **str** |  | [optional] 
**ip_range_services_name** | **str** |  | [optional] 
**ip_range_pods_name** | **str** |  | [optional] 
**additional_ip_range_pods_names** | **List[str]** |  | [optional] 

## Example

```python
from qovery.models.cluster_feature_value import ClusterFeatureValue

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterFeatureValue from a JSON string
cluster_feature_value_instance = ClusterFeatureValue.from_json(json)
# print the JSON string representation of the object
print ClusterFeatureValue.to_json()

# convert the object into a dict
cluster_feature_value_dict = cluster_feature_value_instance.to_dict()
# create an instance of ClusterFeatureValue from a dict
cluster_feature_value_form_dict = cluster_feature_value.from_dict(cluster_feature_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


