# ClusterRequestFeaturesInnerValueOneOf


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

## Example

```python
from qovery.models.cluster_request_features_inner_value_one_of import ClusterRequestFeaturesInnerValueOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterRequestFeaturesInnerValueOneOf from a JSON string
cluster_request_features_inner_value_one_of_instance = ClusterRequestFeaturesInnerValueOneOf.from_json(json)
# print the JSON string representation of the object
print ClusterRequestFeaturesInnerValueOneOf.to_json()

# convert the object into a dict
cluster_request_features_inner_value_one_of_dict = cluster_request_features_inner_value_one_of_instance.to_dict()
# create an instance of ClusterRequestFeaturesInnerValueOneOf from a dict
cluster_request_features_inner_value_one_of_form_dict = cluster_request_features_inner_value_one_of.from_dict(cluster_request_features_inner_value_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


