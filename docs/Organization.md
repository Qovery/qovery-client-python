# Organization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**name** | **str** | name is case insensitive | 
**description** | **str** |  | [optional] 
**plan** | [**PlanEnum**](PlanEnum.md) |  | 
**website_url** | **str** |  | [optional] 
**repository** | **str** |  | [optional] 
**logo_url** | **str** |  | [optional] 
**icon_url** | **str** |  | [optional] 
**admin_emails** | **List[str]** |  | [optional] 
**owner** | **str** | uuid of the user owning the organization | [optional] 

## Example

```python
from qovery.models.organization import Organization

# TODO update the JSON string below
json = "{}"
# create an instance of Organization from a JSON string
organization_instance = Organization.from_json(json)
# print the JSON string representation of the object
print Organization.to_json()

# convert the object into a dict
organization_dict = organization_instance.to_dict()
# create an instance of Organization from a dict
organization_form_dict = organization.from_dict(organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


