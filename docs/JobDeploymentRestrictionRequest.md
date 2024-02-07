# JobDeploymentRestrictionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | [**DeploymentRestrictionModeEnum**](DeploymentRestrictionModeEnum.md) |  | 
**type** | [**DeploymentRestrictionTypeEnum**](DeploymentRestrictionTypeEnum.md) |  | 
**value** | **str** | For &#x60;PATH&#x60; restrictions, the value must not start with &#x60;/&#x60; | 

## Example

```python
from qovery.models.job_deployment_restriction_request import JobDeploymentRestrictionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of JobDeploymentRestrictionRequest from a JSON string
job_deployment_restriction_request_instance = JobDeploymentRestrictionRequest.from_json(json)
# print the JSON string representation of the object
print JobDeploymentRestrictionRequest.to_json()

# convert the object into a dict
job_deployment_restriction_request_dict = job_deployment_restriction_request_instance.to_dict()
# create an instance of JobDeploymentRestrictionRequest from a dict
job_deployment_restriction_request_form_dict = job_deployment_restriction_request.from_dict(job_deployment_restriction_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


