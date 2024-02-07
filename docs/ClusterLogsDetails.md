# ClusterLogsDetails

Present only for `info`, `warning` and `debug` logs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_kind** | **str** | cloud provider used | [optional] 
**region** | **str** |  | [optional] 
**transmitter** | [**ClusterLogsErrorEventDetailsTransmitter**](ClusterLogsErrorEventDetailsTransmitter.md) |  | [optional] 

## Example

```python
from qovery.models.cluster_logs_details import ClusterLogsDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterLogsDetails from a JSON string
cluster_logs_details_instance = ClusterLogsDetails.from_json(json)
# print the JSON string representation of the object
print ClusterLogsDetails.to_json()

# convert the object into a dict
cluster_logs_details_dict = cluster_logs_details_instance.to_dict()
# create an instance of ClusterLogsDetails from a dict
cluster_logs_details_form_dict = cluster_logs_details.from_dict(cluster_logs_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


