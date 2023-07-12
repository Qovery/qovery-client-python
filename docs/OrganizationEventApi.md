# qovery.OrganizationEventApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_organization_event_targets**](OrganizationEventApi.md#get_organization_event_targets) | **GET** /organization/{organizationId}/targets | Get available event targets to filter events
[**get_organization_events**](OrganizationEventApi.md#get_organization_events) | **GET** /organization/{organizationId}/events | Get all events inside the organization


# **get_organization_event_targets**
> GetOrganizationEventTargets200Response get_organization_event_targets(organization_id)

Get available event targets to filter events

Get available event targets to filter events

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import organization_event_api
from qovery.model.organization_event_target_type import OrganizationEventTargetType
from qovery.model.organization_event_type import OrganizationEventType
from qovery.model.get_organization_event_targets200_response import GetOrganizationEventTargets200Response
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
    from_timestamp = "fromTimestamp_example" # str, none_type | Display targets available since this timestamp.   A range of date can be specified by using `from-timestamp` with `to-timestamp` The format is a timestamp with nano precision  (optional)
    to_timestamp = "toTimestamp_example" # str, none_type | Display targets triggered before this timestamp.   A range of date can be specified by using `to-timestamp` with `from-timestamp` The format is a timestamp with nano precision  (optional)
    event_type = OrganizationEventType("CREATE") # OrganizationEventType |  (optional)
    target_type = OrganizationEventTargetType("APPLICATION") # OrganizationEventTargetType |  (optional)
    triggered_by = "triggeredBy_example" # str | Information about the owner of the event (user name / apitoken / automatic action) (optional)
    origin = OrganizationEventOrigin("API") # OrganizationEventOrigin |  (optional)
    project_id = "projectId_example" # str | Mandatory when requesting an environment or a service (optional)
    environment_id = "environmentId_example" # str | Mandatory when requesting a service (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get available event targets to filter events
        api_response = api_instance.get_organization_event_targets(organization_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling OrganizationEventApi->get_organization_event_targets: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get available event targets to filter events
        api_response = api_instance.get_organization_event_targets(organization_id, from_timestamp=from_timestamp, to_timestamp=to_timestamp, event_type=event_type, target_type=target_type, triggered_by=triggered_by, origin=origin, project_id=project_id, environment_id=environment_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling OrganizationEventApi->get_organization_event_targets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **from_timestamp** | **str, none_type**| Display targets available since this timestamp.   A range of date can be specified by using &#x60;from-timestamp&#x60; with &#x60;to-timestamp&#x60; The format is a timestamp with nano precision  | [optional]
 **to_timestamp** | **str, none_type**| Display targets triggered before this timestamp.   A range of date can be specified by using &#x60;to-timestamp&#x60; with &#x60;from-timestamp&#x60; The format is a timestamp with nano precision  | [optional]
 **event_type** | **OrganizationEventType**|  | [optional]
 **target_type** | **OrganizationEventTargetType**|  | [optional]
 **triggered_by** | **str**| Information about the owner of the event (user name / apitoken / automatic action) | [optional]
 **origin** | **OrganizationEventOrigin**|  | [optional]
 **project_id** | **str**| Mandatory when requesting an environment or a service | [optional]
 **environment_id** | **str**| Mandatory when requesting a service | [optional]

### Return type

[**GetOrganizationEventTargets200Response**](GetOrganizationEventTargets200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get organization event targets |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
    page_size = 10 # float, none_type | The number of events to display in the current page (optional) if omitted the server will use the default value of 10
    from_timestamp = "fromTimestamp_example" # str, none_type | Display events triggered since this timestamp.   A range of date can be specified by using `from-timestamp` with `to-timestamp` The format is a timestamp with nano precision  (optional)
    to_timestamp = "toTimestamp_example" # str, none_type | Display events triggered before this timestamp.   A range of date can be specified by using `to-timestamp` with `from-timestamp` The format is a timestamp with nano precision  (optional)
    continue_token = "continueToken_example" # str | Token used to fetch the next page results The format is a timestamp with nano precision  (optional)
    step_back_token = "stepBackToken_example" # str | Token used to fetch the previous page results The format is a timestamp with nano precision  (optional)
    event_type = OrganizationEventType("CREATE") # OrganizationEventType |  (optional)
    target_type = OrganizationEventTargetType("APPLICATION") # OrganizationEventTargetType |  (optional)
    target_id = "targetId_example" # str, none_type | The target resource id to search.   Must be specified with the corresponding `target_type`  (optional)
    sub_target_type = OrganizationEventSubTargetType("ADVANCED_SETTINGS") # OrganizationEventSubTargetType |  (optional)
    triggered_by = "triggeredBy_example" # str | Information about the owner of the event (user name / apitoken / automatic action) (optional)
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
        api_response = api_instance.get_organization_events(organization_id, page_size=page_size, from_timestamp=from_timestamp, to_timestamp=to_timestamp, continue_token=continue_token, step_back_token=step_back_token, event_type=event_type, target_type=target_type, target_id=target_id, sub_target_type=sub_target_type, triggered_by=triggered_by, origin=origin)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling OrganizationEventApi->get_organization_events: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **page_size** | **float, none_type**| The number of events to display in the current page | [optional] if omitted the server will use the default value of 10
 **from_timestamp** | **str, none_type**| Display events triggered since this timestamp.   A range of date can be specified by using &#x60;from-timestamp&#x60; with &#x60;to-timestamp&#x60; The format is a timestamp with nano precision  | [optional]
 **to_timestamp** | **str, none_type**| Display events triggered before this timestamp.   A range of date can be specified by using &#x60;to-timestamp&#x60; with &#x60;from-timestamp&#x60; The format is a timestamp with nano precision  | [optional]
 **continue_token** | **str**| Token used to fetch the next page results The format is a timestamp with nano precision  | [optional]
 **step_back_token** | **str**| Token used to fetch the previous page results The format is a timestamp with nano precision  | [optional]
 **event_type** | **OrganizationEventType**|  | [optional]
 **target_type** | **OrganizationEventTargetType**|  | [optional]
 **target_id** | **str, none_type**| The target resource id to search.   Must be specified with the corresponding &#x60;target_type&#x60;  | [optional]
 **sub_target_type** | **OrganizationEventSubTargetType**|  | [optional]
 **triggered_by** | **str**| Information about the owner of the event (user name / apitoken / automatic action) | [optional]
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

