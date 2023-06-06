# qovery.EnvironmentLogsApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_environment_log**](EnvironmentLogsApi.md#list_environment_log) | **GET** /environment/{environmentId}/log | List environment deployment logs
[**list_environment_logs**](EnvironmentLogsApi.md#list_environment_logs) | **GET** /environment/{environmentId}/logs | List environment deployment logs v2


# **list_environment_log**
> EnvironmentLogResponseList list_environment_log(environment_id)

List environment deployment logs

This returns the last 1000 environment deployment logs.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import environment_logs_api
from qovery.model.environment_log_response_list import EnvironmentLogResponseList
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
    api_instance = environment_logs_api.EnvironmentLogsApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID

    # example passing only required values which don't have defaults set
    try:
        # List environment deployment logs
        api_response = api_instance.list_environment_log(environment_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling EnvironmentLogsApi->list_environment_log: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID |

### Return type

[**EnvironmentLogResponseList**](EnvironmentLogResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List logs |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_environment_logs**
> EnvironmentLogsResponseList list_environment_logs(environment_id)

List environment deployment logs v2

This returns the last 1000 environment deployment logs v2

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import environment_logs_api
from qovery.model.environment_logs_response_list import EnvironmentLogsResponseList
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
    api_instance = environment_logs_api.EnvironmentLogsApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID
    version = "version_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List environment deployment logs v2
        api_response = api_instance.list_environment_logs(environment_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling EnvironmentLogsApi->list_environment_logs: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List environment deployment logs v2
        api_response = api_instance.list_environment_logs(environment_id, version=version)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling EnvironmentLogsApi->list_environment_logs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID |
 **version** | **str**|  | [optional]

### Return type

[**EnvironmentLogsResponseList**](EnvironmentLogsResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List logs v2 |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

