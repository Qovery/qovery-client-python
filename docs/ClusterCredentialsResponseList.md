# ClusterCredentialsResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ClusterCredentials]**](ClusterCredentials.md) |  | [optional] 

## Example

```python
from qovery.models.cluster_credentials_response_list import ClusterCredentialsResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterCredentialsResponseList from a JSON string
cluster_credentials_response_list_instance = ClusterCredentialsResponseList.from_json(json)
# print the JSON string representation of the object
print ClusterCredentialsResponseList.to_json()

# convert the object into a dict
cluster_credentials_response_list_dict = cluster_credentials_response_list_instance.to_dict()
# create an instance of ClusterCredentialsResponseList from a dict
cluster_credentials_response_list_form_dict = cluster_credentials_response_list.from_dict(cluster_credentials_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


