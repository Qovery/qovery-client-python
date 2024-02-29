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
> Secret create_environment_secret(environment_id, secret_request=secret_request)

Add a secret to the environment

- Add a secret to the environment.   - If the secret key already exists, then it will be replaced by the new one.   - If the secret value points toward an existing secret key, it will be considered as an alias. 

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import qovery
from qovery.models.secret import Secret
from qovery.models.secret_request import SecretRequest
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
    api_instance = qovery.EnvironmentSecretApi(api_client)
    environment_id = 'environment_id_example' # str | Environment ID
    secret_request = qovery.SecretRequest() # SecretRequest |  (optional)

    try:
        # Add a secret to the environment
        api_response = api_instance.create_environment_secret(environment_id, secret_request=secret_request)
        print("The response of EnvironmentSecretApi->create_environment_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentSecretApi->create_environment_secret: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID | 
 **secret_request** | [**SecretRequest**](SecretRequest.md)|  | [optional] 

### Return type

[**Secret**](Secret.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

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
> Secret create_environment_secret_alias(environment_id, secret_id, key=key)

Create a secret alias at the environment level

- Allows you to add an alias at environment level on an existing secret having higher scope, in order to customize its key. - You only have to specify a key in the request body - The system will create a new secret at environment level with the same value as the one corresponding to the secret id in the path - The response body will contain the newly created secret - Information regarding the aliased_secret will be exposed in the \"aliased_secret\" field of the newly created secret - You can't create an alias on an alias 

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import qovery
from qovery.models.key import Key
from qovery.models.secret import Secret
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
    api_instance = qovery.EnvironmentSecretApi(api_client)
    environment_id = 'environment_id_example' # str | Environment ID
    secret_id = 'secret_id_example' # str | Secret ID
    key = qovery.Key() # Key |  (optional)

    try:
        # Create a secret alias at the environment level
        api_response = api_instance.create_environment_secret_alias(environment_id, secret_id, key=key)
        print("The response of EnvironmentSecretApi->create_environment_secret_alias:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentSecretApi->create_environment_secret_alias: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID | 
 **secret_id** | **str**| Secret ID | 
 **key** | [**Key**](Key.md)|  | [optional] 

### Return type

[**Secret**](Secret.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

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
> Secret create_environment_secret_override(environment_id, secret_id, value=value)

Create a secret override at the environment level

- Allows you to override at environment level a secret that has a higher scope. - You only have to specify a value in the request body - The system will create a new secret at environment level with the same key as the one corresponding to the secret id in the path - The response body will contain the newly created secret - Information regarding the overridden_secret will be exposed in the \"overridden_secret\" field of the newly created secret 

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import qovery
from qovery.models.secret import Secret
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
    api_instance = qovery.EnvironmentSecretApi(api_client)
    environment_id = 'environment_id_example' # str | Environment ID
    secret_id = 'secret_id_example' # str | Secret ID
    value = qovery.Value() # Value |  (optional)

    try:
        # Create a secret override at the environment level
        api_response = api_instance.create_environment_secret_override(environment_id, secret_id, value=value)
        print("The response of EnvironmentSecretApi->create_environment_secret_override:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentSecretApi->create_environment_secret_override: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID | 
 **secret_id** | **str**| Secret ID | 
 **value** | [**Value**](Value.md)|  | [optional] 

### Return type

[**Secret**](Secret.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

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
    api_instance = qovery.EnvironmentSecretApi(api_client)
    environment_id = 'environment_id_example' # str | Environment ID
    secret_id = 'secret_id_example' # str | Secret ID

    try:
        # Delete a secret from the environment
        api_instance.delete_environment_secret(environment_id, secret_id)
    except Exception as e:
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

# **edit_environment_secret**
> Secret edit_environment_secret(environment_id, secret_id, secret_edit_request)

Edit a secret belonging to the environment

- You can't edit a BUILT_IN secret - For an override, you can't edit the key - For an alias, you can't edit the value - An override can only have a scope lower to the secret it is overriding (hierarchy is BUILT_IN > PROJECT > ENVIRONMENT > APPLICATION) 

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import qovery
from qovery.models.secret import Secret
from qovery.models.secret_edit_request import SecretEditRequest
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
    api_instance = qovery.EnvironmentSecretApi(api_client)
    environment_id = 'environment_id_example' # str | Environment ID
    secret_id = 'secret_id_example' # str | Secret ID
    secret_edit_request = qovery.SecretEditRequest() # SecretEditRequest | 

    try:
        # Edit a secret belonging to the environment
        api_response = api_instance.edit_environment_secret(environment_id, secret_id, secret_edit_request)
        print("The response of EnvironmentSecretApi->edit_environment_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentSecretApi->edit_environment_secret: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID | 
 **secret_id** | **str**| Secret ID | 
 **secret_edit_request** | [**SecretEditRequest**](SecretEditRequest.md)|  | 

### Return type

[**Secret**](Secret.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

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

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import qovery
from qovery.models.secret_response_list import SecretResponseList
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
    api_instance = qovery.EnvironmentSecretApi(api_client)
    environment_id = 'environment_id_example' # str | Environment ID

    try:
        # List environment secrets
        api_response = api_instance.list_environment_secrets(environment_id)
        print("The response of EnvironmentSecretApi->list_environment_secrets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentSecretApi->list_environment_secrets: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID | 

### Return type

[**SecretResponseList**](SecretResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

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

