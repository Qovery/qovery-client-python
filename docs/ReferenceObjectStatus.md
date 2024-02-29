# ReferenceObjectStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**state** | [**StateEnum**](StateEnum.md) |  | 
**service_deployment_status** | [**ServiceDeploymentStatusEnum**](ServiceDeploymentStatusEnum.md) |  | 
**last_deployment_date** | **datetime** |  | [optional] 
**is_part_last_deployment** | **bool** |  | [optional] 
**steps** | [**ServiceStepMetrics**](ServiceStepMetrics.md) |  | [optional] 

## Example

```python
from qovery.models.reference_object_status import ReferenceObjectStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ReferenceObjectStatus from a JSON string
reference_object_status_instance = ReferenceObjectStatus.from_json(json)
# print the JSON string representation of the object
print ReferenceObjectStatus.to_json()

# convert the object into a dict
reference_object_status_dict = reference_object_status_instance.to_dict()
# create an instance of ReferenceObjectStatus from a dict
reference_object_status_form_dict = reference_object_status.from_dict(reference_object_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


