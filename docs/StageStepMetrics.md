# StageStepMetrics


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_duration_sec** | **int** | The total duration in seconds of the stage deployment or null if the deployment is not completed | [optional] 
**details** | [**List[StageStepMetric]**](StageStepMetric.md) | A list of metrics for deployment steps of the stage. | [optional] 

## Example

```python
from qovery.models.stage_step_metrics import StageStepMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of StageStepMetrics from a JSON string
stage_step_metrics_instance = StageStepMetrics.from_json(json)
# print the JSON string representation of the object
print StageStepMetrics.to_json()

# convert the object into a dict
stage_step_metrics_dict = stage_step_metrics_instance.to_dict()
# create an instance of StageStepMetrics from a dict
stage_step_metrics_form_dict = stage_step_metrics.from_dict(stage_step_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


