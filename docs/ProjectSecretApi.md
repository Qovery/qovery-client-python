# qovery.ProjectSecretApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_secret**](ProjectSecretApi.md#create_project_secret) | **POST** /project/{projectId}/secret | Add a secret to the project
[**create_project_secret_alias**](ProjectSecretApi.md#create_project_secret_alias) | **POST** /project/{projectId}/secret/{secretId}/alias | Create a secret alias at the project level
[**create_project_secret_override**](ProjectSecretApi.md#create_project_secret_override) | **POST** /project/{projectId}/secret/{secretId}/override | Create a secret override at the project level
[**delete_project_secret**](ProjectSecretApi.md#delete_project_secret) | **DELETE** /project/{projectId}/secret/{secretId} | Delete a secret from a project
[**edit_project_secret**](ProjectSecretApi.md#edit_project_secret) | **PUT** /project/{projectId}/secret/{secretId} | Edit a secret belonging to the project
[**list_project_secrets**](ProjectSecretApi.md#list_project_secrets) | **GET** /project/{projectId}/secret | List project secrets


# **create_project_secret**
> Secret create_project_secret(project_id)

Add a secret to the project

- Add a secret to the project.   - If the secret key already exists, then it will be replaced by the new one.   - If the secret value points toward an existing secret key, it will be considered as an alias. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import project_secret_api
from qovery.model.secret import Secret
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
    api_instance = project_secret_api.ProjectSecretApi(api_client)
    project_id = "projectId_example" # str | Project ID
    secret_request = SecretRequest(
        key="key_example",
        value="value_example",
        mount_path="mount_path_example",
    ) # SecretRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add a secret to the project
        api_response = api_instance.create_project_secret(project_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ProjectSecretApi->create_project_secret: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add a secret to the project
        api_response = api_instance.create_project_secret(project_id, secret_request=secret_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ProjectSecretApi->create_project_secret: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID |
 **secret_request** | [**SecretRequest**](SecretRequest.md)|  | [optional]

### Return type

[**Secret**](Secret.md)

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

# **create_project_secret_alias**
> Secret create_project_secret_alias(project_id, secret_id)

Create a secret alias at the project level

- Allows you to add an alias at project level on an existing secret having higher scope, in order to customize its key. - You only have to specify a key in the request body - The system will create a new secret at project level with the same value as the one corresponding to the secret id in the path - The response body will contain the newly created secret - Information regarding the aliased_secret will be exposed in the \"aliased_secret\" field of the newly created secret - Only 1 alias level is allowed. You can't create an alias on an alias 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import project_secret_api
from qovery.model.secret import Secret
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
    api_instance = project_secret_api.ProjectSecretApi(api_client)
    project_id = "projectId_example" # str | Project ID
    secret_id = "secretId_example" # str | Secret ID
    key = Key(
        key="key_example",
    ) # Key |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a secret alias at the project level
        api_response = api_instance.create_project_secret_alias(project_id, secret_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ProjectSecretApi->create_project_secret_alias: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a secret alias at the project level
        api_response = api_instance.create_project_secret_alias(project_id, secret_id, key=key)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ProjectSecretApi->create_project_secret_alias: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID |
 **secret_id** | **str**| Secret ID |
 **key** | [**Key**](Key.md)|  | [optional]

### Return type

[**Secret**](Secret.md)

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

# **create_project_secret_override**
> Secret create_project_secret_override(project_id, secret_id)

Create a secret override at the project level

- Allows you to override at project level a secret that has a higher scope. - You only have to specify a value in the request body - The system will create a new secret at project level with the same key as the one corresponding to the secret id in the path - The response body will contain the newly created secret - Information regarding the overridden_secret will be exposed in the \"overridden_secret\" field of the newly created secret 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import project_secret_api
from qovery.model.secret import Secret
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
    api_instance = project_secret_api.ProjectSecretApi(api_client)
    project_id = "projectId_example" # str | Project ID
    secret_id = "secretId_example" # str | Secret ID
    value = Value(
        value="value_example",
    ) # Value |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a secret override at the project level
        api_response = api_instance.create_project_secret_override(project_id, secret_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ProjectSecretApi->create_project_secret_override: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a secret override at the project level
        api_response = api_instance.create_project_secret_override(project_id, secret_id, value=value)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ProjectSecretApi->create_project_secret_override: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID |
 **secret_id** | **str**| Secret ID |
 **value** | [**Value**](Value.md)|  | [optional]

### Return type

[**Secret**](Secret.md)

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

# **delete_project_secret**
> delete_project_secret(project_id, secret_id)

Delete a secret from a project

- To delete a secret you must have the project user permission - You can't delete a BUILT_IN secret - If you delete a secret having override or alias, the associated override/alias will be deleted as well  operationId: deleteProjectSecret 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import project_secret_api
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
    api_instance = project_secret_api.ProjectSecretApi(api_client)
    project_id = "projectId_example" # str | Project ID
    secret_id = "secretId_example" # str | Secret ID

    # example passing only required values which don't have defaults set
    try:
        # Delete a secret from a project
        api_instance.delete_project_secret(project_id, secret_id)
    except qovery.ApiException as e:
        print("Exception when calling ProjectSecretApi->delete_project_secret: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID |
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

# **edit_project_secret**
> Secret edit_project_secret(project_id, secret_id, secret_edit_request)

Edit a secret belonging to the project

- You can't edit a BUILT_IN secret - For an override, you can't edit the key - For an alias, you can't edit the value - An override can only have a scope lower to the secret it is overriding (hierarchy is BUILT_IN > PROJECT > ENVIRONMENT > APPLICATION) 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import project_secret_api
from qovery.model.secret_edit_request import SecretEditRequest
from qovery.model.secret import Secret
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
    api_instance = project_secret_api.ProjectSecretApi(api_client)
    project_id = "projectId_example" # str | Project ID
    secret_id = "secretId_example" # str | Secret ID
    secret_edit_request = SecretEditRequest(
        value="value_example",
        key="key_example",
    ) # SecretEditRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Edit a secret belonging to the project
        api_response = api_instance.edit_project_secret(project_id, secret_id, secret_edit_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ProjectSecretApi->edit_project_secret: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID |
 **secret_id** | **str**| Secret ID |
 **secret_edit_request** | [**SecretEditRequest**](SecretEditRequest.md)|  |

### Return type

[**Secret**](Secret.md)

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

# **list_project_secrets**
> SecretResponseList list_project_secrets(project_id)

List project secrets

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import project_secret_api
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
    api_instance = project_secret_api.ProjectSecretApi(api_client)
    project_id = "projectId_example" # str | Project ID

    # example passing only required values which don't have defaults set
    try:
        # List project secrets
        api_response = api_instance.list_project_secrets(project_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ProjectSecretApi->list_project_secrets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID |

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
**200** | List project secrets |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

