# OrganizationGithubAppConnectRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**installation_id** | **str** |  | 
**code** | **str** |  | 

## Example

```python
from qovery.models.organization_github_app_connect_request import OrganizationGithubAppConnectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationGithubAppConnectRequest from a JSON string
organization_github_app_connect_request_instance = OrganizationGithubAppConnectRequest.from_json(json)
# print the JSON string representation of the object
print OrganizationGithubAppConnectRequest.to_json()

# convert the object into a dict
organization_github_app_connect_request_dict = organization_github_app_connect_request_instance.to_dict()
# create an instance of OrganizationGithubAppConnectRequest from a dict
organization_github_app_connect_request_form_dict = organization_github_app_connect_request.from_dict(organization_github_app_connect_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


