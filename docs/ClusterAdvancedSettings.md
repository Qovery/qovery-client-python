# ClusterAdvancedSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_cloudwatch_eks_logs_retention_days** | **int** | Set the number of retention days for EKS Cloudwatch logs | [optional] 
**aws_vpc_enable_s3_flow_logs** | **bool** | Enable flow logs for on the VPC and store them in an S3 bucket | [optional] 
**aws_vpc_flow_logs_retention_days** | **int** | Set the number of retention days for flow logs. Disable with value \&quot;0\&quot; | [optional] 
**loki_log_retention_in_week** | **int** | For how long in week loki is going to keep logs of your applications | [optional] 
**registry_image_retention_time** | **int** | Configure the number of seconds before cleaning images in the registry | [optional] 
**cloud_provider_container_registry_tags** | **Dict[str, str]** | Add additional tags on the cluster dedicated registry | [optional] 
**load_balancer_size** | **str** | Select the size of the main load_balancer (only effective for Scaleway) | [optional] 
**database_postgresql_deny_public_access** | **bool** | Deny public access to any PostgreSQL database | [optional] 
**database_postgresql_allowed_cidrs** | **List[str]** | List of CIDRs allowed to access the PostgreSQL database | [optional] 
**database_mysql_deny_public_access** | **bool** | Deny public access to any MySql database | [optional] 
**database_mysql_allowed_cidrs** | **List[str]** | List of CIDRs allowed to access the MySql database | [optional] 
**database_mongodb_deny_public_access** | **bool** | Deny public access to any MongoDB/DocumentDB database | [optional] 
**database_mongodb_allowed_cidrs** | **List[str]** | List of CIDRs allowed to access the MongoDB/DocumentDB database | [optional] 
**database_redis_deny_public_access** | **bool** | Deny public access to any Redis database | [optional] 
**database_redis_allowed_cidrs** | **List[str]** | List of CIDRs allowed to access the Redis database | [optional] 
**aws_iam_admin_group** | **str** | AWS IAM group name with cluster access | [optional] 
**aws_eks_ec2_metadata_imds** | **str** | Specify the [IMDS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html) version you want to use:   * &#x60;required&#x60;: IMDS V2 only   * &#x60;optional&#x60;: IMDS V1 + V2  | [optional] 
**pleco_resources_ttl** | **int** |  | [optional] 
**registry_mirroring_mode** | [**RegistryMirroringModeEnum**](RegistryMirroringModeEnum.md) |  | [optional] 
**nginx_vcpu_request_in_milli_cpu** | **int** | vcpu request in millicores | [optional] 
**nginx_vcpu_limit_in_milli_cpu** | **int** | vcpu limit in millicores | [optional] 
**nginx_memory_request_in_mib** | **int** | memory request in MiB | [optional] 
**nginx_memory_limit_in_mib** | **int** | memory limit in MiB | [optional] 
**nginx_hpa_cpu_utilization_percentage_threshold** | **int** | hpa cpu threshold in percentage | [optional] 
**nginx_hpa_min_number_instances** | **int** | hpa minimum number of instances | [optional] 
**nginx_hpa_max_number_instances** | **int** | hpa maximum number of instances | [optional] 

## Example

```python
from qovery.models.cluster_advanced_settings import ClusterAdvancedSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAdvancedSettings from a JSON string
cluster_advanced_settings_instance = ClusterAdvancedSettings.from_json(json)
# print the JSON string representation of the object
print ClusterAdvancedSettings.to_json()

# convert the object into a dict
cluster_advanced_settings_dict = cluster_advanced_settings_instance.to_dict()
# create an instance of ClusterAdvancedSettings from a dict
cluster_advanced_settings_form_dict = cluster_advanced_settings.from_dict(cluster_advanced_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


