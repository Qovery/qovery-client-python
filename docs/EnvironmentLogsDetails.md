# EnvironmentLogsDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** |  | [optional] 
**cluster_id** | **str** |  | [optional] 
**execution_id** | **str** |  | [optional] 
**transmitter** | [**EnvironmentLogsDetailsTransmitter**](EnvironmentLogsDetailsTransmitter.md) |  | [optional] 
**stage** | [**EnvironmentLogsDetailsStage**](EnvironmentLogsDetailsStage.md) |  | [optional] 

## Example

```python
from qovery.models.environment_logs_details import EnvironmentLogsDetails

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentLogsDetails from a JSON string
environment_logs_details_instance = EnvironmentLogsDetails.from_json(json)
# print the JSON string representation of the object
print EnvironmentLogsDetails.to_json()

# convert the object into a dict
environment_logs_details_dict = environment_logs_details_instance.to_dict()
# create an instance of EnvironmentLogsDetails from a dict
environment_logs_details_form_dict = environment_logs_details.from_dict(environment_logs_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


