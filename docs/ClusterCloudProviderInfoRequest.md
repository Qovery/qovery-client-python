# ClusterCloudProviderInfoRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_provider** | [**CloudProviderEnum**](CloudProviderEnum.md) |  | [optional] 
**credentials** | [**ClusterCloudProviderInfoCredentials**](ClusterCloudProviderInfoCredentials.md) |  | [optional] 
**region** | **str** |  | [optional] 

## Example

```python
from qovery.models.cluster_cloud_provider_info_request import ClusterCloudProviderInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterCloudProviderInfoRequest from a JSON string
cluster_cloud_provider_info_request_instance = ClusterCloudProviderInfoRequest.from_json(json)
# print the JSON string representation of the object
print ClusterCloudProviderInfoRequest.to_json()

# convert the object into a dict
cluster_cloud_provider_info_request_dict = cluster_cloud_provider_info_request_instance.to_dict()
# create an instance of ClusterCloudProviderInfoRequest from a dict
cluster_cloud_provider_info_request_form_dict = cluster_cloud_provider_info_request.from_dict(cluster_cloud_provider_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


