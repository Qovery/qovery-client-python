# DeploymentStageResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**environment** | [**ReferenceObject**](ReferenceObject.md) |  | 
**name** | **str** | name is case insensitive | [optional] 
**description** | **str** |  | [optional] 
**deployment_order** | **int** | Position of the deployment stage within the environment | [optional] 
**services** | [**List[DeploymentStageServiceResponse]**](DeploymentStageServiceResponse.md) |  | [optional] 

## Example

```python
from qovery.models.deployment_stage_response import DeploymentStageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentStageResponse from a JSON string
deployment_stage_response_instance = DeploymentStageResponse.from_json(json)
# print the JSON string representation of the object
print DeploymentStageResponse.to_json()

# convert the object into a dict
deployment_stage_response_dict = deployment_stage_response_instance.to_dict()
# create an instance of DeploymentStageResponse from a dict
deployment_stage_response_form_dict = deployment_stage_response.from_dict(deployment_stage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


