# ClusterLogsMessage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**safe_message** | **str** | log global message | [optional] 

## Example

```python
from qovery.models.cluster_logs_message import ClusterLogsMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterLogsMessage from a JSON string
cluster_logs_message_instance = ClusterLogsMessage.from_json(json)
# print the JSON string representation of the object
print ClusterLogsMessage.to_json()

# convert the object into a dict
cluster_logs_message_dict = cluster_logs_message_instance.to_dict()
# create an instance of ClusterLogsMessage from a dict
cluster_logs_message_form_dict = cluster_logs_message.from_dict(cluster_logs_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


