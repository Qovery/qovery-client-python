# OrganizationWebhookCreateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | [**OrganizationWebhookKindEnum**](OrganizationWebhookKindEnum.md) |  | 
**target_url** | **str** | Set the public HTTP or HTTPS endpoint that will receive the specified events. The target URL must starts with &#x60;http://&#x60; or &#x60;https://&#x60;  | 
**target_secret** | **str** | Make sure you receive a payload to sign the Qovery request with your secret. Qovery will add a HTTP header &#x60;Qovery-Signature: &lt;Your Secret&gt;&#x60; to every webhook requests sent to your target URL.  | [optional] 
**description** | **str** |  | [optional] 
**enabled** | **bool** | Turn on or off your endpoint. | [optional] 
**events** | [**List[OrganizationWebhookEventEnum]**](OrganizationWebhookEventEnum.md) |  | 
**project_names_filter** | **List[str]** | Specify the project names you want to filter to.  This webhook will be triggered only if the event is coming from the specified Project IDs. Notes: 1. Wildcard is accepted E.g. &#x60;product*&#x60;. 2. Name is case insensitive.  | [optional] 
**environment_types_filter** | [**List[EnvironmentModeEnum]**](EnvironmentModeEnum.md) | Specify the environment modes you want to filter to. This webhook will be triggered only if the event is coming from an environment with the specified mode.  | [optional] 

## Example

```python
from qovery.models.organization_webhook_create_request import OrganizationWebhookCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationWebhookCreateRequest from a JSON string
organization_webhook_create_request_instance = OrganizationWebhookCreateRequest.from_json(json)
# print the JSON string representation of the object
print OrganizationWebhookCreateRequest.to_json()

# convert the object into a dict
organization_webhook_create_request_dict = organization_webhook_create_request_instance.to_dict()
# create an instance of OrganizationWebhookCreateRequest from a dict
organization_webhook_create_request_form_dict = organization_webhook_create_request.from_dict(organization_webhook_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


