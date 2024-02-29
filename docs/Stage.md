# Stage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** | stage name | 
**steps** | [**StageStepMetrics**](StageStepMetrics.md) |  | [optional] 

## Example

```python
from qovery.models.stage import Stage

# TODO update the JSON string below
json = "{}"
# create an instance of Stage from a JSON string
stage_instance = Stage.from_json(json)
# print the JSON string representation of the object
print Stage.to_json()

# convert the object into a dict
stage_dict = stage_instance.to_dict()
# create an instance of Stage from a dict
stage_form_dict = stage.from_dict(stage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


