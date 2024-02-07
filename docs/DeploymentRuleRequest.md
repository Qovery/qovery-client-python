# DeploymentRuleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name is case insensitive | 
**description** | **str** |  | [optional] 
**mode** | [**EnvironmentModeEnum**](EnvironmentModeEnum.md) |  | 
**cluster** | **str** |  | 
**auto_stop** | **bool** |  | [default to False]
**timezone** | **str** | specify value only if auto_stop &#x3D; false | [optional] [default to 'Europe/London']
**start_time** | **datetime** | specify value only if auto_stop &#x3D; false | [optional] 
**stop_time** | **datetime** | specify value only if auto_stop &#x3D; false | [optional] 
**weekdays** | [**List[WeekdayEnum]**](WeekdayEnum.md) | specify value only if auto_stop &#x3D; false | [optional] 

## Example

```python
from qovery.models.deployment_rule_request import DeploymentRuleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentRuleRequest from a JSON string
deployment_rule_request_instance = DeploymentRuleRequest.from_json(json)
# print the JSON string representation of the object
print DeploymentRuleRequest.to_json()

# convert the object into a dict
deployment_rule_request_dict = deployment_rule_request_instance.to_dict()
# create an instance of DeploymentRuleRequest from a dict
deployment_rule_request_form_dict = deployment_rule_request.from_dict(deployment_rule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


