# ClusterReadinessStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_ready** | **bool** |  | [optional] 

## Example

```python
from qovery.models.cluster_readiness_status import ClusterReadinessStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterReadinessStatus from a JSON string
cluster_readiness_status_instance = ClusterReadinessStatus.from_json(json)
# print the JSON string representation of the object
print ClusterReadinessStatus.to_json()

# convert the object into a dict
cluster_readiness_status_dict = cluster_readiness_status_instance.to_dict()
# create an instance of ClusterReadinessStatus from a dict
cluster_readiness_status_form_dict = cluster_readiness_status.from_dict(cluster_readiness_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


