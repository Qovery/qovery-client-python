# Probe


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ProbeType**](ProbeType.md) |  | [optional] 
**initial_delay_seconds** | **int** |  | [optional] [default to 30]
**period_seconds** | **int** |  | [optional] [default to 10]
**timeout_seconds** | **int** |  | [optional] [default to 5]
**success_threshold** | **int** |  | [optional] [default to 1]
**failure_threshold** | **int** |  | [optional] [default to 9]

## Example

```python
from qovery.models.probe import Probe

# TODO update the JSON string below
json = "{}"
# create an instance of Probe from a JSON string
probe_instance = Probe.from_json(json)
# print the JSON string representation of the object
print Probe.to_json()

# convert the object into a dict
probe_dict = probe_instance.to_dict()
# create an instance of Probe from a dict
probe_form_dict = probe.from_dict(probe_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


