# OrganizationWebhookCreateResponseAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | [**OrganizationWebhookKindEnum**](OrganizationWebhookKindEnum.md) |  | [optional] 
**target_url** | **str** | Set the public HTTP or HTTPS endpoint that will receive the specified events. The target URL must starts with &#x60;http://&#x60; or &#x60;https://&#x60;  | [optional] 
**target_secret_set** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**enabled** | **bool** | Turn on or off your endpoint. | [optional] 
**events** | [**[OrganizationWebhookEventEnum]**](OrganizationWebhookEventEnum.md) |  | [optional] 
**project_names_filter** | **[str]** |  | [optional] 
**environment_types_filter** | [**[EnvironmentModeEnum]**](EnvironmentModeEnum.md) | Specify the environment modes you want to filter to. This webhook will be triggered only if the event is coming from an environment with the specified mode.  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


