# qovery.ApplicationsApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_application**](ApplicationsApi.md#create_application) | **POST** /environment/{environmentId}/application | Create an application
[**deploy_all_applications**](ApplicationsApi.md#deploy_all_applications) | **POST** /environment/{environmentId}/application/deploy | Deploy applications
[**get_environment_application_current_instance**](ApplicationsApi.md#get_environment_application_current_instance) | **GET** /environment/{environmentId}/application/instance | List running instances with CPU and RAM usage for each application
[**get_environment_application_current_scale**](ApplicationsApi.md#get_environment_application_current_scale) | **GET** /environment/{environmentId}/application/currentScale | List current scaling information for each application
[**get_environment_application_current_storage**](ApplicationsApi.md#get_environment_application_current_storage) | **GET** /environment/{environmentId}/application/currentStorage | List current storage disk usage for each application
[**get_environment_application_status**](ApplicationsApi.md#get_environment_application_status) | **GET** /environment/{environmentId}/application/status | List all environment applications statuses
[**get_environment_application_supported_languages**](ApplicationsApi.md#get_environment_application_supported_languages) | **GET** /environment/{environmentId}/application/supportedLanguage | List supported languages
[**list_application**](ApplicationsApi.md#list_application) | **GET** /environment/{environmentId}/application | List applications


# **create_application**
> Application create_application(environment_id)

Create an application

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import applications_api
from qovery.model.application import Application
from qovery.model.application_request import ApplicationRequest
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
    api_instance = applications_api.ApplicationsApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID
    application_request = ApplicationRequest(None) # ApplicationRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create an application
        api_response = api_instance.create_application(environment_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationsApi->create_application: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an application
        api_response = api_instance.create_application(environment_id, application_request=application_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationsApi->create_application: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID |
 **application_request** | [**ApplicationRequest**](ApplicationRequest.md)|  | [optional]

### Return type

[**Application**](Application.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create application |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Application name within the environment is already taken |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deploy_all_applications**
> Status deploy_all_applications(environment_id)

Deploy applications

Deploy to the last commit the applications you specified.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import applications_api
from qovery.model.deploy_all_request import DeployAllRequest
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
    api_instance = applications_api.ApplicationsApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID
    deploy_all_request = DeployAllRequest(
        applications=[
            DeployAllRequestApplications(
                application_id="application_id_example",
                git_commit_id="git_commit_id_example",
            ),
        ],
    ) # DeployAllRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Deploy applications
        api_response = api_instance.deploy_all_applications(environment_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationsApi->deploy_all_applications: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Deploy applications
        api_response = api_instance.deploy_all_applications(environment_id, deploy_all_request=deploy_all_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationsApi->deploy_all_applications: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID |
 **deploy_all_request** | [**DeployAllRequest**](DeployAllRequest.md)|  | [optional]

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
**202** | Deployed applications |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Operation is in progress |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_environment_application_current_instance**
> EnvironmentApplicationsInstanceResponseList get_environment_application_current_instance(environment_id)

List running instances with CPU and RAM usage for each application

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import applications_api
from qovery.model.environment_applications_instance_response_list import EnvironmentApplicationsInstanceResponseList
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
    api_instance = applications_api.ApplicationsApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID

    # example passing only required values which don't have defaults set
    try:
        # List running instances with CPU and RAM usage for each application
        api_response = api_instance.get_environment_application_current_instance(environment_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationsApi->get_environment_application_current_instance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID |

### Return type

[**EnvironmentApplicationsInstanceResponseList**](EnvironmentApplicationsInstanceResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Know current resource consumption for each application of the environment |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_environment_application_current_scale**
> EnvironmentApplicationsCurrentScaleResponseList get_environment_application_current_scale(environment_id)

List current scaling information for each application

Returns min, max, and running number of instances for each application

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import applications_api
from qovery.model.environment_applications_current_scale_response_list import EnvironmentApplicationsCurrentScaleResponseList
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
    api_instance = applications_api.ApplicationsApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID

    # example passing only required values which don't have defaults set
    try:
        # List current scaling information for each application
        api_response = api_instance.get_environment_application_current_scale(environment_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationsApi->get_environment_application_current_scale: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID |

### Return type

[**EnvironmentApplicationsCurrentScaleResponseList**](EnvironmentApplicationsCurrentScaleResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list applications with current scaling |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_environment_application_current_storage**
> EnvironmentApplicationsStorageResponseList get_environment_application_current_storage(environment_id)

List current storage disk usage for each application

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import applications_api
from qovery.model.environment_applications_storage_response_list import EnvironmentApplicationsStorageResponseList
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
    api_instance = applications_api.ApplicationsApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID

    # example passing only required values which don't have defaults set
    try:
        # List current storage disk usage for each application
        api_response = api_instance.get_environment_application_current_storage(environment_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationsApi->get_environment_application_current_storage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID |

### Return type

[**EnvironmentApplicationsStorageResponseList**](EnvironmentApplicationsStorageResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current storage disk usage |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_environment_application_status**
> ReferenceObjectStatusResponseList get_environment_application_status(environment_id)

List all environment applications statuses

Returns a list of applications with only their id and status.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import applications_api
from qovery.model.reference_object_status_response_list import ReferenceObjectStatusResponseList
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
    api_instance = applications_api.ApplicationsApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID

    # example passing only required values which don't have defaults set
    try:
        # List all environment applications statuses
        api_response = api_instance.get_environment_application_status(environment_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationsApi->get_environment_application_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID |

### Return type

[**ReferenceObjectStatusResponseList**](ReferenceObjectStatusResponseList.md)

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

# **get_environment_application_supported_languages**
> EnvironmentApplicationsSupportedLanguageList get_environment_application_supported_languages(environment_id)

List supported languages

Returns list of languages supported by Buildpacks.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import applications_api
from qovery.model.environment_applications_supported_language_list import EnvironmentApplicationsSupportedLanguageList
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
    api_instance = applications_api.ApplicationsApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID

    # example passing only required values which don't have defaults set
    try:
        # List supported languages
        api_response = api_instance.get_environment_application_supported_languages(environment_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationsApi->get_environment_application_supported_languages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID |

### Return type

[**EnvironmentApplicationsSupportedLanguageList**](EnvironmentApplicationsSupportedLanguageList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Supported languages list. |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_application**
> ApplicationResponseList list_application(environment_id)

List applications

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import applications_api
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
    api_instance = applications_api.ApplicationsApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID

    # example passing only required values which don't have defaults set
    try:
        # List applications
        api_response = api_instance.list_application(environment_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationsApi->list_application: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID |

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
**200** | List applications |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

