# qovery.ApplicationEventApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_application_event**](ApplicationEventApi.md#list_application_event) | **GET** /application/{applicationId}/event | List application events


# **list_application_event**
> EventPaginatedResponseList list_application_event(application_id)

List application events

By default it returns the 20 last results. The response is paginated. In order to request the next page, you can use the startId query parameter

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import application_event_api
from qovery.model.event_paginated_response_list import EventPaginatedResponseList
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
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = qovery.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with qovery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = application_event_api.ApplicationEventApi(api_client)
    application_id = "applicationId_example" # str | Application ID
    start_id = "startId_example" # str | Starting point after which to return results (optional)

    # example passing only required values which don't have defaults set
    try:
        # List application events
        api_response = api_instance.list_application_event(application_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationEventApi->list_application_event: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List application events
        api_response = api_instance.list_application_event(application_id, start_id=start_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationEventApi->list_application_event: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID |
 **start_id** | **str**| Starting point after which to return results | [optional]

### Return type

[**EventPaginatedResponseList**](EventPaginatedResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List events |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

