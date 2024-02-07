# DeploymentStageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the deployment stage | 
**description** | **str** | free test describing this stage | [optional] 

## Example

```python
from qovery.models.deployment_stage_request import DeploymentStageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentStageRequest from a JSON string
deployment_stage_request_instance = DeploymentStageRequest.from_json(json)
# print the JSON string representation of the object
print DeploymentStageRequest.to_json()

# convert the object into a dict
deployment_stage_request_dict = deployment_stage_request_instance.to_dict()
# create an instance of DeploymentStageRequest from a dict
deployment_stage_request_form_dict = deployment_stage_request.from_dict(deployment_stage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


