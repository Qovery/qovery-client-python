# qovery.ContainerEnvironmentVariableApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_container_environment_variable**](ContainerEnvironmentVariableApi.md#create_container_environment_variable) | **POST** /container/{containerId}/environmentVariable | Add an environment variable to the container
[**create_container_environment_variable_alias**](ContainerEnvironmentVariableApi.md#create_container_environment_variable_alias) | **POST** /container/{containerId}/environmentVariable/{environmentVariableId}/alias | Create an environment variable alias at the container level
[**create_container_environment_variable_override**](ContainerEnvironmentVariableApi.md#create_container_environment_variable_override) | **POST** /container/{containerId}/environmentVariable/{environmentVariableId}/override | Create an environment variable override at the container level
[**delete_container_environment_variable**](ContainerEnvironmentVariableApi.md#delete_container_environment_variable) | **DELETE** /container/{containerId}/environmentVariable/{environmentVariableId} | Delete an environment variable from a container
[**edit_container_environment_variable**](ContainerEnvironmentVariableApi.md#edit_container_environment_variable) | **PUT** /container/{containerId}/environmentVariable/{environmentVariableId} | Edit an environment variable belonging to the container
[**import_container_environment_variable**](ContainerEnvironmentVariableApi.md#import_container_environment_variable) | **POST** /container/{containerId}/environmentVariable/import | Import variables
[**list_container_environment_variable**](ContainerEnvironmentVariableApi.md#list_container_environment_variable) | **GET** /container/{containerId}/environmentVariable | List environment variables


# **create_container_environment_variable**
> EnvironmentVariable create_container_environment_variable(container_id)

Add an environment variable to the container

- Add an environment variable to the container. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import container_environment_variable_api
from qovery.model.environment_variable import EnvironmentVariable
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
    api_instance = container_environment_variable_api.ContainerEnvironmentVariableApi(api_client)
    container_id = "containerId_example" # str | Container ID
    environment_variable_request = EnvironmentVariableRequest(
        key="key_example",
        value="value_example",
    ) # EnvironmentVariableRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add an environment variable to the container
        api_response = api_instance.create_container_environment_variable(container_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainerEnvironmentVariableApi->create_container_environment_variable: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add an environment variable to the container
        api_response = api_instance.create_container_environment_variable(container_id, environment_variable_request=environment_variable_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainerEnvironmentVariableApi->create_container_environment_variable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Container ID |
 **environment_variable_request** | [**EnvironmentVariableRequest**](EnvironmentVariableRequest.md)|  | [optional]

### Return type

[**EnvironmentVariable**](EnvironmentVariable.md)

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

# **create_container_environment_variable_alias**
> EnvironmentVariable create_container_environment_variable_alias(container_id, environment_variable_id)

Create an environment variable alias at the container level

- Allows you to add an alias at container level on an existing environment variable having higher scope, in order to customize its key. - You only have to specify a key in the request body - The system will create a new environment variable at container level with the same value as the one corresponding to the variable id in the path - The response body will contain the newly created variable - Information regarding the aliased_variable will be exposed in the \"aliased_variable\" field of the newly created variable - Only 1 alias level is allowed. You can't create an alias on an alias 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import container_environment_variable_api
from qovery.model.key import Key
from qovery.model.environment_variable import EnvironmentVariable
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
    api_instance = container_environment_variable_api.ContainerEnvironmentVariableApi(api_client)
    container_id = "containerId_example" # str | Container ID
    environment_variable_id = "environmentVariableId_example" # str | Environment Variable ID
    key = Key(
        key="key_example",
    ) # Key |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create an environment variable alias at the container level
        api_response = api_instance.create_container_environment_variable_alias(container_id, environment_variable_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainerEnvironmentVariableApi->create_container_environment_variable_alias: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an environment variable alias at the container level
        api_response = api_instance.create_container_environment_variable_alias(container_id, environment_variable_id, key=key)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainerEnvironmentVariableApi->create_container_environment_variable_alias: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Container ID |
 **environment_variable_id** | **str**| Environment Variable ID |
 **key** | [**Key**](Key.md)|  | [optional]

### Return type

[**EnvironmentVariable**](EnvironmentVariable.md)

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

# **create_container_environment_variable_override**
> EnvironmentVariable create_container_environment_variable_override(container_id, environment_variable_id)

Create an environment variable override at the container level

- Allows you to override at container level an environment variable that has a higher scope. - You only have to specify a value in the request body - The system will create a new environment variable at container level with the same key as the one corresponding to the variable id in the path - The response body will contain the newly created variable - Information regarding the overridden_variable will be exposed in the \"overridden_variable\" field of the newly created variable 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import container_environment_variable_api
from qovery.model.environment_variable import EnvironmentVariable
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
    api_instance = container_environment_variable_api.ContainerEnvironmentVariableApi(api_client)
    container_id = "containerId_example" # str | Container ID
    environment_variable_id = "environmentVariableId_example" # str | Environment Variable ID
    value = Value(
        value="value_example",
    ) # Value |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create an environment variable override at the container level
        api_response = api_instance.create_container_environment_variable_override(container_id, environment_variable_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainerEnvironmentVariableApi->create_container_environment_variable_override: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an environment variable override at the container level
        api_response = api_instance.create_container_environment_variable_override(container_id, environment_variable_id, value=value)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainerEnvironmentVariableApi->create_container_environment_variable_override: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Container ID |
 **environment_variable_id** | **str**| Environment Variable ID |
 **value** | [**Value**](Value.md)|  | [optional]

### Return type

[**EnvironmentVariable**](EnvironmentVariable.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create variable override |  -  |
**400** | Can&#39;t create an override on a higher scope. Overrides can only be created from one scope to a lower scope. Scope hierarchy is BUILT_IN &gt; PROJECT &gt; ENVIRONMENT &gt; CONTAINER |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_container_environment_variable**
> delete_container_environment_variable(container_id, environment_variable_id)

Delete an environment variable from a container

- To delete an environment variable from an container you must have the project user permission - You can't delete a BUILT_IN variable - If you delete a variable having override or alias, the associated override/alias will be deleted as well 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import container_environment_variable_api
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
    api_instance = container_environment_variable_api.ContainerEnvironmentVariableApi(api_client)
    container_id = "containerId_example" # str | Container ID
    environment_variable_id = "environmentVariableId_example" # str | Environment Variable ID

    # example passing only required values which don't have defaults set
    try:
        # Delete an environment variable from a container
        api_instance.delete_container_environment_variable(container_id, environment_variable_id)
    except qovery.ApiException as e:
        print("Exception when calling ContainerEnvironmentVariableApi->delete_container_environment_variable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Container ID |
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

# **edit_container_environment_variable**
> EnvironmentVariable edit_container_environment_variable(container_id, environment_variable_id, environment_variable_edit_request)

Edit an environment variable belonging to the container

- You can't edit a BUILT_IN variable - For an override, you can't edit the key - For an alias, you can't edit the value - An override can only have a scope lower to the variable it is overriding (hierarchy is BUILT_IN > PROJECT > ENVIRONMENT > CONTAINER) 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import container_environment_variable_api
from qovery.model.environment_variable_edit_request import EnvironmentVariableEditRequest
from qovery.model.environment_variable import EnvironmentVariable
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
    api_instance = container_environment_variable_api.ContainerEnvironmentVariableApi(api_client)
    container_id = "containerId_example" # str | Container ID
    environment_variable_id = "environmentVariableId_example" # str | Environment Variable ID
    environment_variable_edit_request = EnvironmentVariableEditRequest(
        key="key_example",
        value="value_example",
    ) # EnvironmentVariableEditRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Edit an environment variable belonging to the container
        api_response = api_instance.edit_container_environment_variable(container_id, environment_variable_id, environment_variable_edit_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainerEnvironmentVariableApi->edit_container_environment_variable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Container ID |
 **environment_variable_id** | **str**| Environment Variable ID |
 **environment_variable_edit_request** | [**EnvironmentVariableEditRequest**](EnvironmentVariableEditRequest.md)|  |

### Return type

[**EnvironmentVariable**](EnvironmentVariable.md)

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

# **import_container_environment_variable**
> VariableImport import_container_environment_variable(container_id)

Import variables

Import environment variables in a defined scope, with a defined visibility.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import container_environment_variable_api
from qovery.model.variable_import import VariableImport
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
    api_instance = container_environment_variable_api.ContainerEnvironmentVariableApi(api_client)
    container_id = "containerId_example" # str | Container ID
    variable_import_request = VariableImportRequest(
        overwrite=False,
        vars=[
            VariableImportRequestVars(
                name="name_example",
                value="value_example",
                scope=EnvironmentVariableScopeEnum("APPLICATION"),
                is_secret=True,
            ),
        ],
    ) # VariableImportRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Import variables
        api_response = api_instance.import_container_environment_variable(container_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainerEnvironmentVariableApi->import_container_environment_variable: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Import variables
        api_response = api_instance.import_container_environment_variable(container_id, variable_import_request=variable_import_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainerEnvironmentVariableApi->import_container_environment_variable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Container ID |
 **variable_import_request** | [**VariableImportRequest**](VariableImportRequest.md)|  | [optional]

### Return type

[**VariableImport**](VariableImport.md)

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

# **list_container_environment_variable**
> EnvironmentVariableResponseList list_container_environment_variable(container_id)

List environment variables

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import container_environment_variable_api
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
    api_instance = container_environment_variable_api.ContainerEnvironmentVariableApi(api_client)
    container_id = "containerId_example" # str | Container ID

    # example passing only required values which don't have defaults set
    try:
        # List environment variables
        api_response = api_instance.list_container_environment_variable(container_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainerEnvironmentVariableApi->list_container_environment_variable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Container ID |

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

