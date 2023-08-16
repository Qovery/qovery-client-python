# qovery.EnvironmentMainCallsApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_environment**](EnvironmentMainCallsApi.md#delete_environment) | **DELETE** /environment/{environmentId} | Delete an environment
[**edit_environment**](EnvironmentMainCallsApi.md#edit_environment) | **PUT** /environment/{environmentId} | Edit an environment
[**get_environment**](EnvironmentMainCallsApi.md#get_environment) | **GET** /environment/{environmentId} | Get environment by ID
[**get_environment_status**](EnvironmentMainCallsApi.md#get_environment_status) | **GET** /environment/{environmentId}/status | Get environment status
[**get_environment_statuses**](EnvironmentMainCallsApi.md#get_environment_statuses) | **GET** /environment/{environmentId}/statuses | Get environment statuses with services status
[**get_environment_statuses_with_stages**](EnvironmentMainCallsApi.md#get_environment_statuses_with_stages) | **GET** /environment/{environmentId}/statusesWithStages | Get environment statuses with stages


# **delete_environment**
> delete_environment(environment_id)

Delete an environment

To delete an environment you must have the admin permission

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import environment_main_calls_api
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
    api_instance = environment_main_calls_api.EnvironmentMainCallsApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID

    # example passing only required values which don't have defaults set
    try:
        # Delete an environment
        api_instance.delete_environment(environment_id)
    except qovery.ApiException as e:
        print("Exception when calling EnvironmentMainCallsApi->delete_environment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID |

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

# **edit_environment**
> Environment edit_environment(environment_id)

Edit an environment

To edit an environment you must have the admin permission

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import environment_main_calls_api
from qovery.model.environment_edit_request import EnvironmentEditRequest
from qovery.model.environment import Environment
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
    api_instance = environment_main_calls_api.EnvironmentMainCallsApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID
    environment_edit_request = EnvironmentEditRequest(
        name="name_example",
        mode=CreateEnvironmentModeEnum("PRODUCTION"),
    ) # EnvironmentEditRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Edit an environment
        api_response = api_instance.edit_environment(environment_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling EnvironmentMainCallsApi->edit_environment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit an environment
        api_response = api_instance.edit_environment(environment_id, environment_edit_request=environment_edit_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling EnvironmentMainCallsApi->edit_environment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID |
 **environment_edit_request** | [**EnvironmentEditRequest**](EnvironmentEditRequest.md)|  | [optional]

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
**200** | Edit an environment |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Environment name within the project is already taken |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_environment**
> Environment get_environment(environment_id)

Get environment by ID

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import environment_main_calls_api
from qovery.model.environment import Environment
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
    api_instance = environment_main_calls_api.EnvironmentMainCallsApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID

    # example passing only required values which don't have defaults set
    try:
        # Get environment by ID
        api_response = api_instance.get_environment(environment_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling EnvironmentMainCallsApi->get_environment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID |

### Return type

[**Environment**](Environment.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get environment by ID |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_environment_status**
> EnvironmentStatus get_environment_status(environment_id)

Get environment status

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import environment_main_calls_api
from qovery.model.environment_status import EnvironmentStatus
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
    api_instance = environment_main_calls_api.EnvironmentMainCallsApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID

    # example passing only required values which don't have defaults set
    try:
        # Get environment status
        api_response = api_instance.get_environment_status(environment_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling EnvironmentMainCallsApi->get_environment_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID |

### Return type

[**EnvironmentStatus**](EnvironmentStatus.md)

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

# **get_environment_statuses**
> EnvironmentStatuses get_environment_statuses(environment_id)

Get environment statuses with services status

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import environment_main_calls_api
from qovery.model.environment_statuses import EnvironmentStatuses
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
    api_instance = environment_main_calls_api.EnvironmentMainCallsApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID

    # example passing only required values which don't have defaults set
    try:
        # Get environment statuses with services status
        api_response = api_instance.get_environment_statuses(environment_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling EnvironmentMainCallsApi->get_environment_statuses: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID |

### Return type

[**EnvironmentStatuses**](EnvironmentStatuses.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get statuses |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_environment_statuses_with_stages**
> EnvironmentStatusesWithStages get_environment_statuses_with_stages(environment_id)

Get environment statuses with stages

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import environment_main_calls_api
from qovery.model.environment_statuses_with_stages import EnvironmentStatusesWithStages
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
    api_instance = environment_main_calls_api.EnvironmentMainCallsApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID

    # example passing only required values which don't have defaults set
    try:
        # Get environment statuses with stages
        api_response = api_instance.get_environment_statuses_with_stages(environment_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling EnvironmentMainCallsApi->get_environment_statuses_with_stages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID |

### Return type

[**EnvironmentStatusesWithStages**](EnvironmentStatusesWithStages.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get statuses with stages |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

