# HelmDeploymentRestrictionResponse


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
from qovery.models.helm_deployment_restriction_response import HelmDeploymentRestrictionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HelmDeploymentRestrictionResponse from a JSON string
helm_deployment_restriction_response_instance = HelmDeploymentRestrictionResponse.from_json(json)
# print the JSON string representation of the object
print HelmDeploymentRestrictionResponse.to_json()

# convert the object into a dict
helm_deployment_restriction_response_dict = helm_deployment_restriction_response_instance.to_dict()
# create an instance of HelmDeploymentRestrictionResponse from a dict
helm_deployment_restriction_response_form_dict = helm_deployment_restriction_response.from_dict(helm_deployment_restriction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


