# ServiceStepMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_duration_sec** | **int** | The total duration in seconds of the service deployment or null if the deployment is not completed. | [optional] 
**total_computing_duration_sec** | **int** | The total duration in seconds of the service deployment without queuing steps. | [optional] 
**details** | [**List[ServiceStepMetric]**](ServiceStepMetric.md) | A list of metrics for deployment steps of the service. | [optional] 

## Example

```python
from qovery.models.service_step_metrics import ServiceStepMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceStepMetrics from a JSON string
service_step_metrics_instance = ServiceStepMetrics.from_json(json)
# print the JSON string representation of the object
print ServiceStepMetrics.to_json()

# convert the object into a dict
service_step_metrics_dict = service_step_metrics_instance.to_dict()
# create an instance of ServiceStepMetrics from a dict
service_step_metrics_form_dict = service_step_metrics.from_dict(service_step_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


