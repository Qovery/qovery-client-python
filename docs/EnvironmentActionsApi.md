# qovery.EnvironmentActionsApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_environment_deployment**](EnvironmentActionsApi.md#cancel_environment_deployment) | **POST** /environment/{environmentId}/cancelDeployment | Cancel environment deployment
[**clone_environment**](EnvironmentActionsApi.md#clone_environment) | **POST** /environment/{environmentId}/clone | Clone environment
[**deploy_environment**](EnvironmentActionsApi.md#deploy_environment) | **POST** /environment/{environmentId}/deploy | Deploy environment
[**restart_environment**](EnvironmentActionsApi.md#restart_environment) | **POST** /environment/{environmentId}/restart | Restart environment
[**stop_environment**](EnvironmentActionsApi.md#stop_environment) | **POST** /environment/{environmentId}/stop | Stop environment


# **cancel_environment_deployment**
> Status cancel_environment_deployment(environment_id)

Cancel environment deployment

Cancel the current deployment of your environment.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import environment_actions_api
from qovery.model.status import Status
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
    api_instance = environment_actions_api.EnvironmentActionsApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID

    # example passing only required values which don't have defaults set
    try:
        # Cancel environment deployment
        api_response = api_instance.cancel_environment_deployment(environment_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling EnvironmentActionsApi->cancel_environment_deployment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID |

### Return type

[**Status**](Status.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | environment deployment cancelling has been requested |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Environment deployment is already cancelled or an operation is in progress |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clone_environment**
> EnvironmentResponse clone_environment(environment_id)

Clone environment

You must provide a name. This will create a new environment, with the same configuration, and same applications and databases. Database data is not cloned.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import environment_actions_api
from qovery.model.clone_request import CloneRequest
from qovery.model.environment_response import EnvironmentResponse
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
    api_instance = environment_actions_api.EnvironmentActionsApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID
    clone_request = CloneRequest(
        name="name_example",
        cluster_id="cluster_id_example",
        mode=EnvironmentModeEnum("PRODUCTION"),
    ) # CloneRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Clone environment
        api_response = api_instance.clone_environment(environment_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling EnvironmentActionsApi->clone_environment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Clone environment
        api_response = api_instance.clone_environment(environment_id, clone_request=clone_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling EnvironmentActionsApi->clone_environment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID |
 **clone_request** | [**CloneRequest**](CloneRequest.md)|  | [optional]

### Return type

[**EnvironmentResponse**](EnvironmentResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Environment clone has been requested |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Operation is in progress |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deploy_environment**
> Status deploy_environment(environment_id)

Deploy environment

This will deploy all the services of this environment to their latest version.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import environment_actions_api
from qovery.model.status import Status
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
    api_instance = environment_actions_api.EnvironmentActionsApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID

    # example passing only required values which don't have defaults set
    try:
        # Deploy environment
        api_response = api_instance.deploy_environment(environment_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling EnvironmentActionsApi->deploy_environment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID |

### Return type

[**Status**](Status.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Deploy environment |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Operation is in progress |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restart_environment**
> Status restart_environment(environment_id)

Restart environment

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import environment_actions_api
from qovery.model.environment_restart_request import EnvironmentRestartRequest
from qovery.model.status import Status
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
    api_instance = environment_actions_api.EnvironmentActionsApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID
    environment_restart_request = EnvironmentRestartRequest(
        restart_db=False,
    ) # EnvironmentRestartRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Restart environment
        api_response = api_instance.restart_environment(environment_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling EnvironmentActionsApi->restart_environment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Restart environment
        api_response = api_instance.restart_environment(environment_id, environment_restart_request=environment_restart_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling EnvironmentActionsApi->restart_environment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID |
 **environment_restart_request** | [**EnvironmentRestartRequest**](EnvironmentRestartRequest.md)|  | [optional]

### Return type

[**Status**](Status.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Environment restart has been requested |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Operation is in progress |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_environment**
> Status stop_environment(environment_id)

Stop environment

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import environment_actions_api
from qovery.model.status import Status
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
    api_instance = environment_actions_api.EnvironmentActionsApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID

    # example passing only required values which don't have defaults set
    try:
        # Stop environment
        api_response = api_instance.stop_environment(environment_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling EnvironmentActionsApi->stop_environment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID |

### Return type

[**Status**](Status.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Environment stop has been requested |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Environment is already stopped or an operation is in progress |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

