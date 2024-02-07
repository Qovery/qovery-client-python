# qovery.ContainerRegistriesApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_container_registry**](ContainerRegistriesApi.md#create_container_registry) | **POST** /organization/{organizationId}/containerRegistry | Create a container registry
[**delete_container_registry**](ContainerRegistriesApi.md#delete_container_registry) | **DELETE** /organization/{organizationId}/containerRegistry/{containerRegistryId} | Delete a container registry
[**edit_container_registry**](ContainerRegistriesApi.md#edit_container_registry) | **PUT** /organization/{organizationId}/containerRegistry/{containerRegistryId} | Edit a container registry
[**get_container_registry**](ContainerRegistriesApi.md#get_container_registry) | **GET** /organization/{organizationId}/containerRegistry/{containerRegistryId} | Get a container registry
[**list_available_container_registry**](ContainerRegistriesApi.md#list_available_container_registry) | **GET** /availableContainerRegistry | List supported container registries
[**list_container_registry**](ContainerRegistriesApi.md#list_container_registry) | **GET** /organization/{organizationId}/containerRegistry | List organization container registries


# **create_container_registry**
> ContainerRegistryResponse create_container_registry(organization_id, container_registry_request=container_registry_request)

Create a container registry

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import os
import qovery
from qovery.models.container_registry_request import ContainerRegistryRequest
from qovery.models.container_registry_response import ContainerRegistryResponse
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
    api_instance = qovery.ContainerRegistriesApi(api_client)
    organization_id = 'organization_id_example' # str | Organization ID
    container_registry_request = qovery.ContainerRegistryRequest() # ContainerRegistryRequest |  (optional)

    try:
        # Create a container registry
        api_response = api_instance.create_container_registry(organization_id, container_registry_request=container_registry_request)
        print("The response of ContainerRegistriesApi->create_container_registry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainerRegistriesApi->create_container_registry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID | 
 **container_registry_request** | [**ContainerRegistryRequest**](ContainerRegistryRequest.md)|  | [optional] 

### Return type

[**ContainerRegistryResponse**](ContainerRegistryResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create a Container Registry |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_container_registry**
> delete_container_registry(organization_id, container_registry_id)

Delete a container registry

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
    api_instance = qovery.ContainerRegistriesApi(api_client)
    organization_id = 'organization_id_example' # str | Organization ID
    container_registry_id = 'container_registry_id_example' # str | Container Registry ID

    try:
        # Delete a container registry
        api_instance.delete_container_registry(organization_id, container_registry_id)
    except Exception as e:
        print("Exception when calling ContainerRegistriesApi->delete_container_registry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID | 
 **container_registry_id** | **str**| Container Registry ID | 

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

# **edit_container_registry**
> ContainerRegistryResponse edit_container_registry(organization_id, container_registry_id, container_registry_request=container_registry_request)

Edit a container registry

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import os
import qovery
from qovery.models.container_registry_request import ContainerRegistryRequest
from qovery.models.container_registry_response import ContainerRegistryResponse
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
    api_instance = qovery.ContainerRegistriesApi(api_client)
    organization_id = 'organization_id_example' # str | Organization ID
    container_registry_id = 'container_registry_id_example' # str | Container Registry ID
    container_registry_request = qovery.ContainerRegistryRequest() # ContainerRegistryRequest |  (optional)

    try:
        # Edit a container registry
        api_response = api_instance.edit_container_registry(organization_id, container_registry_id, container_registry_request=container_registry_request)
        print("The response of ContainerRegistriesApi->edit_container_registry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainerRegistriesApi->edit_container_registry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID | 
 **container_registry_id** | **str**| Container Registry ID | 
 **container_registry_request** | [**ContainerRegistryRequest**](ContainerRegistryRequest.md)|  | [optional] 

### Return type

[**ContainerRegistryResponse**](ContainerRegistryResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Edited the container registry |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_container_registry**
> ContainerRegistryResponse get_container_registry(organization_id, container_registry_id)

Get a container registry

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import os
import qovery
from qovery.models.container_registry_response import ContainerRegistryResponse
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
    api_instance = qovery.ContainerRegistriesApi(api_client)
    organization_id = 'organization_id_example' # str | Organization ID
    container_registry_id = 'container_registry_id_example' # str | Container Registry ID

    try:
        # Get a container registry
        api_response = api_instance.get_container_registry(organization_id, container_registry_id)
        print("The response of ContainerRegistriesApi->get_container_registry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainerRegistriesApi->get_container_registry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID | 
 **container_registry_id** | **str**| Container Registry ID | 

### Return type

[**ContainerRegistryResponse**](ContainerRegistryResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The container registry |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_available_container_registry**
> AvailableContainerRegistryResponseList list_available_container_registry()

List supported container registries

List supported container registries by Qovery and get the mandatory authentification configuration.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import os
import qovery
from qovery.models.available_container_registry_response_list import AvailableContainerRegistryResponseList
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
    api_instance = qovery.ContainerRegistriesApi(api_client)

    try:
        # List supported container registries
        api_response = api_instance.list_available_container_registry()
        print("The response of ContainerRegistriesApi->list_available_container_registry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainerRegistriesApi->list_available_container_registry: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AvailableContainerRegistryResponseList**](AvailableContainerRegistryResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | supported container registries |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_container_registry**
> ContainerRegistryResponseList list_container_registry(organization_id)

List organization container registries

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import os
import qovery
from qovery.models.container_registry_response_list import ContainerRegistryResponseList
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
    api_instance = qovery.ContainerRegistriesApi(api_client)
    organization_id = 'organization_id_example' # str | Organization ID

    try:
        # List organization container registries
        api_response = api_instance.list_container_registry(organization_id)
        print("The response of ContainerRegistriesApi->list_container_registry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainerRegistriesApi->list_container_registry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID | 

### Return type

[**ContainerRegistryResponseList**](ContainerRegistryResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List container registries |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

