# qovery.EnvironmentsApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_environment**](EnvironmentsApi.md#create_environment) | **POST** /project/{projectId}/environment | Create an environment
[**get_project_environment_service_number**](EnvironmentsApi.md#get_project_environment_service_number) | **GET** /project/{projectId}/environment/stats | List total number of services for each environment of the project
[**get_project_environments_status**](EnvironmentsApi.md#get_project_environments_status) | **GET** /project/{projectId}/environment/status | List environments statuses
[**list_environment**](EnvironmentsApi.md#list_environment) | **GET** /project/{projectId}/environment | List environments


# **create_environment**
> Environment create_environment(project_id, create_environment_request=create_environment_request)

Create an environment

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import qovery
from qovery.models.create_environment_request import CreateEnvironmentRequest
from qovery.models.environment import Environment
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
    api_instance = qovery.EnvironmentsApi(api_client)
    project_id = 'project_id_example' # str | Project ID
    create_environment_request = qovery.CreateEnvironmentRequest() # CreateEnvironmentRequest |  (optional)

    try:
        # Create an environment
        api_response = api_instance.create_environment(project_id, create_environment_request=create_environment_request)
        print("The response of EnvironmentsApi->create_environment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentsApi->create_environment: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 
 **create_environment_request** | [**CreateEnvironmentRequest**](CreateEnvironmentRequest.md)|  | [optional] 

### Return type

[**Environment**](Environment.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create environment |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Environment name within the project is already taken |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_environment_service_number**
> EnvironmentStatsResponseList get_project_environment_service_number(project_id)

List total number of services for each environment of the project

Returns a list of environment ids, and for each its total numberof services

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import qovery
from qovery.models.environment_stats_response_list import EnvironmentStatsResponseList
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
    api_instance = qovery.EnvironmentsApi(api_client)
    project_id = 'project_id_example' # str | Project ID

    try:
        # List total number of services for each environment of the project
        api_response = api_instance.get_project_environment_service_number(project_id)
        print("The response of EnvironmentsApi->get_project_environment_service_number:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentsApi->get_project_environment_service_number: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 

### Return type

[**EnvironmentStatsResponseList**](EnvironmentStatsResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get number of services |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_environments_status**
> EnvironmentStatusList get_project_environments_status(project_id)

List environments statuses

Returns a list of environments with only their id and status.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import qovery
from qovery.models.environment_status_list import EnvironmentStatusList
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
    api_instance = qovery.EnvironmentsApi(api_client)
    project_id = 'project_id_example' # str | Project ID

    try:
        # List environments statuses
        api_response = api_instance.get_project_environments_status(project_id)
        print("The response of EnvironmentsApi->get_project_environments_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentsApi->get_project_environments_status: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 

### Return type

[**EnvironmentStatusList**](EnvironmentStatusList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get status |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_environment**
> EnvironmentResponseList list_environment(project_id)

List environments

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import qovery
from qovery.models.environment_response_list import EnvironmentResponseList
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
    api_instance = qovery.EnvironmentsApi(api_client)
    project_id = 'project_id_example' # str | Project ID

    try:
        # List environments
        api_response = api_instance.list_environment(project_id)
        print("The response of EnvironmentsApi->list_environment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentsApi->list_environment: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID | 

### Return type

[**EnvironmentResponseList**](EnvironmentResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List environments |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

