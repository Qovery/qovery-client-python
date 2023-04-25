# qovery.OrganizationEventApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_organization_events**](OrganizationEventApi.md#get_organization_events) | **GET** /organization/{organizationId}/events | Get all events inside the organization


# **get_organization_events**
> OrganizationEventResponseList get_organization_events(organization_id)

Get all events inside the organization

Get all events inside the organization

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import organization_event_api
from qovery.model.organization_event_response_list import OrganizationEventResponseList
from qovery.model.organization_event_target_type import OrganizationEventTargetType
from qovery.model.organization_event_type import OrganizationEventType
from qovery.model.organization_event_sub_target_type import OrganizationEventSubTargetType
from qovery.model.organization_event_origin import OrganizationEventOrigin
from pprint import pprint
# Defining the host is optional and defaults to https://api.qovery.com
# See configuration.py for a list of all supported configuration parameters.
configuration = qovery.Configuration(
    host = "https://api.qovery.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = qovery.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with qovery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = organization_event_api.OrganizationEventApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    from_timestamp = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Display events triggered since this timestamp.   A range of date can be specified by using `from-timestamp` with `to-timestamp`  (optional)
    to_timestamp = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Display events triggered before this timestamp.   A range of date can be specified by using `to-timestamp` with `from-timestamp`  (optional)
    event_type = OrganizationEventType("CREATE") # OrganizationEventType |  (optional)
    target_type = OrganizationEventTargetType("APPLICATION") # OrganizationEventTargetType |  (optional)
    target_id = "target_id_example" # str |  (optional)
    sub_target = OrganizationEventSubTargetType("ADVANCED_SETTINGS") # OrganizationEventSubTargetType |  (optional)
    user = "user_example" # str | The username who has triggered the action (optional)
    origin = OrganizationEventOrigin("API") # OrganizationEventOrigin |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all events inside the organization
        api_response = api_instance.get_organization_events(organization_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling OrganizationEventApi->get_organization_events: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all events inside the organization
        api_response = api_instance.get_organization_events(organization_id, from_timestamp=from_timestamp, to_timestamp=to_timestamp, event_type=event_type, target_type=target_type, target_id=target_id, sub_target=sub_target, user=user, origin=origin)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling OrganizationEventApi->get_organization_events: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **from_timestamp** | **datetime**| Display events triggered since this timestamp.   A range of date can be specified by using &#x60;from-timestamp&#x60; with &#x60;to-timestamp&#x60;  | [optional]
 **to_timestamp** | **datetime**| Display events triggered before this timestamp.   A range of date can be specified by using &#x60;to-timestamp&#x60; with &#x60;from-timestamp&#x60;  | [optional]
 **event_type** | **OrganizationEventType**|  | [optional]
 **target_type** | **OrganizationEventTargetType**|  | [optional]
 **target_id** | **str**|  | [optional]
 **sub_target** | **OrganizationEventSubTargetType**|  | [optional]
 **user** | **str**| The username who has triggered the action | [optional]
 **origin** | **OrganizationEventOrigin**|  | [optional]

### Return type

[**OrganizationEventResponseList**](OrganizationEventResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get organization events |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

