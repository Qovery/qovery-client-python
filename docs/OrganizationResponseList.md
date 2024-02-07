# OrganizationResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Organization]**](Organization.md) |  | [optional] 

## Example

```python
from qovery.models.organization_response_list import OrganizationResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationResponseList from a JSON string
organization_response_list_instance = OrganizationResponseList.from_json(json)
# print the JSON string representation of the object
print OrganizationResponseList.to_json()

# convert the object into a dict
organization_response_list_dict = organization_response_list_instance.to_dict()
# create an instance of OrganizationResponseList from a dict
organization_response_list_form_dict = organization_response_list.from_dict(organization_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


