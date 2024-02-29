# JobDeploymentRestrictionResponseList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[JobDeploymentRestrictionResponse]**](JobDeploymentRestrictionResponse.md) |  | [optional] 

## Example

```python
from qovery.models.job_deployment_restriction_response_list import JobDeploymentRestrictionResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of JobDeploymentRestrictionResponseList from a JSON string
job_deployment_restriction_response_list_instance = JobDeploymentRestrictionResponseList.from_json(json)
# print the JSON string representation of the object
print JobDeploymentRestrictionResponseList.to_json()

# convert the object into a dict
job_deployment_restriction_response_list_dict = job_deployment_restriction_response_list_instance.to_dict()
# create an instance of JobDeploymentRestrictionResponseList from a dict
job_deployment_restriction_response_list_form_dict = job_deployment_restriction_response_list.from_dict(job_deployment_restriction_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


