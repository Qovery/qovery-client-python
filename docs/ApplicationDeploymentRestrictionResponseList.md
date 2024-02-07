# ApplicationDeploymentRestrictionResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ApplicationDeploymentRestriction]**](ApplicationDeploymentRestriction.md) |  | [optional] 

## Example

```python
from qovery.models.application_deployment_restriction_response_list import ApplicationDeploymentRestrictionResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationDeploymentRestrictionResponseList from a JSON string
application_deployment_restriction_response_list_instance = ApplicationDeploymentRestrictionResponseList.from_json(json)
# print the JSON string representation of the object
print ApplicationDeploymentRestrictionResponseList.to_json()

# convert the object into a dict
application_deployment_restriction_response_list_dict = application_deployment_restriction_response_list_instance.to_dict()
# create an instance of ApplicationDeploymentRestrictionResponseList from a dict
application_deployment_restriction_response_list_form_dict = application_deployment_restriction_response_list.from_dict(application_deployment_restriction_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


