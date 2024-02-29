# qovery.OrganizationEventApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_organization_event_targets**](OrganizationEventApi.md#get_organization_event_targets) | **GET** /organization/{organizationId}/targets | Get available event targets to filter events
[**get_organization_events**](OrganizationEventApi.md#get_organization_events) | **GET** /organization/{organizationId}/events | Get all events inside the organization


# **get_organization_event_targets**
> OrganizationEventTargetResponseList get_organization_event_targets(organization_id, from_timestamp=from_timestamp, to_timestamp=to_timestamp, event_type=event_type, target_type=target_type, triggered_by=triggered_by, origin=origin, project_id=project_id, environment_id=environment_id)

Get available event targets to filter events

Get available event targets to filter events

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import qovery
from qovery.models.organization_event_origin import OrganizationEventOrigin
from qovery.models.organization_event_target_response_list import OrganizationEventTargetResponseList
from qovery.models.organization_event_target_type import OrganizationEventTargetType
from qovery.models.organization_event_type import OrganizationEventType
from qovery.rest import ApiException
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

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = qovery.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qovery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qovery.OrganizationEventApi(api_client)
    organization_id = 'organization_id_example' # str | Organization ID
    from_timestamp = 'from_timestamp_example' # str | Display targets available since this timestamp.   A range of date can be specified by using `from-timestamp` with `to-timestamp` The format is a timestamp with nano precision  (optional)
    to_timestamp = 'to_timestamp_example' # str | Display targets triggered before this timestamp.   A range of date can be specified by using `to-timestamp` with `from-timestamp` The format is a timestamp with nano precision  (optional)
    event_type = qovery.OrganizationEventType() # OrganizationEventType |  (optional)
    target_type = qovery.OrganizationEventTargetType() # OrganizationEventTargetType |  (optional)
    triggered_by = 'triggered_by_example' # str | Information about the owner of the event (user name / apitoken / automatic action) (optional)
    origin = qovery.OrganizationEventOrigin() # OrganizationEventOrigin |  (optional)
    project_id = 'project_id_example' # str | Mandatory when requesting an environment or a service (optional)
    environment_id = 'environment_id_example' # str | Mandatory when requesting a service (optional)

    try:
        # Get available event targets to filter events
        api_response = api_instance.get_organization_event_targets(organization_id, from_timestamp=from_timestamp, to_timestamp=to_timestamp, event_type=event_type, target_type=target_type, triggered_by=triggered_by, origin=origin, project_id=project_id, environment_id=environment_id)
        print("The response of OrganizationEventApi->get_organization_event_targets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationEventApi->get_organization_event_targets: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID | 
 **from_timestamp** | **str**| Display targets available since this timestamp.   A range of date can be specified by using &#x60;from-timestamp&#x60; with &#x60;to-timestamp&#x60; The format is a timestamp with nano precision  | [optional] 
 **to_timestamp** | **str**| Display targets triggered before this timestamp.   A range of date can be specified by using &#x60;to-timestamp&#x60; with &#x60;from-timestamp&#x60; The format is a timestamp with nano precision  | [optional] 
 **event_type** | [**OrganizationEventType**](.md)|  | [optional] 
 **target_type** | [**OrganizationEventTargetType**](.md)|  | [optional] 
 **triggered_by** | **str**| Information about the owner of the event (user name / apitoken / automatic action) | [optional] 
 **origin** | [**OrganizationEventOrigin**](.md)|  | [optional] 
 **project_id** | **str**| Mandatory when requesting an environment or a service | [optional] 
 **environment_id** | **str**| Mandatory when requesting a service | [optional] 

### Return type

[**OrganizationEventTargetResponseList**](OrganizationEventTargetResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

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
> OrganizationEventResponseList get_organization_events(organization_id, page_size=page_size, from_timestamp=from_timestamp, to_timestamp=to_timestamp, continue_token=continue_token, step_back_token=step_back_token, event_type=event_type, target_type=target_type, target_id=target_id, sub_target_type=sub_target_type, triggered_by=triggered_by, origin=origin)

Get all events inside the organization

Get all events inside the organization

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import qovery
from qovery.models.organization_event_origin import OrganizationEventOrigin
from qovery.models.organization_event_response_list import OrganizationEventResponseList
from qovery.models.organization_event_sub_target_type import OrganizationEventSubTargetType
from qovery.models.organization_event_target_type import OrganizationEventTargetType
from qovery.models.organization_event_type import OrganizationEventType
from qovery.rest import ApiException
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

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = qovery.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qovery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qovery.OrganizationEventApi(api_client)
    organization_id = 'organization_id_example' # str | Organization ID
    page_size = 10 # float | The number of events to display in the current page (optional) (default to 10)
    from_timestamp = 'from_timestamp_example' # str | Display events triggered since this timestamp.   A range of date can be specified by using `from-timestamp` with `to-timestamp` The format is a timestamp with nano precision  (optional)
    to_timestamp = 'to_timestamp_example' # str | Display events triggered before this timestamp.   A range of date can be specified by using `to-timestamp` with `from-timestamp` The format is a timestamp with nano precision  (optional)
    continue_token = 'continue_token_example' # str | Token used to fetch the next page results The format is a timestamp with nano precision  (optional)
    step_back_token = 'step_back_token_example' # str | Token used to fetch the previous page results The format is a timestamp with nano precision  (optional)
    event_type = qovery.OrganizationEventType() # OrganizationEventType |  (optional)
    target_type = qovery.OrganizationEventTargetType() # OrganizationEventTargetType |  (optional)
    target_id = 'target_id_example' # str | The target resource id to search.   Must be specified with the corresponding `target_type`  (optional)
    sub_target_type = qovery.OrganizationEventSubTargetType() # OrganizationEventSubTargetType |  (optional)
    triggered_by = 'triggered_by_example' # str | Information about the owner of the event (user name / apitoken / automatic action) (optional)
    origin = qovery.OrganizationEventOrigin() # OrganizationEventOrigin |  (optional)

    try:
        # Get all events inside the organization
        api_response = api_instance.get_organization_events(organization_id, page_size=page_size, from_timestamp=from_timestamp, to_timestamp=to_timestamp, continue_token=continue_token, step_back_token=step_back_token, event_type=event_type, target_type=target_type, target_id=target_id, sub_target_type=sub_target_type, triggered_by=triggered_by, origin=origin)
        print("The response of OrganizationEventApi->get_organization_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationEventApi->get_organization_events: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID | 
 **page_size** | **float**| The number of events to display in the current page | [optional] [default to 10]
 **from_timestamp** | **str**| Display events triggered since this timestamp.   A range of date can be specified by using &#x60;from-timestamp&#x60; with &#x60;to-timestamp&#x60; The format is a timestamp with nano precision  | [optional] 
 **to_timestamp** | **str**| Display events triggered before this timestamp.   A range of date can be specified by using &#x60;to-timestamp&#x60; with &#x60;from-timestamp&#x60; The format is a timestamp with nano precision  | [optional] 
 **continue_token** | **str**| Token used to fetch the next page results The format is a timestamp with nano precision  | [optional] 
 **step_back_token** | **str**| Token used to fetch the previous page results The format is a timestamp with nano precision  | [optional] 
 **event_type** | [**OrganizationEventType**](.md)|  | [optional] 
 **target_type** | [**OrganizationEventTargetType**](.md)|  | [optional] 
 **target_id** | **str**| The target resource id to search.   Must be specified with the corresponding &#x60;target_type&#x60;  | [optional] 
 **sub_target_type** | [**OrganizationEventSubTargetType**](.md)|  | [optional] 
 **triggered_by** | **str**| Information about the owner of the event (user name / apitoken / automatic action) | [optional] 
 **origin** | [**OrganizationEventOrigin**](.md)|  | [optional] 

### Return type

[**OrganizationEventResponseList**](OrganizationEventResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

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

