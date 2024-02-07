# OrganizationWebhookCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**kind** | [**OrganizationWebhookKindEnum**](OrganizationWebhookKindEnum.md) |  | [optional] 
**target_url** | **str** | Set the public HTTP or HTTPS endpoint that will receive the specified events. The target URL must starts with &#x60;http://&#x60; or &#x60;https://&#x60;  | [optional] 
**target_secret_set** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**enabled** | **bool** | Turn on or off your endpoint. | [optional] 
**events** | [**List[OrganizationWebhookEventEnum]**](OrganizationWebhookEventEnum.md) |  | [optional] 
**project_names_filter** | **List[str]** | Specify the project names you want to filter to.  This webhook will be triggered only if the event is coming from the specified Project IDs. Notes: 1. Wildcard is accepted E.g. &#x60;product*&#x60;. 2. Name is case insensitive.  | [optional] 
**environment_types_filter** | [**List[EnvironmentModeEnum]**](EnvironmentModeEnum.md) | Specify the environment modes you want to filter to. This webhook will be triggered only if the event is coming from an environment with the specified mode.  | [optional] 

## Example

```python
from qovery.models.organization_webhook_create_response import OrganizationWebhookCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationWebhookCreateResponse from a JSON string
organization_webhook_create_response_instance = OrganizationWebhookCreateResponse.from_json(json)
# print the JSON string representation of the object
print OrganizationWebhookCreateResponse.to_json()

# convert the object into a dict
organization_webhook_create_response_dict = organization_webhook_create_response_instance.to_dict()
# create an instance of OrganizationWebhookCreateResponse from a dict
organization_webhook_create_response_form_dict = organization_webhook_create_response.from_dict(organization_webhook_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


