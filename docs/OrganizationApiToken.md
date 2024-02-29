# OrganizationApiToken


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**role_name** | **str** |  | [optional] 
**role_id** | **str** |  | [optional] 

## Example

```python
from qovery.models.organization_api_token import OrganizationApiToken

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationApiToken from a JSON string
organization_api_token_instance = OrganizationApiToken.from_json(json)
# print the JSON string representation of the object
print OrganizationApiToken.to_json()

# convert the object into a dict
organization_api_token_dict = organization_api_token_instance.to_dict()
# create an instance of OrganizationApiToken from a dict
organization_api_token_form_dict = organization_api_token.from_dict(organization_api_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


