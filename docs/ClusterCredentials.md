# ClusterCredentials


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from qovery.models.cluster_credentials import ClusterCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterCredentials from a JSON string
cluster_credentials_instance = ClusterCredentials.from_json(json)
# print the JSON string representation of the object
print ClusterCredentials.to_json()

# convert the object into a dict
cluster_credentials_dict = cluster_credentials_instance.to_dict()
# create an instance of ClusterCredentials from a dict
cluster_credentials_form_dict = cluster_credentials.from_dict(cluster_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


