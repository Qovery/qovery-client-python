# ApplicationDeploymentRestrictionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | [**DeploymentRestrictionModeEnum**](DeploymentRestrictionModeEnum.md) |  | 
**type** | [**DeploymentRestrictionTypeEnum**](DeploymentRestrictionTypeEnum.md) |  | 
**value** | **str** | For &#x60;PATH&#x60; restrictions, the value must not start with &#x60;/&#x60; | 

## Example

```python
from qovery.models.application_deployment_restriction_request import ApplicationDeploymentRestrictionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationDeploymentRestrictionRequest from a JSON string
application_deployment_restriction_request_instance = ApplicationDeploymentRestrictionRequest.from_json(json)
# print the JSON string representation of the object
print ApplicationDeploymentRestrictionRequest.to_json()

# convert the object into a dict
application_deployment_restriction_request_dict = application_deployment_restriction_request_instance.to_dict()
# create an instance of ApplicationDeploymentRestrictionRequest from a dict
application_deployment_restriction_request_form_dict = application_deployment_restriction_request.from_dict(application_deployment_restriction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


