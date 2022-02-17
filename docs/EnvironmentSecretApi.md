# qovery.EnvironmentSecretApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_environment_secret**](EnvironmentSecretApi.md#create_environment_secret) | **POST** /environment/{environmentId}/secret | Add a secret to the environment
[**create_environment_secret_alias**](EnvironmentSecretApi.md#create_environment_secret_alias) | **POST** /environment/{environmentId}/secret/{secretId}/alias | Create a secret alias at the environment level
[**create_environment_secret_override**](EnvironmentSecretApi.md#create_environment_secret_override) | **POST** /environment/{environmentId}/secret/{secretId}/override | Create a secret override at the environment level
[**delete_environment_secret**](EnvironmentSecretApi.md#delete_environment_secret) | **DELETE** /environment/{environmentId}/secret/{secretId} | Delete a secret from the environment
[**edit_environment_secret**](EnvironmentSecretApi.md#edit_environment_secret) | **PUT** /environment/{environmentId}/secret/{secretId} | Edit a secret belonging to the environment
[**list_environment_secrets**](EnvironmentSecretApi.md#list_environment_secrets) | **GET** /environment/{environmentId}/secret | List environment secrets


# **create_environment_secret**
> SecretResponse create_environment_secret(environment_id)

Add a secret to the environment

- Add a secret to the environment.   - If the secret key already exists, then it will be replaced by the new one.   - If the secret value points toward an existing secret key, it will be considered as an alias. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import environment_secret_api
from qovery.model.secret_response import SecretResponse
from qovery.model.secret_request import SecretRequest
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
    api_instance = environment_secret_api.EnvironmentSecretApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID
    secret_request = SecretRequest(
        key="key_example",
        value="value_example",
    ) # SecretRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add a secret to the environment
        api_response = api_instance.create_environment_secret(environment_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling EnvironmentSecretApi->create_environment_secret: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add a secret to the environment
        api_response = api_instance.create_environment_secret(environment_id, secret_request=secret_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling EnvironmentSecretApi->create_environment_secret: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID |
 **secret_request** | [**SecretRequest**](SecretRequest.md)|  | [optional]

### Return type

[**SecretResponse**](SecretResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Added a secret |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_environment_secret_alias**
> SecretResponse create_environment_secret_alias(environment_id, secret_id)

Create a secret alias at the environment level

- Allows you to add an alias at environment level on an existing secret having higher scope, in order to customize its key. - You only have to specify a key in the request body - The system will create a new secret at environment level with the same value as the one corresponding to the secret id in the path - The response body will contain the newly created secret - Information regarding the aliased_secret will be exposed in the \"aliased_secret\" field of the newly created secret - Only 1 alias level is allowed. You can't create an alias on an alias 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import environment_secret_api
from qovery.model.secret_response import SecretResponse
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
    api_instance = environment_secret_api.EnvironmentSecretApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID
    secret_id = "secretId_example" # str | Secret ID
    key = Key(
        key="key_example",
    ) # Key |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a secret alias at the environment level
        api_response = api_instance.create_environment_secret_alias(environment_id, secret_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling EnvironmentSecretApi->create_environment_secret_alias: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a secret alias at the environment level
        api_response = api_instance.create_environment_secret_alias(environment_id, secret_id, key=key)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling EnvironmentSecretApi->create_environment_secret_alias: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID |
 **secret_id** | **str**| Secret ID |
 **key** | [**Key**](Key.md)|  | [optional]

### Return type

[**SecretResponse**](SecretResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create secret alias |  -  |
**400** | Can&#39;t create an alias on a higher scope. Aliases can only be created from one scope to a lower scope. Scope hierarchy is BUILT_IN &gt; PROJECT &gt; ENVIRONMENT &gt; APPLICATION |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_environment_secret_override**
> SecretResponse create_environment_secret_override(environment_id, secret_id)

Create a secret override at the environment level

- Allows you to override at environment level a secret that has a higher scope. - You only have to specify a value in the request body - The system will create a new secret at environment level with the same key as the one corresponding to the secret id in the path - The response body will contain the newly created secret - Information regarding the overridden_secret will be exposed in the \"overridden_secret\" field of the newly created secret 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import environment_secret_api
from qovery.model.secret_response import SecretResponse
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
    api_instance = environment_secret_api.EnvironmentSecretApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID
    secret_id = "secretId_example" # str | Secret ID
    value = Value(
        value="value_example",
    ) # Value |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a secret override at the environment level
        api_response = api_instance.create_environment_secret_override(environment_id, secret_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling EnvironmentSecretApi->create_environment_secret_override: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a secret override at the environment level
        api_response = api_instance.create_environment_secret_override(environment_id, secret_id, value=value)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling EnvironmentSecretApi->create_environment_secret_override: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID |
 **secret_id** | **str**| Secret ID |
 **value** | [**Value**](Value.md)|  | [optional]

### Return type

[**SecretResponse**](SecretResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create secret override |  -  |
**400** | Can&#39;t create an override on a higher scope. Overrides can only be created from one scope to a lower scope. Scope hierarchy is BUILT_IN &gt; PROJECT &gt; ENVIRONMENT &gt; APPLICATION |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_environment_secret**
> delete_environment_secret(environment_id, secret_id)

Delete a secret from the environment

- To delete a secret you must have the project user permission - You can't delete a BUILT_IN secret - If you delete a secret having override or alias, the associated override/alias will be deleted as well  operationId: deleteEnvironmentSecret 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import environment_secret_api
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
    api_instance = environment_secret_api.EnvironmentSecretApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID
    secret_id = "secretId_example" # str | Secret ID

    # example passing only required values which don't have defaults set
    try:
        # Delete a secret from the environment
        api_instance.delete_environment_secret(environment_id, secret_id)
    except qovery.ApiException as e:
        print("Exception when calling EnvironmentSecretApi->delete_environment_secret: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID |
 **secret_id** | **str**| Secret ID |

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

# **edit_environment_secret**
> SecretResponse edit_environment_secret(environment_id, secret_id, secret_edit_request)

Edit a secret belonging to the environment

- You can't edit a BUILT_IN secret - For an override, you can't edit the key - For an alias, you can't edit the value - An override can only have a scope lower to the secret it is overriding (hierarchy is BUILT_IN > PROJECT > ENVIRONMENT > APPLICATION) 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import environment_secret_api
from qovery.model.secret_edit_request import SecretEditRequest
from qovery.model.secret_response import SecretResponse
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
    api_instance = environment_secret_api.EnvironmentSecretApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID
    secret_id = "secretId_example" # str | Secret ID
    secret_edit_request = SecretEditRequest(
        value="value_example",
        key="key_example",
    ) # SecretEditRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Edit a secret belonging to the environment
        api_response = api_instance.edit_environment_secret(environment_id, secret_id, secret_edit_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling EnvironmentSecretApi->edit_environment_secret: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID |
 **secret_id** | **str**| Secret ID |
 **secret_edit_request** | [**SecretEditRequest**](SecretEditRequest.md)|  |

### Return type

[**SecretResponse**](SecretResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Edited the secret value |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_environment_secrets**
> SecretResponseList list_environment_secrets(environment_id)

List environment secrets

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import environment_secret_api
from qovery.model.secret_response_list import SecretResponseList
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
    api_instance = environment_secret_api.EnvironmentSecretApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID

    # example passing only required values which don't have defaults set
    try:
        # List environment secrets
        api_response = api_instance.list_environment_secrets(environment_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling EnvironmentSecretApi->list_environment_secrets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID |

### Return type

[**SecretResponseList**](SecretResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List environment secrets |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

