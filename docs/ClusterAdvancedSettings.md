# ClusterAdvancedSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loki_log_retention_in_week** | **int** | For how long in week loki is going to keep logs of your applications | [optional]  if omitted the server will use the default value of 12
**aws_vpc_enable_s3_flow_logs** | **bool** | Enable flow logs for on the VPC and store them in an S3 bucket | [optional]  if omitted the server will use the default value of False
**registry_image_retention_time** | **int** | Configure the number of seconds before cleaning images in the registry | [optional]  if omitted the server will use the default value of 31536000
**cloud_provider_container_registry_tags** | [**ClusterAdvancedSettingsCloudProviderContainerRegistryTags**](ClusterAdvancedSettingsCloudProviderContainerRegistryTags.md) |  | [optional] 
**load_balancer_size** | **str** | Select the size of the main load_balancer (only effective for Scaleway) | [optional]  if omitted the server will use the default value of "lb-s"
**pleco_resources_ttl** | **int** |  | [optional]  if omitted the server will use the default value of -1
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


