# OrganizationApiTokenCreateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**scope** | [**OrganizationApiTokenScope**](OrganizationApiTokenScope.md) |  | [optional] 
**role_id** | **str** | the roleId provided by the \&quot;List organization custom roles\&quot; endpoint. | 

## Example

```python
from qovery.models.organization_api_token_create_request import OrganizationApiTokenCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationApiTokenCreateRequest from a JSON string
organization_api_token_create_request_instance = OrganizationApiTokenCreateRequest.from_json(json)
# print the JSON string representation of the object
print OrganizationApiTokenCreateRequest.to_json()

# convert the object into a dict
organization_api_token_create_request_dict = organization_api_token_create_request_instance.to_dict()
# create an instance of OrganizationApiTokenCreateRequest from a dict
organization_api_token_create_request_form_dict = organization_api_token_create_request.from_dict(organization_api_token_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


