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
> EnvironmentVariable create_application_environment_variable(application_id, environment_variable_request=environment_variable_request)

Add an environment variable to the application

- Add an environment variable to the application. 

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import qovery
from qovery.models.environment_variable import EnvironmentVariable
from qovery.models.environment_variable_request import EnvironmentVariableRequest
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
    api_instance = qovery.ApplicationEnvironmentVariableApi(api_client)
    application_id = 'application_id_example' # str | Application ID
    environment_variable_request = qovery.EnvironmentVariableRequest() # EnvironmentVariableRequest |  (optional)

    try:
        # Add an environment variable to the application
        api_response = api_instance.create_application_environment_variable(application_id, environment_variable_request=environment_variable_request)
        print("The response of ApplicationEnvironmentVariableApi->create_application_environment_variable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationEnvironmentVariableApi->create_application_environment_variable: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID | 
 **environment_variable_request** | [**EnvironmentVariableRequest**](EnvironmentVariableRequest.md)|  | [optional] 

### Return type

[**EnvironmentVariable**](EnvironmentVariable.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

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
> EnvironmentVariable create_application_environment_variable_alias(application_id, environment_variable_id, key=key)

Create an environment variable alias at the application level

- Allows you to add an alias at application level on an existing environment variable having higher scope, in order to customize its key. - You only have to specify a key in the request body - The system will create a new environment variable at application level with the same value as the one corresponding to the variable id in the path - The response body will contain the newly created variable - Information regarding the aliased_variable will be exposed in the \"aliased_variable\" field of the newly created variable - You can't create an alias on an alias 

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import qovery
from qovery.models.environment_variable import EnvironmentVariable
from qovery.models.key import Key
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
    api_instance = qovery.ApplicationEnvironmentVariableApi(api_client)
    application_id = 'application_id_example' # str | Application ID
    environment_variable_id = 'environment_variable_id_example' # str | Environment Variable ID
    key = qovery.Key() # Key |  (optional)

    try:
        # Create an environment variable alias at the application level
        api_response = api_instance.create_application_environment_variable_alias(application_id, environment_variable_id, key=key)
        print("The response of ApplicationEnvironmentVariableApi->create_application_environment_variable_alias:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationEnvironmentVariableApi->create_application_environment_variable_alias: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID | 
 **environment_variable_id** | **str**| Environment Variable ID | 
 **key** | [**Key**](Key.md)|  | [optional] 

### Return type

[**EnvironmentVariable**](EnvironmentVariable.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

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
> EnvironmentVariable create_application_environment_variable_override(application_id, environment_variable_id, value=value)

Create an environment variable override at the application level

- Allows you to override at application level an environment variable that has a higher scope. - You only have to specify a value in the request body - The system will create a new environment variable at application level with the same key as the one corresponding to the variable id in the path - The response body will contain the newly created variable - Information regarding the overridden_variable will be exposed in the \"overridden_variable\" field of the newly created variable 

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import qovery
from qovery.models.environment_variable import EnvironmentVariable
from qovery.models.value import Value
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
    api_instance = qovery.ApplicationEnvironmentVariableApi(api_client)
    application_id = 'application_id_example' # str | Application ID
    environment_variable_id = 'environment_variable_id_example' # str | Environment Variable ID
    value = qovery.Value() # Value |  (optional)

    try:
        # Create an environment variable override at the application level
        api_response = api_instance.create_application_environment_variable_override(application_id, environment_variable_id, value=value)
        print("The response of ApplicationEnvironmentVariableApi->create_application_environment_variable_override:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationEnvironmentVariableApi->create_application_environment_variable_override: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID | 
 **environment_variable_id** | **str**| Environment Variable ID | 
 **value** | [**Value**](Value.md)|  | [optional] 

### Return type

[**EnvironmentVariable**](EnvironmentVariable.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

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

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import qovery
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
    api_instance = qovery.ApplicationEnvironmentVariableApi(api_client)
    application_id = 'application_id_example' # str | Application ID
    environment_variable_id = 'environment_variable_id_example' # str | Environment Variable ID

    try:
        # Delete an environment variable from an application
        api_instance.delete_application_environment_variable(application_id, environment_variable_id)
    except Exception as e:
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

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

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
> EnvironmentVariable edit_application_environment_variable(application_id, environment_variable_id, environment_variable_edit_request)

Edit an environment variable belonging to the application

- You can't edit a BUILT_IN variable - For an override, you can't edit the key - For an alias, you can't edit the value - An override can only have a scope lower to the variable it is overriding (hierarchy is BUILT_IN > PROJECT > ENVIRONMENT > APPLICATION) 

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import qovery
from qovery.models.environment_variable import EnvironmentVariable
from qovery.models.environment_variable_edit_request import EnvironmentVariableEditRequest
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
    api_instance = qovery.ApplicationEnvironmentVariableApi(api_client)
    application_id = 'application_id_example' # str | Application ID
    environment_variable_id = 'environment_variable_id_example' # str | Environment Variable ID
    environment_variable_edit_request = qovery.EnvironmentVariableEditRequest() # EnvironmentVariableEditRequest | 

    try:
        # Edit an environment variable belonging to the application
        api_response = api_instance.edit_application_environment_variable(application_id, environment_variable_id, environment_variable_edit_request)
        print("The response of ApplicationEnvironmentVariableApi->edit_application_environment_variable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationEnvironmentVariableApi->edit_application_environment_variable: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID | 
 **environment_variable_id** | **str**| Environment Variable ID | 
 **environment_variable_edit_request** | [**EnvironmentVariableEditRequest**](EnvironmentVariableEditRequest.md)|  | 

### Return type

[**EnvironmentVariable**](EnvironmentVariable.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

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
> VariableImport import_environment_variable(application_id, variable_import_request=variable_import_request)

Import variables

Import environment variables in a defined scope, with a defined visibility.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import qovery
from qovery.models.variable_import import VariableImport
from qovery.models.variable_import_request import VariableImportRequest
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
    api_instance = qovery.ApplicationEnvironmentVariableApi(api_client)
    application_id = 'application_id_example' # str | Application ID
    variable_import_request = qovery.VariableImportRequest() # VariableImportRequest |  (optional)

    try:
        # Import variables
        api_response = api_instance.import_environment_variable(application_id, variable_import_request=variable_import_request)
        print("The response of ApplicationEnvironmentVariableApi->import_environment_variable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationEnvironmentVariableApi->import_environment_variable: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID | 
 **variable_import_request** | [**VariableImportRequest**](VariableImportRequest.md)|  | [optional] 

### Return type

[**VariableImport**](VariableImport.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

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

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import qovery
from qovery.models.environment_variable_response_list import EnvironmentVariableResponseList
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
    api_instance = qovery.ApplicationEnvironmentVariableApi(api_client)
    application_id = 'application_id_example' # str | Application ID

    try:
        # List environment variables
        api_response = api_instance.list_application_environment_variable(application_id)
        print("The response of ApplicationEnvironmentVariableApi->list_application_environment_variable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationEnvironmentVariableApi->list_application_environment_variable: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID | 

### Return type

[**EnvironmentVariableResponseList**](EnvironmentVariableResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

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

