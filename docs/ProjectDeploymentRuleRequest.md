# ProjectDeploymentRuleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name is case insensitive | 
**description** | **str** |  | [optional] 
**mode** | [**EnvironmentModeEnum**](EnvironmentModeEnum.md) |  | 
**cluster_id** | **str** |  | 
**auto_stop** | **bool** |  | [optional] [default to False]
**timezone** | **str** |  | 
**start_time** | **datetime** |  | 
**stop_time** | **datetime** |  | 
**weekdays** | [**List[WeekdayEnum]**](WeekdayEnum.md) |  | 
**wildcard** | **str** | wildcard pattern composed of &#39;?&#39; and/or &#39;*&#39; used to target new created environments | [default to '']

## Example

```python
from qovery.models.project_deployment_rule_request import ProjectDeploymentRuleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDeploymentRuleRequest from a JSON string
project_deployment_rule_request_instance = ProjectDeploymentRuleRequest.from_json(json)
# print the JSON string representation of the object
print ProjectDeploymentRuleRequest.to_json()

# convert the object into a dict
project_deployment_rule_request_dict = project_deployment_rule_request_instance.to_dict()
# create an instance of ProjectDeploymentRuleRequest from a dict
project_deployment_rule_request_form_dict = project_deployment_rule_request.from_dict(project_deployment_rule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


