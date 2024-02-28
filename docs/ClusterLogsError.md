# ClusterLogsError

Present only for `error` log

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag** | **str** | log error tag | [optional] 
**user_log_message** | **str** | log details about the error | [optional] 
**link** | **str** | link to our documentation | [optional] 
**hint_message** | **str** | hint the user can follow | [optional] 
**event_details** | [**ClusterLogsErrorEventDetails**](ClusterLogsErrorEventDetails.md) |  | [optional] 
**underlying_error** | [**ClusterLogsErrorUnderlyingError**](ClusterLogsErrorUnderlyingError.md) |  | [optional] 

## Example

```python
from qovery.models.cluster_logs_error import ClusterLogsError

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterLogsError from a JSON string
cluster_logs_error_instance = ClusterLogsError.from_json(json)
# print the JSON string representation of the object
print ClusterLogsError.to_json()

# convert the object into a dict
cluster_logs_error_dict = cluster_logs_error_instance.to_dict()
# create an instance of ClusterLogsError from a dict
cluster_logs_error_form_dict = cluster_logs_error.from_dict(cluster_logs_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


