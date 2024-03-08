# ClusterFeatureGcpExistingVpc


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vpc_name** | **str** |  | 
**vpc_project_id** | **str** |  | [optional] 
**subnetwork_name** | **str** |  | [optional] 
**ip_range_services_name** | **str** |  | [optional] 
**ip_range_pods_name** | **str** |  | [optional] 
**additional_ip_range_pods_names** | **List[str]** |  | [optional] 

## Example

```python
from qovery.models.cluster_feature_gcp_existing_vpc import ClusterFeatureGcpExistingVpc

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterFeatureGcpExistingVpc from a JSON string
cluster_feature_gcp_existing_vpc_instance = ClusterFeatureGcpExistingVpc.from_json(json)
# print the JSON string representation of the object
print ClusterFeatureGcpExistingVpc.to_json()

# convert the object into a dict
cluster_feature_gcp_existing_vpc_dict = cluster_feature_gcp_existing_vpc_instance.to_dict()
# create an instance of ClusterFeatureGcpExistingVpc from a dict
cluster_feature_gcp_existing_vpc_form_dict = cluster_feature_gcp_existing_vpc.from_dict(cluster_feature_gcp_existing_vpc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


