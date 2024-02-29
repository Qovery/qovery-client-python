# OrganizationEventTargetResponseList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**targets** | [**List[ClusterCloudProviderInfoCredentials]**](ClusterCloudProviderInfoCredentials.md) |  | [optional] 

## Example

```python
from qovery.models.organization_event_target_response_list import OrganizationEventTargetResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationEventTargetResponseList from a JSON string
organization_event_target_response_list_instance = OrganizationEventTargetResponseList.from_json(json)
# print the JSON string representation of the object
print OrganizationEventTargetResponseList.to_json()

# convert the object into a dict
organization_event_target_response_list_dict = organization_event_target_response_list_instance.to_dict()
# create an instance of OrganizationEventTargetResponseList from a dict
organization_event_target_response_list_form_dict = organization_event_target_response_list.from_dict(organization_event_target_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


