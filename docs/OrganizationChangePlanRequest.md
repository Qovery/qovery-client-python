# OrganizationChangePlanRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan** | **str** |  | [optional] 

## Example

```python
from qovery.models.organization_change_plan_request import OrganizationChangePlanRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationChangePlanRequest from a JSON string
organization_change_plan_request_instance = OrganizationChangePlanRequest.from_json(json)
# print the JSON string representation of the object
print OrganizationChangePlanRequest.to_json()

# convert the object into a dict
organization_change_plan_request_dict = organization_change_plan_request_instance.to_dict()
# create an instance of OrganizationChangePlanRequest from a dict
organization_change_plan_request_form_dict = organization_change_plan_request.from_dict(organization_change_plan_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


