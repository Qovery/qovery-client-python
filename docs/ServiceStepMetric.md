# ServiceStepMetric


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**step_name** | [**ServiceStepMetricNameEnum**](ServiceStepMetricNameEnum.md) |  | [optional] 
**status** | [**StepMetricStatusEnum**](StepMetricStatusEnum.md) |  | [optional] 
**duration_sec** | **int** | The duration of the step in seconds. | [optional] 

## Example

```python
from qovery.models.service_step_metric import ServiceStepMetric

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceStepMetric from a JSON string
service_step_metric_instance = ServiceStepMetric.from_json(json)
# print the JSON string representation of the object
print ServiceStepMetric.to_json()

# convert the object into a dict
service_step_metric_dict = service_step_metric_instance.to_dict()
# create an instance of ServiceStepMetric from a dict
service_step_metric_form_dict = service_step_metric.from_dict(service_step_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


