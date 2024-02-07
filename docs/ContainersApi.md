# qovery.ContainersApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auto_deploy_container_environments**](ContainersApi.md#auto_deploy_container_environments) | **POST** /organization/{organizationId}/container/deploy | Auto deploy containers
[**clone_container**](ContainersApi.md#clone_container) | **POST** /container/{containerId}/clone | Clone container
[**create_container**](ContainersApi.md#create_container) | **POST** /environment/{environmentId}/container | Create a container
[**get_container_registry_container_status**](ContainersApi.md#get_container_registry_container_status) | **GET** /organization/{organizationId}/containerRegistry/{containerRegistryId}/container/status | List all container registry container statuses
[**get_default_container_advanced_settings**](ContainersApi.md#get_default_container_advanced_settings) | **GET** /defaultContainerAdvancedSettings | List default container advanced settings
[**get_environment_container_status**](ContainersApi.md#get_environment_container_status) | **GET** /environment/{environmentId}/container/status | List all environment container statuses
[**list_container**](ContainersApi.md#list_container) | **GET** /environment/{environmentId}/container | List containers
[**preview_container_environments**](ContainersApi.md#preview_container_environments) | **POST** /organization/{organizationId}/container/preview | Preview container environments


# **auto_deploy_container_environments**
> Status auto_deploy_container_environments(organization_id, organization_container_auto_deploy_request=organization_container_auto_deploy_request)

Auto deploy containers

Triggers a new container deploy in each environment matching the following conditions - environment should have the auto-deploy enabled - the container should have the same image name and a different tag 

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import os
import qovery
from qovery.models.organization_container_auto_deploy_request import OrganizationContainerAutoDeployRequest
from qovery.models.status import Status
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
    api_instance = qovery.ContainersApi(api_client)
    organization_id = 'organization_id_example' # str | Organization ID
    organization_container_auto_deploy_request = qovery.OrganizationContainerAutoDeployRequest() # OrganizationContainerAutoDeployRequest |  (optional)

    try:
        # Auto deploy containers
        api_response = api_instance.auto_deploy_container_environments(organization_id, organization_container_auto_deploy_request=organization_container_auto_deploy_request)
        print("The response of ContainersApi->auto_deploy_container_environments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainersApi->auto_deploy_container_environments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID | 
 **organization_container_auto_deploy_request** | [**OrganizationContainerAutoDeployRequest**](OrganizationContainerAutoDeployRequest.md)|  | [optional] 

### Return type

[**Status**](Status.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Deployed containers |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Operation is in progress |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clone_container**
> ContainerResponse clone_container(container_id, clone_service_request=clone_service_request)

Clone container

This will create a new container with the same configuration on the targeted environment Id.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import os
import qovery
from qovery.models.clone_service_request import CloneServiceRequest
from qovery.models.container_response import ContainerResponse
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
    api_instance = qovery.ContainersApi(api_client)
    container_id = 'container_id_example' # str | Container ID
    clone_service_request = qovery.CloneServiceRequest() # CloneServiceRequest |  (optional)

    try:
        # Clone container
        api_response = api_instance.clone_container(container_id, clone_service_request=clone_service_request)
        print("The response of ContainersApi->clone_container:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainersApi->clone_container: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Container ID | 
 **clone_service_request** | [**CloneServiceRequest**](CloneServiceRequest.md)|  | [optional] 

### Return type

[**ContainerResponse**](ContainerResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Container clone has been requested |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Operation is in progress |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_container**
> ContainerResponse create_container(environment_id, container_request=container_request)

Create a container

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import os
import qovery
from qovery.models.container_request import ContainerRequest
from qovery.models.container_response import ContainerResponse
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
    api_instance = qovery.ContainersApi(api_client)
    environment_id = 'environment_id_example' # str | Environment ID
    container_request = qovery.ContainerRequest() # ContainerRequest |  (optional)

    try:
        # Create a container
        api_response = api_instance.create_container(environment_id, container_request=container_request)
        print("The response of ContainersApi->create_container:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainersApi->create_container: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID | 
 **container_request** | [**ContainerRequest**](ContainerRequest.md)|  | [optional] 

### Return type

[**ContainerResponse**](ContainerResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create container |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Container name within the environment is already taken |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_container_registry_container_status**
> ReferenceObjectStatusResponseList get_container_registry_container_status(organization_id, container_registry_id)

List all container registry container statuses

Returns a list of containers with only their id and status.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import os
import qovery
from qovery.models.reference_object_status_response_list import ReferenceObjectStatusResponseList
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
    api_instance = qovery.ContainersApi(api_client)
    organization_id = 'organization_id_example' # str | Organization ID
    container_registry_id = 'container_registry_id_example' # str | Container Registry ID

    try:
        # List all container registry container statuses
        api_response = api_instance.get_container_registry_container_status(organization_id, container_registry_id)
        print("The response of ContainersApi->get_container_registry_container_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainersApi->get_container_registry_container_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID | 
 **container_registry_id** | **str**| Container Registry ID | 

### Return type

[**ReferenceObjectStatusResponseList**](ReferenceObjectStatusResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get status |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_default_container_advanced_settings**
> ContainerAdvancedSettings get_default_container_advanced_settings()

List default container advanced settings

Default values for each setting are available in [our documentation](https://hub.qovery.com/docs/using-qovery/configuration/advanced-settings/)

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import os
import qovery
from qovery.models.container_advanced_settings import ContainerAdvancedSettings
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
    api_instance = qovery.ContainersApi(api_client)

    try:
        # List default container advanced settings
        api_response = api_instance.get_default_container_advanced_settings()
        print("The response of ContainersApi->get_default_container_advanced_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainersApi->get_default_container_advanced_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ContainerAdvancedSettings**](ContainerAdvancedSettings.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default container advanced settings |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_environment_container_status**
> ReferenceObjectStatusResponseList get_environment_container_status(environment_id)

List all environment container statuses

Returns a list of containers with only their id and status.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import os
import qovery
from qovery.models.reference_object_status_response_list import ReferenceObjectStatusResponseList
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
    api_instance = qovery.ContainersApi(api_client)
    environment_id = 'environment_id_example' # str | Environment ID

    try:
        # List all environment container statuses
        api_response = api_instance.get_environment_container_status(environment_id)
        print("The response of ContainersApi->get_environment_container_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainersApi->get_environment_container_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID | 

### Return type

[**ReferenceObjectStatusResponseList**](ReferenceObjectStatusResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get status |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_container**
> ContainerResponseList list_container(environment_id)

List containers

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import os
import qovery
from qovery.models.container_response_list import ContainerResponseList
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
    api_instance = qovery.ContainersApi(api_client)
    environment_id = 'environment_id_example' # str | Environment ID

    try:
        # List containers
        api_response = api_instance.list_container(environment_id)
        print("The response of ContainersApi->list_container:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainersApi->list_container: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID | 

### Return type

[**ContainerResponseList**](ContainerResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List containers |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preview_container_environments**
> Status preview_container_environments(organization_id, organization_container_preview_request=organization_container_preview_request)

Preview container environments

Triggers a new container preview for each environment matching the following conditions - preview environment feature should be enabled for the container - the container should have the same image name and a different tag 

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import os
import qovery
from qovery.models.organization_container_preview_request import OrganizationContainerPreviewRequest
from qovery.models.status import Status
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
    api_instance = qovery.ContainersApi(api_client)
    organization_id = 'organization_id_example' # str | Organization ID
    organization_container_preview_request = qovery.OrganizationContainerPreviewRequest() # OrganizationContainerPreviewRequest |  (optional)

    try:
        # Preview container environments
        api_response = api_instance.preview_container_environments(organization_id, organization_container_preview_request=organization_container_preview_request)
        print("The response of ContainersApi->preview_container_environments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainersApi->preview_container_environments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID | 
 **organization_container_preview_request** | [**OrganizationContainerPreviewRequest**](OrganizationContainerPreviewRequest.md)|  | [optional] 

### Return type

[**Status**](Status.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Preview environments processing |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Operation is in progress |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

