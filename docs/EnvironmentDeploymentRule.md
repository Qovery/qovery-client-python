# EnvironmentDeploymentRule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**on_demand_preview** | **bool** |  | [optional] [default to False]
**auto_stop** | **bool** |  | [optional] [default to False]
**auto_preview** | **bool** |  | [optional] [default to False]
**timezone** | **str** |  | 
**start_time** | **datetime** |  | 
**stop_time** | **datetime** |  | 
**weekdays** | [**List[WeekdayEnum]**](WeekdayEnum.md) |  | 

## Example

```python
from qovery.models.environment_deployment_rule import EnvironmentDeploymentRule

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentDeploymentRule from a JSON string
environment_deployment_rule_instance = EnvironmentDeploymentRule.from_json(json)
# print the JSON string representation of the object
print EnvironmentDeploymentRule.to_json()

# convert the object into a dict
environment_deployment_rule_dict = environment_deployment_rule_instance.to_dict()
# create an instance of EnvironmentDeploymentRule from a dict
environment_deployment_rule_form_dict = environment_deployment_rule.from_dict(environment_deployment_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


