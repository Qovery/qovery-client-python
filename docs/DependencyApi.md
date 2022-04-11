# qovery.DependencyApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_application_dependency**](DependencyApi.md#create_application_dependency) | **POST** /application/{applicationId}/dependency/{targetApplicationId} | Add application dependency to this application.
[**list_application_dependency**](DependencyApi.md#list_application_dependency) | **GET** /application/{applicationId}/dependency | List application dependencies
[**remove_application_dependency**](DependencyApi.md#remove_application_dependency) | **DELETE** /application/{applicationId}/dependency/{targetApplicationId} | Remove application dependency to this application.


# **create_application_dependency**
> Application create_application_dependency(application_id, target_application_id)

Add application dependency to this application.

Add application dependency to this application to prevent this application starting before the linked dependencies

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import dependency_api
from qovery.model.application import Application
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
    api_instance = dependency_api.DependencyApi(api_client)
    application_id = "applicationId_example" # str | Application ID
    target_application_id = "targetApplicationId_example" # str | Target application ID

    # example passing only required values which don't have defaults set
    try:
        # Add application dependency to this application.
        api_response = api_instance.create_application_dependency(application_id, target_application_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling DependencyApi->create_application_dependency: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID |
 **target_application_id** | **str**| Target application ID |

### Return type

[**Application**](Application.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Add application dependencies |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_application_dependency**
> ApplicationResponseList list_application_dependency(application_id)

List application dependencies

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import dependency_api
from qovery.model.application_response_list import ApplicationResponseList
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
    api_instance = dependency_api.DependencyApi(api_client)
    application_id = "applicationId_example" # str | Application ID

    # example passing only required values which don't have defaults set
    try:
        # List application dependencies
        api_response = api_instance.list_application_dependency(application_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling DependencyApi->list_application_dependency: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID |

### Return type

[**ApplicationResponseList**](ApplicationResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List dependencies |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_application_dependency**
> remove_application_dependency(application_id, target_application_id)

Remove application dependency to this application.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import dependency_api
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
    api_instance = dependency_api.DependencyApi(api_client)
    application_id = "applicationId_example" # str | Application ID
    target_application_id = "targetApplicationId_example" # str | Target application ID

    # example passing only required values which don't have defaults set
    try:
        # Remove application dependency to this application.
        api_instance.remove_application_dependency(application_id, target_application_id)
    except qovery.ApiException as e:
        print("Exception when calling DependencyApi->remove_application_dependency: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID |
 **target_application_id** | **str**| Target application ID |

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was deleted successfully |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

