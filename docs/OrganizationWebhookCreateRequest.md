# OrganizationWebhookCreateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | Define the type of the webhook. &#x60;SLACK&#x60; is a special webhook type to push notifications directly to slack. The &#x60;target_url&#x60; must be a Slack compatible endpoint. | 
**target_url** | **str** | Set the public HTTP or HTTPS endpoint that will receive the specified events. The target URL must starts with &#x60;http://&#x60; or &#x60;https://&#x60;  | 
**events** | **[str]** |  | 
**target_secret** | **str** | Make sure you receive a payload to sign the Qovery request with your secret. Qovery will add a HTTP header &#x60;Qovery-Signature: &lt;Your Secret&gt;&#x60; to every webhook requests sent to your target URL.  | [optional] 
**description** | **str** |  | [optional] 
**enabled** | **bool** | Turn on or off your endpoint. | [optional] 
**project_id_filter** | **[str]** |  | [optional] 
**environment_types_filter** | [**[EnvironmentModeEnum]**](EnvironmentModeEnum.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


