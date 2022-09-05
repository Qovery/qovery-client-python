# qovery.EnvironmentsApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_environment**](EnvironmentsApi.md#create_environment) | **POST** /project/{projectId}/environment | Create an environment
[**get_project_environment_service_number**](EnvironmentsApi.md#get_project_environment_service_number) | **GET** /project/{projectId}/environment/stats | List total number of services for each environment of the project
[**get_project_environments_status**](EnvironmentsApi.md#get_project_environments_status) | **GET** /project/{projectId}/environment/status | List environments statuses
[**list_environment**](EnvironmentsApi.md#list_environment) | **GET** /project/{projectId}/environment | List environments


# **create_environment**
> Environment create_environment(project_id)

Create an environment

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import environments_api
from qovery.model.environment import Environment
from qovery.model.create_environment_request import CreateEnvironmentRequest
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
    api_instance = environments_api.EnvironmentsApi(api_client)
    project_id = "projectId_example" # str | Project ID
    create_environment_request = CreateEnvironmentRequest(
        name="name_example",
        cluster="cluster_example",
        mode=CreateEnvironmentModeEnum("PRODUCTION"),
    ) # CreateEnvironmentRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create an environment
        api_response = api_instance.create_environment(project_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling EnvironmentsApi->create_environment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an environment
        api_response = api_instance.create_environment(project_id, create_environment_request=create_environment_request)
        pprint(api_response)
    except qovery.ApiException as e:
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

[bearerAuth](../README.md#bearerAuth)

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

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import environments_api
from qovery.model.environment_stats_response_list import EnvironmentStatsResponseList
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
    api_instance = environments_api.EnvironmentsApi(api_client)
    project_id = "projectId_example" # str | Project ID

    # example passing only required values which don't have defaults set
    try:
        # List total number of services for each environment of the project
        api_response = api_instance.get_project_environment_service_number(project_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling EnvironmentsApi->get_project_environment_service_number: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID |

### Return type

[**EnvironmentStatsResponseList**](EnvironmentStatsResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

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

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import environments_api
from qovery.model.environment_status_list import EnvironmentStatusList
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
    api_instance = environments_api.EnvironmentsApi(api_client)
    project_id = "projectId_example" # str | Project ID

    # example passing only required values which don't have defaults set
    try:
        # List environments statuses
        api_response = api_instance.get_project_environments_status(project_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling EnvironmentsApi->get_project_environments_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID |

### Return type

[**EnvironmentStatusList**](EnvironmentStatusList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

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

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import environments_api
from qovery.model.environment_response_list import EnvironmentResponseList
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
    api_instance = environments_api.EnvironmentsApi(api_client)
    project_id = "projectId_example" # str | Project ID

    # example passing only required values which don't have defaults set
    try:
        # List environments
        api_response = api_instance.list_environment(project_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling EnvironmentsApi->list_environment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID |

### Return type

[**EnvironmentResponseList**](EnvironmentResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

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

