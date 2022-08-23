# qovery.ContainerRegistriesApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_container_registry**](ContainerRegistriesApi.md#create_container_registry) | **POST** /organization/{organizationId}/containerRegistry | Create a container registry
[**delete_container_registry**](ContainerRegistriesApi.md#delete_container_registry) | **DELETE** /organization/{organizationId}/containerRegistry/{containerRegistryId} | NOT YET IMPLEMENTED - Delete a container registry
[**list_available_container_registry**](ContainerRegistriesApi.md#list_available_container_registry) | **GET** /availableContainerRegistry | List supported container registries
[**list_container_registry**](ContainerRegistriesApi.md#list_container_registry) | **GET** /organization/{organizationId}/containerRegistry | NOT YET IMPLEMENTED - List organization container registries


# **create_container_registry**
> ContainerRegistryResponse create_container_registry(organization_id)

Create a container registry

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import container_registries_api
from qovery.model.container_registry_request import ContainerRegistryRequest
from qovery.model.container_registry_response import ContainerRegistryResponse
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
    api_instance = container_registries_api.ContainerRegistriesApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    container_registry_request = ContainerRegistryRequest(
        name="name_example",
        kind=ContainerRegistryKindEnum("ECR"),
        description="description_example",
        url="url_example",
        config={},
    ) # ContainerRegistryRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a container registry
        api_response = api_instance.create_container_registry(organization_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainerRegistriesApi->create_container_registry: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a container registry
        api_response = api_instance.create_container_registry(organization_id, container_registry_request=container_registry_request)
        pprint(api_response)
    except qovery.ApiException as e:
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

[bearerAuth](../README.md#bearerAuth)

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
> delete_container_registry(organization_id)

NOT YET IMPLEMENTED - Delete a container registry

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import container_registries_api
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
    api_instance = container_registries_api.ContainerRegistriesApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID

    # example passing only required values which don't have defaults set
    try:
        # NOT YET IMPLEMENTED - Delete a container registry
        api_instance.delete_container_registry(organization_id)
    except qovery.ApiException as e:
        print("Exception when calling ContainerRegistriesApi->delete_container_registry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |

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

# **list_available_container_registry**
> AvailableContainerRegistryResponse list_available_container_registry()

List supported container registries

List supported container registries by Qovery and get the mandatory authentification configuration.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import container_registries_api
from qovery.model.available_container_registry_response import AvailableContainerRegistryResponse
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
    api_instance = container_registries_api.ContainerRegistriesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List supported container registries
        api_response = api_instance.list_available_container_registry()
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainerRegistriesApi->list_available_container_registry: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AvailableContainerRegistryResponse**](AvailableContainerRegistryResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

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
> ListContainerRegistry200Response list_container_registry(organization_id)

NOT YET IMPLEMENTED - List organization container registries

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import container_registries_api
from qovery.model.list_container_registry200_response import ListContainerRegistry200Response
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
    api_instance = container_registries_api.ContainerRegistriesApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID

    # example passing only required values which don't have defaults set
    try:
        # NOT YET IMPLEMENTED - List organization container registries
        api_response = api_instance.list_container_registry(organization_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainerRegistriesApi->list_container_registry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |

### Return type

[**ListContainerRegistry200Response**](ListContainerRegistry200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

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

