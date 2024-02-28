# OrganizationEventResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**event_type** | [**OrganizationEventType**](OrganizationEventType.md) |  | [optional] 
**target_id** | **str** |  | [optional] 
**target_name** | **str** |  | [optional] 
**target_type** | [**OrganizationEventTargetType**](OrganizationEventTargetType.md) |  | [optional] 
**sub_target_type** | [**OrganizationEventSubTargetType**](OrganizationEventSubTargetType.md) |  | [optional] 
**change** | **str** |  | [optional] 
**origin** | [**OrganizationEventOrigin**](OrganizationEventOrigin.md) |  | [optional] 
**triggered_by** | **str** |  | [optional] 
**project_id** | **str** |  | [optional] 
**project_name** | **str** |  | [optional] 
**environment_id** | **str** |  | [optional] 
**environment_name** | **str** |  | [optional] 

## Example

```python
from qovery.models.organization_event_response import OrganizationEventResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationEventResponse from a JSON string
organization_event_response_instance = OrganizationEventResponse.from_json(json)
# print the JSON string representation of the object
print OrganizationEventResponse.to_json()

# convert the object into a dict
organization_event_response_dict = organization_event_response_instance.to_dict()
# create an instance of OrganizationEventResponse from a dict
organization_event_response_form_dict = organization_event_response.from_dict(organization_event_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


