# ClusterAdvancedSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_cloudwatch_eks_logs_retention_days** | **int** | Set the number of retention days for EKS Cloudwatch logs | [optional]  if omitted the server will use the default value of 90
**aws_vpc_enable_s3_flow_logs** | **bool** | Enable flow logs for on the VPC and store them in an S3 bucket | [optional]  if omitted the server will use the default value of False
**aws_vpc_flow_logs_retention_days** | **int** | Set the number of retention days for flow logs. Disable with value \&quot;0\&quot; | [optional]  if omitted the server will use the default value of 365
**loki_log_retention_in_week** | **int** | For how long in week loki is going to keep logs of your applications | [optional]  if omitted the server will use the default value of 12
**registry_image_retention_time** | **int** | Configure the number of seconds before cleaning images in the registry | [optional]  if omitted the server will use the default value of 31536000
**cloud_provider_container_registry_tags** | **{str: (str,)}** | Add additional tags on the cluster dedicated registry | [optional] 
**load_balancer_size** | **str** | Select the size of the main load_balancer (only effective for Scaleway) | [optional]  if omitted the server will use the default value of "lb-s"
**database_postgresql_deny_public_access** | **bool** | Deny public access to any PostgreSQL database | [optional]  if omitted the server will use the default value of False
**database_postgresql_allowed_cidrs** | **[str]** | List of CIDRs allowed to access the PostgreSQL database | [optional]  if omitted the server will use the default value of ["0.0.0.0/0"]
**database_mysql_deny_public_access** | **bool** | Deny public access to any MySql database | [optional]  if omitted the server will use the default value of False
**database_mysql_allowed_cidrs** | **[str]** | List of CIDRs allowed to access the MySql database | [optional]  if omitted the server will use the default value of ["0.0.0.0/0"]
**database_mongodb_deny_public_access** | **bool** | Deny public access to any MongoDB/DocumentDB database | [optional]  if omitted the server will use the default value of False
**database_mongodb_allowed_cidrs** | **[str]** | List of CIDRs allowed to access the MongoDB/DocumentDB database | [optional]  if omitted the server will use the default value of ["0.0.0.0/0"]
**database_redis_deny_public_access** | **bool** | Deny public access to any Redis database | [optional]  if omitted the server will use the default value of False
**database_redis_allowed_cidrs** | **[str]** | List of CIDRs allowed to access the Redis database | [optional]  if omitted the server will use the default value of ["0.0.0.0/0"]
**aws_iam_admin_group** | **str** | AWS IAM group name with cluster access | [optional]  if omitted the server will use the default value of "Admins"
**aws_eks_ec2_metadata_imds** | **str** | Specify the [IMDS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html) version you want to use:   * &#x60;required&#x60;: IMDS V2 only   * &#x60;optional&#x60;: IMDS V1 + V2  | [optional]  if omitted the server will use the default value of "optional"
**pleco_resources_ttl** | **int** |  | [optional]  if omitted the server will use the default value of -1
**registry_mirroring_mode** | [**RegistryMirroringModeEnum**](RegistryMirroringModeEnum.md) |  | [optional] 
**nginx_vcpu_request_in_milli_cpu** | **int** | vcpu request in millicores | [optional]  if omitted the server will use the default value of 100
**nginx_vcpu_limit_in_milli_cpu** | **int** | vcpu limit in millicores | [optional]  if omitted the server will use the default value of 500
**nginx_memory_request_in_mib** | **int** | memory request in MiB | [optional]  if omitted the server will use the default value of 768
**nginx_memory_limit_in_mib** | **int** | memory limit in MiB | [optional]  if omitted the server will use the default value of 768
**nginx_hpa_cpu_utilization_percentage_threshold** | **int** | hpa cpu threshold in percentage | [optional]  if omitted the server will use the default value of 50
**nginx_hpa_min_number_instances** | **int** | hpa minimum number of instances | [optional]  if omitted the server will use the default value of 2
**nginx_hpa_max_number_instances** | **int** | hpa maximum number of instances | [optional]  if omitted the server will use the default value of 25
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


