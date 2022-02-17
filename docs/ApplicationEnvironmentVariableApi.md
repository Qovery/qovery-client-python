# qovery.ApplicationEnvironmentVariableApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_application_environment_variable**](ApplicationEnvironmentVariableApi.md#create_application_environment_variable) | **POST** /application/{applicationId}/environmentVariable | Add an environment variable to the application
[**create_application_environment_variable_alias**](ApplicationEnvironmentVariableApi.md#create_application_environment_variable_alias) | **POST** /application/{applicationId}/environmentVariable/{environmentVariableId}/alias | Create an environment variable alias at the application level
[**create_application_environment_variable_override**](ApplicationEnvironmentVariableApi.md#create_application_environment_variable_override) | **POST** /application/{applicationId}/environmentVariable/{environmentVariableId}/override | Create an environment variable override at the application level
[**delete_application_environment_variable**](ApplicationEnvironmentVariableApi.md#delete_application_environment_variable) | **DELETE** /application/{applicationId}/environmentVariable/{environmentVariableId} | Delete an environment variable from an application
[**edit_application_environment_variable**](ApplicationEnvironmentVariableApi.md#edit_application_environment_variable) | **PUT** /application/{applicationId}/environmentVariable/{environmentVariableId} | Edit an environment variable belonging to the application
[**import_environment_variable**](ApplicationEnvironmentVariableApi.md#import_environment_variable) | **POST** /application/{applicationId}/environmentVariable/import | Import variables
[**list_application_environment_variable**](ApplicationEnvironmentVariableApi.md#list_application_environment_variable) | **GET** /application/{applicationId}/environmentVariable | List environment variables


# **create_application_environment_variable**
> EnvironmentVariableResponse create_application_environment_variable(application_id)

Add an environment variable to the application

- Add an environment variable to the application. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import application_environment_variable_api
from qovery.model.environment_variable_response import EnvironmentVariableResponse
from qovery.model.environment_variable_request import EnvironmentVariableRequest
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
    api_instance = application_environment_variable_api.ApplicationEnvironmentVariableApi(api_client)
    application_id = "applicationId_example" # str | Application ID
    environment_variable_request = EnvironmentVariableRequest(
        key="key_example",
        value="value_example",
    ) # EnvironmentVariableRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add an environment variable to the application
        api_response = api_instance.create_application_environment_variable(application_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationEnvironmentVariableApi->create_application_environment_variable: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add an environment variable to the application
        api_response = api_instance.create_application_environment_variable(application_id, environment_variable_request=environment_variable_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationEnvironmentVariableApi->create_application_environment_variable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID |
 **environment_variable_request** | [**EnvironmentVariableRequest**](EnvironmentVariableRequest.md)|  | [optional]

### Return type

[**EnvironmentVariableResponse**](EnvironmentVariableResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Added an environment variable |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_application_environment_variable_alias**
> EnvironmentVariableResponse create_application_environment_variable_alias(application_id, environment_variable_id)

Create an environment variable alias at the application level

- Allows you to add an alias at application level on an existing environment variable having higher scope, in order to customize its key. - You only have to specify a key in the request body - The system will create a new environment variable at application level with the same value as the one corresponding to the variable id in the path - The response body will contain the newly created variable - Information regarding the aliased_variable will be exposed in the \"aliased_variable\" field of the newly created variable - Only 1 alias level is allowed. You can't create an alias on an alias 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import application_environment_variable_api
from qovery.model.environment_variable_response import EnvironmentVariableResponse
from qovery.model.key import Key
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
    api_instance = application_environment_variable_api.ApplicationEnvironmentVariableApi(api_client)
    application_id = "applicationId_example" # str | Application ID
    environment_variable_id = "environmentVariableId_example" # str | Environment Variable ID
    key = Key(
        key="key_example",
    ) # Key |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create an environment variable alias at the application level
        api_response = api_instance.create_application_environment_variable_alias(application_id, environment_variable_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationEnvironmentVariableApi->create_application_environment_variable_alias: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an environment variable alias at the application level
        api_response = api_instance.create_application_environment_variable_alias(application_id, environment_variable_id, key=key)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationEnvironmentVariableApi->create_application_environment_variable_alias: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID |
 **environment_variable_id** | **str**| Environment Variable ID |
 **key** | [**Key**](Key.md)|  | [optional]

### Return type

[**EnvironmentVariableResponse**](EnvironmentVariableResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create variable alias |  -  |
**400** | Can&#39;t create an alias on a higher scope. Aliases can only be created from one scope to a lower scope. Scope hierarchy is BUILT_IN &gt; PROJECT &gt; ENVIRONMENT &gt; APPLICATION |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_application_environment_variable_override**
> EnvironmentVariableResponse create_application_environment_variable_override(application_id, environment_variable_id)

Create an environment variable override at the application level

- Allows you to override at application level an environment variable that has a higher scope. - You only have to specify a value in the request body - The system will create a new environment variable at application level with the same key as the one corresponding to the variable id in the path - The response body will contain the newly created variable - Information regarding the overridden_variable will be exposed in the \"overridden_variable\" field of the newly created variable 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import application_environment_variable_api
from qovery.model.environment_variable_response import EnvironmentVariableResponse
from qovery.model.value import Value
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
    api_instance = application_environment_variable_api.ApplicationEnvironmentVariableApi(api_client)
    application_id = "applicationId_example" # str | Application ID
    environment_variable_id = "environmentVariableId_example" # str | Environment Variable ID
    value = Value(
        value="value_example",
    ) # Value |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create an environment variable override at the application level
        api_response = api_instance.create_application_environment_variable_override(application_id, environment_variable_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationEnvironmentVariableApi->create_application_environment_variable_override: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an environment variable override at the application level
        api_response = api_instance.create_application_environment_variable_override(application_id, environment_variable_id, value=value)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationEnvironmentVariableApi->create_application_environment_variable_override: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID |
 **environment_variable_id** | **str**| Environment Variable ID |
 **value** | [**Value**](Value.md)|  | [optional]

### Return type

[**EnvironmentVariableResponse**](EnvironmentVariableResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create variable override |  -  |
**400** | Can&#39;t create an override on a higher scope. Overrides can only be created from one scope to a lower scope. Scope hierarchy is BUILT_IN &gt; PROJECT &gt; ENVIRONMENT &gt; APPLICATION |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_application_environment_variable**
> delete_application_environment_variable(application_id, environment_variable_id)

Delete an environment variable from an application

- To delete an environment variable from an application you must have the project user permission - You can't delete a BUILT_IN variable - If you delete a variable having override or alias, the associated override/alias will be deleted as well 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import application_environment_variable_api
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
    api_instance = application_environment_variable_api.ApplicationEnvironmentVariableApi(api_client)
    application_id = "applicationId_example" # str | Application ID
    environment_variable_id = "environmentVariableId_example" # str | Environment Variable ID

    # example passing only required values which don't have defaults set
    try:
        # Delete an environment variable from an application
        api_instance.delete_application_environment_variable(application_id, environment_variable_id)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationEnvironmentVariableApi->delete_application_environment_variable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID |
 **environment_variable_id** | **str**| Environment Variable ID |

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

# **edit_application_environment_variable**
> EnvironmentVariableResponse edit_application_environment_variable(application_id, environment_variable_id, environment_variable_edit_request)

Edit an environment variable belonging to the application

- You can't edit a BUILT_IN variable - For an override, you can't edit the key - For an alias, you can't edit the value - An override can only have a scope lower to the variable it is overriding (hierarchy is BUILT_IN > PROJECT > ENVIRONMENT > APPLICATION) 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import application_environment_variable_api
from qovery.model.environment_variable_response import EnvironmentVariableResponse
from qovery.model.environment_variable_edit_request import EnvironmentVariableEditRequest
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
    api_instance = application_environment_variable_api.ApplicationEnvironmentVariableApi(api_client)
    application_id = "applicationId_example" # str | Application ID
    environment_variable_id = "environmentVariableId_example" # str | Environment Variable ID
    environment_variable_edit_request = EnvironmentVariableEditRequest(
        key="key_example",
        value="value_example",
    ) # EnvironmentVariableEditRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Edit an environment variable belonging to the application
        api_response = api_instance.edit_application_environment_variable(application_id, environment_variable_id, environment_variable_edit_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationEnvironmentVariableApi->edit_application_environment_variable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID |
 **environment_variable_id** | **str**| Environment Variable ID |
 **environment_variable_edit_request** | [**EnvironmentVariableEditRequest**](EnvironmentVariableEditRequest.md)|  |

### Return type

[**EnvironmentVariableResponse**](EnvironmentVariableResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Edited the environment variable value |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_environment_variable**
> VariableImportResponse import_environment_variable(application_id)

Import variables

Import environment variables in a defined scope, with a defined visibility.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import application_environment_variable_api
from qovery.model.variable_import_response import VariableImportResponse
from qovery.model.variable_import_request import VariableImportRequest
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
    api_instance = application_environment_variable_api.ApplicationEnvironmentVariableApi(api_client)
    application_id = "applicationId_example" # str | Application ID
    variable_import_request = VariableImportRequest(
        overwrite=False,
        vars=[
            VariableImportRequestVars(
                name="name_example",
                value="value_example",
                scope="ORGANIZATION",
                is_secret=True,
            ),
        ],
    ) # VariableImportRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Import variables
        api_response = api_instance.import_environment_variable(application_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationEnvironmentVariableApi->import_environment_variable: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Import variables
        api_response = api_instance.import_environment_variable(application_id, variable_import_request=variable_import_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationEnvironmentVariableApi->import_environment_variable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID |
 **variable_import_request** | [**VariableImportRequest**](VariableImportRequest.md)|  | [optional]

### Return type

[**VariableImportResponse**](VariableImportResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Import environment variables |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_application_environment_variable**
> EnvironmentVariableResponseList list_application_environment_variable(application_id)

List environment variables

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import application_environment_variable_api
from qovery.model.environment_variable_response_list import EnvironmentVariableResponseList
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
    api_instance = application_environment_variable_api.ApplicationEnvironmentVariableApi(api_client)
    application_id = "applicationId_example" # str | Application ID

    # example passing only required values which don't have defaults set
    try:
        # List environment variables
        api_response = api_instance.list_application_environment_variable(application_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationEnvironmentVariableApi->list_application_environment_variable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID |

### Return type

[**EnvironmentVariableResponseList**](EnvironmentVariableResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List environment variables |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

