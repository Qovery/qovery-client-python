# ApplicationDeploymentRestriction


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**mode** | [**DeploymentRestrictionModeEnum**](DeploymentRestrictionModeEnum.md) |  | 
**type** | [**DeploymentRestrictionTypeEnum**](DeploymentRestrictionTypeEnum.md) |  | 
**value** | **str** | For &#x60;PATH&#x60; restrictions, the value must not start with &#x60;/&#x60; | 

## Example

```python
from qovery.models.application_deployment_restriction import ApplicationDeploymentRestriction

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationDeploymentRestriction from a JSON string
application_deployment_restriction_instance = ApplicationDeploymentRestriction.from_json(json)
# print the JSON string representation of the object
print ApplicationDeploymentRestriction.to_json()

# convert the object into a dict
application_deployment_restriction_dict = application_deployment_restriction_instance.to_dict()
# create an instance of ApplicationDeploymentRestriction from a dict
application_deployment_restriction_form_dict = application_deployment_restriction.from_dict(application_deployment_restriction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


