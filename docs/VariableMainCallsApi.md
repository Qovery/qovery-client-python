# qovery.VariableMainCallsApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_variable**](VariableMainCallsApi.md#create_variable) | **POST** /variable | Create a variable
[**create_variable_alias**](VariableMainCallsApi.md#create_variable_alias) | **POST** /variable/{variableId}/alias | Create a variable alias
[**create_variable_override**](VariableMainCallsApi.md#create_variable_override) | **POST** /variable/{variableId}/override | Create a variable override
[**delete_variable**](VariableMainCallsApi.md#delete_variable) | **DELETE** /variable/{variableId} | Delete a variable
[**edit_variable**](VariableMainCallsApi.md#edit_variable) | **PUT** /variable/{variableId} | Edit a variable
[**import_environment_variables**](VariableMainCallsApi.md#import_environment_variables) | **POST** /variable/import | Import variables
[**list_variables**](VariableMainCallsApi.md#list_variables) | **GET** /variable | List variables


# **create_variable**
> VariableResponse create_variable()

Create a variable

- Create a variable with the scope defined in the request body. 

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import variable_main_calls_api
from qovery.model.variable_response import VariableResponse
from qovery.model.variable_request import VariableRequest
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
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = qovery.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with qovery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = variable_main_calls_api.VariableMainCallsApi(api_client)
    variable_request = VariableRequest(
        key="key_example",
        value="value_example",
        mount_path="mount_path_example",
        is_secret=True,
        variable_scope=APIVariableScopeEnum("APPLICATION"),
        variable_parent_id="variable_parent_id_example",
    ) # VariableRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a variable
        api_response = api_instance.create_variable(variable_request=variable_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling VariableMainCallsApi->create_variable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variable_request** | [**VariableRequest**](VariableRequest.md)|  | [optional]

### Return type

[**VariableResponse**](VariableResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create a variable |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_variable_alias**
> VariableResponse create_variable_alias(variable_id)

Create a variable alias

- Allows you to create an alias of one of the existing variables. - You have to specify an alias (key) in the request body, the scope and the parent id of the alias (project id, environment id or service id) - The system will create a new variable at the requested level with the same value as the one corresponding to the variable id passed as path parameter. - The response body will contain the newly created variable - Information regarding the aliased_variable will be exposed in the \"aliased_variable\" or in the \"aliased_secret\" field of the newly created variable - You can't create an alias on an alias 

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import variable_main_calls_api
from qovery.model.variable_response import VariableResponse
from qovery.model.variable_alias_request import VariableAliasRequest
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
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = qovery.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with qovery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = variable_main_calls_api.VariableMainCallsApi(api_client)
    variable_id = "variableId_example" # str | Variable ID
    variable_alias_request = VariableAliasRequest(
        key="key_example",
        alias_scope=APIVariableScopeEnum("APPLICATION"),
        alias_parent_id="alias_parent_id_example",
    ) # VariableAliasRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a variable alias
        api_response = api_instance.create_variable_alias(variable_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling VariableMainCallsApi->create_variable_alias: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a variable alias
        api_response = api_instance.create_variable_alias(variable_id, variable_alias_request=variable_alias_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling VariableMainCallsApi->create_variable_alias: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variable_id** | **str**| Variable ID |
 **variable_alias_request** | [**VariableAliasRequest**](VariableAliasRequest.md)|  | [optional]

### Return type

[**VariableResponse**](VariableResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create variable alias |  -  |
**400** | Can&#39;t create an alias on a higher scope. Aliases can only be created from one scope to a lower scope. Scope hierarchy is ORGANIZATION &gt; PROJECT &gt; ENVIRONMENT &gt; CONTAINER |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_variable_override**
> VariableResponse create_variable_override(variable_id)

Create a variable override

- Allows you to override a variable that has a higher scope. - You have to specify a value (override) in the request body and the scope and the parent id of the variable to override (project id, environment id or service id) - The system will create a new environment variable at the requested level with the same key as the one corresponding to the variable id passed as path parameter. - The response body will contain the newly created variable - Information regarding the overridden_variable will be exposed in the \"overridden_variable\" or in the \"overridden_secret\" field of the newly created variable 

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import variable_main_calls_api
from qovery.model.variable_override_request import VariableOverrideRequest
from qovery.model.variable_response import VariableResponse
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
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = qovery.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with qovery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = variable_main_calls_api.VariableMainCallsApi(api_client)
    variable_id = "variableId_example" # str | Variable ID
    variable_override_request = VariableOverrideRequest(
        value="value_example",
        override_scope=APIVariableScopeEnum("APPLICATION"),
        override_parent_id="override_parent_id_example",
    ) # VariableOverrideRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a variable override
        api_response = api_instance.create_variable_override(variable_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling VariableMainCallsApi->create_variable_override: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a variable override
        api_response = api_instance.create_variable_override(variable_id, variable_override_request=variable_override_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling VariableMainCallsApi->create_variable_override: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variable_id** | **str**| Variable ID |
 **variable_override_request** | [**VariableOverrideRequest**](VariableOverrideRequest.md)|  | [optional]

### Return type

[**VariableResponse**](VariableResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create variable override |  -  |
**400** | Can&#39;t create an override on a higher scope. Overrides can only be created from one scope to a lower scope. Scope hierarchy is ORGANIZATION &gt; PROJECT &gt; ENVIRONMENT &gt; APPLICATION |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_variable**
> delete_variable(variable_id)

Delete a variable

- To delete a variable - You can't delete a BUILT_IN variable - If you delete a variable having override or alias, the associated override/alias will be deleted as well 

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import variable_main_calls_api
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
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = qovery.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with qovery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = variable_main_calls_api.VariableMainCallsApi(api_client)
    variable_id = "variableId_example" # str | Variable ID

    # example passing only required values which don't have defaults set
    try:
        # Delete a variable
        api_instance.delete_variable(variable_id)
    except qovery.ApiException as e:
        print("Exception when calling VariableMainCallsApi->delete_variable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variable_id** | **str**| Variable ID |

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

# **edit_variable**
> VariableResponse edit_variable(variable_id, variable_edit_request)

Edit a variable

- You can't edit a BUILT_IN variable - For an override, you can't edit the key - For an alias, you can't edit the value 

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import variable_main_calls_api
from qovery.model.variable_edit_request import VariableEditRequest
from qovery.model.variable_response import VariableResponse
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
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = qovery.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with qovery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = variable_main_calls_api.VariableMainCallsApi(api_client)
    variable_id = "variableId_example" # str | Variable ID
    variable_edit_request = VariableEditRequest(
        key="key_example",
        value="value_example",
    ) # VariableEditRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Edit a variable
        api_response = api_instance.edit_variable(variable_id, variable_edit_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling VariableMainCallsApi->edit_variable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variable_id** | **str**| Variable ID |
 **variable_edit_request** | [**VariableEditRequest**](VariableEditRequest.md)|  |

### Return type

[**VariableResponse**](VariableResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Edited variable value |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_environment_variables**
> VariableImport import_environment_variables(service_id, service_type)

Import variables

Import environment variables in a defined scope, with a defined visibility.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import variable_main_calls_api
from qovery.model.service_type_for_variable_enum import ServiceTypeForVariableEnum
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

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = qovery.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with qovery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = variable_main_calls_api.VariableMainCallsApi(api_client)
    service_id = "service_id_example" # str | service id
    service_type = ServiceTypeForVariableEnum("APPLICATION") # ServiceTypeForVariableEnum | service type
    variable_import_request = VariableImportRequest(
        overwrite=False,
        vars=[
            VariableImportRequestVarsInner(
                name="name_example",
                value="value_example",
                scope=APIVariableScopeEnum("APPLICATION"),
                is_secret=True,
            ),
        ],
    ) # VariableImportRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Import variables
        api_response = api_instance.import_environment_variables(service_id, service_type)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling VariableMainCallsApi->import_environment_variables: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Import variables
        api_response = api_instance.import_environment_variables(service_id, service_type, variable_import_request=variable_import_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling VariableMainCallsApi->import_environment_variables: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| service id |
 **service_type** | **ServiceTypeForVariableEnum**| service type |
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

# **list_variables**
> VariableResponseList list_variables(parent_id, scope)

List variables

Returns a list of variables. The result can be filtered by using the query parameters.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import variable_main_calls_api
from qovery.model.api_variable_scope_enum import APIVariableScopeEnum
from qovery.model.variable_response_list import VariableResponseList
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
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = qovery.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with qovery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = variable_main_calls_api.VariableMainCallsApi(api_client)
    parent_id = "parent_id_example" # str | it filters the list by returning only the variables accessible by the selected parent_id. This field shall contain the id of a project, environment or service depending on the selected scope. Example, if scope = APPLICATION and parent_id=<application_id>, the result will contain any variable accessible by the application. The result will contain also any variable declared at an higher scope.
    scope = APIVariableScopeEnum("APPLICATION") # APIVariableScopeEnum | the type of the parent_id (application, project, environment etc..).
    is_secret = True # bool, none_type |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List variables
        api_response = api_instance.list_variables(parent_id, scope)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling VariableMainCallsApi->list_variables: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List variables
        api_response = api_instance.list_variables(parent_id, scope, is_secret=is_secret)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling VariableMainCallsApi->list_variables: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **str**| it filters the list by returning only the variables accessible by the selected parent_id. This field shall contain the id of a project, environment or service depending on the selected scope. Example, if scope &#x3D; APPLICATION and parent_id&#x3D;&lt;application_id&gt;, the result will contain any variable accessible by the application. The result will contain also any variable declared at an higher scope. |
 **scope** | **APIVariableScopeEnum**| the type of the parent_id (application, project, environment etc..). |
 **is_secret** | **bool, none_type**|  | [optional]

### Return type

[**VariableResponseList**](VariableResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List variables |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

