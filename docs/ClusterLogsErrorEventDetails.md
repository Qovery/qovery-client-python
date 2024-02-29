# ClusterLogsErrorEventDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_kind** | **str** | cloud provider used | [optional] 
**region** | **str** |  | [optional] 
**transmitter** | [**ClusterLogsErrorEventDetailsTransmitter**](ClusterLogsErrorEventDetailsTransmitter.md) |  | [optional] 

## Example

```python
from qovery.models.cluster_logs_error_event_details import ClusterLogsErrorEventDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterLogsErrorEventDetails from a JSON string
cluster_logs_error_event_details_instance = ClusterLogsErrorEventDetails.from_json(json)
# print the JSON string representation of the object
print ClusterLogsErrorEventDetails.to_json()

# convert the object into a dict
cluster_logs_error_event_details_dict = cluster_logs_error_event_details_instance.to_dict()
# create an instance of ClusterLogsErrorEventDetails from a dict
cluster_logs_error_event_details_form_dict = cluster_logs_error_event_details.from_dict(cluster_logs_error_event_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


