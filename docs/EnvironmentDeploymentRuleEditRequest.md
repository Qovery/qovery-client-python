# EnvironmentDeploymentRuleEditRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**on_demand_preview** | **bool** |  | [optional] [default to False]
**auto_preview** | **bool** |  | [optional] [default to False]
**auto_stop** | **bool** |  | [optional] [default to False]
**timezone** | **str** |  | 
**start_time** | **datetime** |  | 
**stop_time** | **datetime** |  | 
**weekdays** | [**List[WeekdayEnum]**](WeekdayEnum.md) |  | 

## Example

```python
from qovery.models.environment_deployment_rule_edit_request import EnvironmentDeploymentRuleEditRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentDeploymentRuleEditRequest from a JSON string
environment_deployment_rule_edit_request_instance = EnvironmentDeploymentRuleEditRequest.from_json(json)
# print the JSON string representation of the object
print EnvironmentDeploymentRuleEditRequest.to_json()

# convert the object into a dict
environment_deployment_rule_edit_request_dict = environment_deployment_rule_edit_request_instance.to_dict()
# create an instance of EnvironmentDeploymentRuleEditRequest from a dict
environment_deployment_rule_edit_request_form_dict = environment_deployment_rule_edit_request.from_dict(environment_deployment_rule_edit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


