# ProjectDeploymentRulesPriorityOrderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_deployment_rule_ids_in_order** | **List[str]** |  | [optional] 

## Example

```python
from qovery.models.project_deployment_rules_priority_order_request import ProjectDeploymentRulesPriorityOrderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDeploymentRulesPriorityOrderRequest from a JSON string
project_deployment_rules_priority_order_request_instance = ProjectDeploymentRulesPriorityOrderRequest.from_json(json)
# print the JSON string representation of the object
print ProjectDeploymentRulesPriorityOrderRequest.to_json()

# convert the object into a dict
project_deployment_rules_priority_order_request_dict = project_deployment_rules_priority_order_request_instance.to_dict()
# create an instance of ProjectDeploymentRulesPriorityOrderRequest from a dict
project_deployment_rules_priority_order_request_form_dict = project_deployment_rules_priority_order_request.from_dict(project_deployment_rules_priority_order_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


