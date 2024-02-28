# ClusterCloudProviderInfoCredentials


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from qovery.models.cluster_cloud_provider_info_credentials import ClusterCloudProviderInfoCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterCloudProviderInfoCredentials from a JSON string
cluster_cloud_provider_info_credentials_instance = ClusterCloudProviderInfoCredentials.from_json(json)
# print the JSON string representation of the object
print ClusterCloudProviderInfoCredentials.to_json()

# convert the object into a dict
cluster_cloud_provider_info_credentials_dict = cluster_cloud_provider_info_credentials_instance.to_dict()
# create an instance of ClusterCloudProviderInfoCredentials from a dict
cluster_cloud_provider_info_credentials_form_dict = cluster_cloud_provider_info_credentials.from_dict(cluster_cloud_provider_info_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


