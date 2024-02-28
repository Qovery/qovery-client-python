# HelmDeploymentRestrictionResponseList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[HelmDeploymentRestrictionResponse]**](HelmDeploymentRestrictionResponse.md) |  | [optional] 

## Example

```python
from qovery.models.helm_deployment_restriction_response_list import HelmDeploymentRestrictionResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of HelmDeploymentRestrictionResponseList from a JSON string
helm_deployment_restriction_response_list_instance = HelmDeploymentRestrictionResponseList.from_json(json)
# print the JSON string representation of the object
print HelmDeploymentRestrictionResponseList.to_json()

# convert the object into a dict
helm_deployment_restriction_response_list_dict = helm_deployment_restriction_response_list_instance.to_dict()
# create an instance of HelmDeploymentRestrictionResponseList from a dict
helm_deployment_restriction_response_list_form_dict = helm_deployment_restriction_response_list.from_dict(helm_deployment_restriction_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


