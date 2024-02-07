# CloudProviderResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[CloudProvider]**](CloudProvider.md) |  | [optional] 

## Example

```python
from qovery.models.cloud_provider_response_list import CloudProviderResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of CloudProviderResponseList from a JSON string
cloud_provider_response_list_instance = CloudProviderResponseList.from_json(json)
# print the JSON string representation of the object
print CloudProviderResponseList.to_json()

# convert the object into a dict
cloud_provider_response_list_dict = cloud_provider_response_list_instance.to_dict()
# create an instance of CloudProviderResponseList from a dict
cloud_provider_response_list_form_dict = cloud_provider_response_list.from_dict(cloud_provider_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


