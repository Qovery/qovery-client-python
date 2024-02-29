# DeploymentStageServiceResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**service_id** | **str** | id of the service attached to the stage | [optional] 
**service_type** | **str** | type of the service (i.e APPLICATION, JOB, DATABASE, ...) | [optional] 

## Example

```python
from qovery.models.deployment_stage_service_response import DeploymentStageServiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentStageServiceResponse from a JSON string
deployment_stage_service_response_instance = DeploymentStageServiceResponse.from_json(json)
# print the JSON string representation of the object
print DeploymentStageServiceResponse.to_json()

# convert the object into a dict
deployment_stage_service_response_dict = deployment_stage_service_response_instance.to_dict()
# create an instance of DeploymentStageServiceResponse from a dict
deployment_stage_service_response_form_dict = deployment_stage_service_response.from_dict(deployment_stage_service_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


