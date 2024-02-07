# HelmDeploymentRestrictionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | [**DeploymentRestrictionModeEnum**](DeploymentRestrictionModeEnum.md) |  | 
**type** | [**DeploymentRestrictionTypeEnum**](DeploymentRestrictionTypeEnum.md) |  | 
**value** | **str** | For &#x60;PATH&#x60; restrictions, the value must not start with &#x60;/&#x60; | 

## Example

```python
from qovery.models.helm_deployment_restriction_request import HelmDeploymentRestrictionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HelmDeploymentRestrictionRequest from a JSON string
helm_deployment_restriction_request_instance = HelmDeploymentRestrictionRequest.from_json(json)
# print the JSON string representation of the object
print HelmDeploymentRestrictionRequest.to_json()

# convert the object into a dict
helm_deployment_restriction_request_dict = helm_deployment_restriction_request_instance.to_dict()
# create an instance of HelmDeploymentRestrictionRequest from a dict
helm_deployment_restriction_request_form_dict = helm_deployment_restriction_request.from_dict(helm_deployment_restriction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


