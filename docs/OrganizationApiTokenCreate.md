# OrganizationApiTokenCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**token** | **str** | the generated token to send in &#39;Authorization&#39; header prefixed by &#39;Token &#39; | [optional] 
**role_name** | **str** |  | [optional] 
**role_id** | **str** |  | [optional] 

## Example

```python
from qovery.models.organization_api_token_create import OrganizationApiTokenCreate

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationApiTokenCreate from a JSON string
organization_api_token_create_instance = OrganizationApiTokenCreate.from_json(json)
# print the JSON string representation of the object
print OrganizationApiTokenCreate.to_json()

# convert the object into a dict
organization_api_token_create_dict = organization_api_token_create_instance.to_dict()
# create an instance of OrganizationApiTokenCreate from a dict
organization_api_token_create_form_dict = organization_api_token_create.from_dict(organization_api_token_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


