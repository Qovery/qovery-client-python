# qovery.HelmRepositoriesApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_helm_repository**](HelmRepositoriesApi.md#create_helm_repository) | **POST** /organization/{organizationId}/helmRepository | Create a helm repository
[**delete_helm_repository**](HelmRepositoriesApi.md#delete_helm_repository) | **DELETE** /organization/{organizationId}/helmRepository/{helmRepositoryId} | Delete a helm repository
[**edit_helm_repository**](HelmRepositoriesApi.md#edit_helm_repository) | **PUT** /organization/{organizationId}/helmRepository/{helmRepositoryId} | Edit a helm repository
[**get_helm_repository**](HelmRepositoriesApi.md#get_helm_repository) | **GET** /organization/{organizationId}/helmRepository/{helmRepositoryId} | Get a helm repository
[**list_available_helm_repository**](HelmRepositoriesApi.md#list_available_helm_repository) | **GET** /availableHelmRepository | List supported helm repository
[**list_helm_repository**](HelmRepositoriesApi.md#list_helm_repository) | **GET** /organization/{organizationId}/helmRepository | List organization helm repositories


# **create_helm_repository**
> HelmRepositoryResponse create_helm_repository(organization_id, helm_repository_request=helm_repository_request)

Create a helm repository

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import os
import qovery
from qovery.models.helm_repository_request import HelmRepositoryRequest
from qovery.models.helm_repository_response import HelmRepositoryResponse
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
    api_instance = qovery.HelmRepositoriesApi(api_client)
    organization_id = 'organization_id_example' # str | Organization ID
    helm_repository_request = qovery.HelmRepositoryRequest() # HelmRepositoryRequest |  (optional)

    try:
        # Create a helm repository
        api_response = api_instance.create_helm_repository(organization_id, helm_repository_request=helm_repository_request)
        print("The response of HelmRepositoriesApi->create_helm_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HelmRepositoriesApi->create_helm_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID | 
 **helm_repository_request** | [**HelmRepositoryRequest**](HelmRepositoryRequest.md)|  | [optional] 

### Return type

[**HelmRepositoryResponse**](HelmRepositoryResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create a helm repository |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_helm_repository**
> delete_helm_repository(organization_id, helm_repository_id)

Delete a helm repository

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
    api_instance = qovery.HelmRepositoriesApi(api_client)
    organization_id = 'organization_id_example' # str | Organization ID
    helm_repository_id = 'helm_repository_id_example' # str | Helm chart repository ID

    try:
        # Delete a helm repository
        api_instance.delete_helm_repository(organization_id, helm_repository_id)
    except Exception as e:
        print("Exception when calling HelmRepositoriesApi->delete_helm_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID | 
 **helm_repository_id** | **str**| Helm chart repository ID | 

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

# **edit_helm_repository**
> HelmRepositoryResponse edit_helm_repository(organization_id, helm_repository_id, helm_repository_request=helm_repository_request)

Edit a helm repository

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import os
import qovery
from qovery.models.helm_repository_request import HelmRepositoryRequest
from qovery.models.helm_repository_response import HelmRepositoryResponse
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
    api_instance = qovery.HelmRepositoriesApi(api_client)
    organization_id = 'organization_id_example' # str | Organization ID
    helm_repository_id = 'helm_repository_id_example' # str | Helm chart repository ID
    helm_repository_request = qovery.HelmRepositoryRequest() # HelmRepositoryRequest |  (optional)

    try:
        # Edit a helm repository
        api_response = api_instance.edit_helm_repository(organization_id, helm_repository_id, helm_repository_request=helm_repository_request)
        print("The response of HelmRepositoriesApi->edit_helm_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HelmRepositoriesApi->edit_helm_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID | 
 **helm_repository_id** | **str**| Helm chart repository ID | 
 **helm_repository_request** | [**HelmRepositoryRequest**](HelmRepositoryRequest.md)|  | [optional] 

### Return type

[**HelmRepositoryResponse**](HelmRepositoryResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Edited the helm repository |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_helm_repository**
> HelmRepositoryResponse get_helm_repository(organization_id, helm_repository_id)

Get a helm repository

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import os
import qovery
from qovery.models.helm_repository_response import HelmRepositoryResponse
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
    api_instance = qovery.HelmRepositoriesApi(api_client)
    organization_id = 'organization_id_example' # str | Organization ID
    helm_repository_id = 'helm_repository_id_example' # str | Helm chart repository ID

    try:
        # Get a helm repository
        api_response = api_instance.get_helm_repository(organization_id, helm_repository_id)
        print("The response of HelmRepositoriesApi->get_helm_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HelmRepositoriesApi->get_helm_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID | 
 **helm_repository_id** | **str**| Helm chart repository ID | 

### Return type

[**HelmRepositoryResponse**](HelmRepositoryResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The helm repository |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_available_helm_repository**
> AvailableHelmRepositoryResponseList list_available_helm_repository()

List supported helm repository

List supported helm repository by Qovery and get the mandatory authentification configuration.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import os
import qovery
from qovery.models.available_helm_repository_response_list import AvailableHelmRepositoryResponseList
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
    api_instance = qovery.HelmRepositoriesApi(api_client)

    try:
        # List supported helm repository
        api_response = api_instance.list_available_helm_repository()
        print("The response of HelmRepositoriesApi->list_available_helm_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HelmRepositoriesApi->list_available_helm_repository: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AvailableHelmRepositoryResponseList**](AvailableHelmRepositoryResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | supported helm repositories |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_helm_repository**
> HelmRepositoryResponseList list_helm_repository(organization_id)

List organization helm repositories

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import os
import qovery
from qovery.models.helm_repository_response_list import HelmRepositoryResponseList
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
    api_instance = qovery.HelmRepositoriesApi(api_client)
    organization_id = 'organization_id_example' # str | Organization ID

    try:
        # List organization helm repositories
        api_response = api_instance.list_helm_repository(organization_id)
        print("The response of HelmRepositoriesApi->list_helm_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HelmRepositoriesApi->list_helm_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID | 

### Return type

[**HelmRepositoryResponseList**](HelmRepositoryResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List helm repositories |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

