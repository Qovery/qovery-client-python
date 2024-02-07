# DeploymentStageResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[DeploymentStageResponse]**](DeploymentStageResponse.md) |  | [optional] 

## Example

```python
from qovery.models.deployment_stage_response_list import DeploymentStageResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentStageResponseList from a JSON string
deployment_stage_response_list_instance = DeploymentStageResponseList.from_json(json)
# print the JSON string representation of the object
print DeploymentStageResponseList.to_json()

# convert the object into a dict
deployment_stage_response_list_dict = deployment_stage_response_list_instance.to_dict()
# create an instance of DeploymentStageResponseList from a dict
deployment_stage_response_list_form_dict = deployment_stage_response_list.from_dict(deployment_stage_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


