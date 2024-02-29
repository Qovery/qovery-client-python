# ProjectDeploymentRule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
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
**priority_index** | **int** | used to select the first deployment rule to match new created environments | [optional] 

## Example

```python
from qovery.models.project_deployment_rule import ProjectDeploymentRule

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDeploymentRule from a JSON string
project_deployment_rule_instance = ProjectDeploymentRule.from_json(json)
# print the JSON string representation of the object
print ProjectDeploymentRule.to_json()

# convert the object into a dict
project_deployment_rule_dict = project_deployment_rule_instance.to_dict()
# create an instance of ProjectDeploymentRule from a dict
project_deployment_rule_form_dict = project_deployment_rule.from_dict(project_deployment_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


