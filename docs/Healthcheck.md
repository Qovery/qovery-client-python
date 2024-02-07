# Healthcheck


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**readiness_probe** | [**Probe**](Probe.md) |  | [optional] 
**liveness_probe** | [**Probe**](Probe.md) |  | [optional] 

## Example

```python
from qovery.models.healthcheck import Healthcheck

# TODO update the JSON string below
json = "{}"
# create an instance of Healthcheck from a JSON string
healthcheck_instance = Healthcheck.from_json(json)
# print the JSON string representation of the object
print Healthcheck.to_json()

# convert the object into a dict
healthcheck_dict = healthcheck_instance.to_dict()
# create an instance of Healthcheck from a dict
healthcheck_form_dict = healthcheck.from_dict(healthcheck_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


