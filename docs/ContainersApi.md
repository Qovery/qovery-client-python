# qovery.ContainersApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auto_deploy_container_environments**](ContainersApi.md#auto_deploy_container_environments) | **POST** /organization/{organizationId}/container/deploy | Auto deploy containers
[**clone_container**](ContainersApi.md#clone_container) | **POST** /container/{containerId}/clone | Clone container
[**clone_helm**](ContainersApi.md#clone_helm) | **POST** /helm/{helmId}/clone | Clone helm
[**create_container**](ContainersApi.md#create_container) | **POST** /environment/{environmentId}/container | Create a container
[**get_container_registry_container_status**](ContainersApi.md#get_container_registry_container_status) | **GET** /organization/{organizationId}/containerRegistry/{containerRegistryId}/container/status | List all container registry container statuses
[**get_default_container_advanced_settings**](ContainersApi.md#get_default_container_advanced_settings) | **GET** /defaultContainerAdvancedSettings | List default container advanced settings
[**get_environment_container_current_scale**](ContainersApi.md#get_environment_container_current_scale) | **GET** /environment/{environmentId}/container/currentScale | List current scaling information for each container
[**get_environment_container_current_storage**](ContainersApi.md#get_environment_container_current_storage) | **GET** /environment/{environmentId}/container/currentStorage | List current storage disk usage for each containers
[**get_environment_container_status**](ContainersApi.md#get_environment_container_status) | **GET** /environment/{environmentId}/container/status | List all environment container statuses
[**list_container**](ContainersApi.md#list_container) | **GET** /environment/{environmentId}/container | List containers
[**preview_container_environments**](ContainersApi.md#preview_container_environments) | **POST** /organization/{organizationId}/container/preview | Preview container environments


# **auto_deploy_container_environments**
> Status auto_deploy_container_environments(organization_id)

Auto deploy containers

Triggers a new container deploy in each environment matching the following conditions - environment should have the auto-deploy enabled - the container should have the same image name and a different tag 

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import containers_api
from qovery.model.status import Status
from qovery.model.organization_container_auto_deploy_request import OrganizationContainerAutoDeployRequest
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
    api_instance = containers_api.ContainersApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    organization_container_auto_deploy_request = OrganizationContainerAutoDeployRequest(
        image_name="image_name_example",
        tag="tag_example",
    ) # OrganizationContainerAutoDeployRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Auto deploy containers
        api_response = api_instance.auto_deploy_container_environments(organization_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainersApi->auto_deploy_container_environments: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Auto deploy containers
        api_response = api_instance.auto_deploy_container_environments(organization_id, organization_container_auto_deploy_request=organization_container_auto_deploy_request)
        pprint(api_response)
    except qovery.ApiException as e:
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
> ContainerResponse clone_container(container_id)

Clone container

This will create a new container with the same configuration on the targeted environment Id.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import containers_api
from qovery.model.clone_service_request import CloneServiceRequest
from qovery.model.container_response import ContainerResponse
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
    api_instance = containers_api.ContainersApi(api_client)
    container_id = "containerId_example" # str | Container ID
    clone_service_request = CloneServiceRequest(
        name="name_example",
        environment_id="environment_id_example",
    ) # CloneServiceRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Clone container
        api_response = api_instance.clone_container(container_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainersApi->clone_container: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Clone container
        api_response = api_instance.clone_container(container_id, clone_service_request=clone_service_request)
        pprint(api_response)
    except qovery.ApiException as e:
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

# **clone_helm**
> HelmResponse clone_helm(helm_id)

Clone helm

This will create a new helm with the same configuration on the targeted environment Id.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import containers_api
from qovery.model.clone_service_request import CloneServiceRequest
from qovery.model.helm_response import HelmResponse
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
    api_instance = containers_api.ContainersApi(api_client)
    helm_id = "helmId_example" # str | Helm ID
    clone_service_request = CloneServiceRequest(
        name="name_example",
        environment_id="environment_id_example",
    ) # CloneServiceRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Clone helm
        api_response = api_instance.clone_helm(helm_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainersApi->clone_helm: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Clone helm
        api_response = api_instance.clone_helm(helm_id, clone_service_request=clone_service_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainersApi->clone_helm: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **helm_id** | **str**| Helm ID |
 **clone_service_request** | [**CloneServiceRequest**](CloneServiceRequest.md)|  | [optional]

### Return type

[**HelmResponse**](HelmResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Helm clone has been requested |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Operation is in progress |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_container**
> ContainerResponse create_container(environment_id)

Create a container

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import containers_api
from qovery.model.container_request import ContainerRequest
from qovery.model.container_response import ContainerResponse
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
    api_instance = containers_api.ContainersApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID
    container_request = ContainerRequest(None) # ContainerRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a container
        api_response = api_instance.create_container(environment_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainersApi->create_container: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a container
        api_response = api_instance.create_container(environment_id, container_request=container_request)
        pprint(api_response)
    except qovery.ApiException as e:
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
import qovery
from qovery.api import containers_api
from qovery.model.reference_object_status_response_list import ReferenceObjectStatusResponseList
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
    api_instance = containers_api.ContainersApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    container_registry_id = "containerRegistryId_example" # str | Container Registry ID

    # example passing only required values which don't have defaults set
    try:
        # List all container registry container statuses
        api_response = api_instance.get_container_registry_container_status(organization_id, container_registry_id)
        pprint(api_response)
    except qovery.ApiException as e:
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
import qovery
from qovery.api import containers_api
from qovery.model.container_advanced_settings import ContainerAdvancedSettings
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
    api_instance = containers_api.ContainersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List default container advanced settings
        api_response = api_instance.get_default_container_advanced_settings()
        pprint(api_response)
    except qovery.ApiException as e:
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

# **get_environment_container_current_scale**
> EnvironmentContainersCurrentScaleResponseList get_environment_container_current_scale(environment_id)

List current scaling information for each container

Returns min, max, and running number of instances for each container

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import containers_api
from qovery.model.environment_containers_current_scale_response_list import EnvironmentContainersCurrentScaleResponseList
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
    api_instance = containers_api.ContainersApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID

    # example passing only required values which don't have defaults set
    try:
        # List current scaling information for each container
        api_response = api_instance.get_environment_container_current_scale(environment_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainersApi->get_environment_container_current_scale: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID |

### Return type

[**EnvironmentContainersCurrentScaleResponseList**](EnvironmentContainersCurrentScaleResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list containers with current scaling |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_environment_container_current_storage**
> EnvironmentContainersStorageResponseList get_environment_container_current_storage(environment_id)

List current storage disk usage for each containers

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import containers_api
from qovery.model.environment_containers_storage_response_list import EnvironmentContainersStorageResponseList
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
    api_instance = containers_api.ContainersApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID

    # example passing only required values which don't have defaults set
    try:
        # List current storage disk usage for each containers
        api_response = api_instance.get_environment_container_current_storage(environment_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainersApi->get_environment_container_current_storage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID |

### Return type

[**EnvironmentContainersStorageResponseList**](EnvironmentContainersStorageResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current storage disk usage |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

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
import qovery
from qovery.api import containers_api
from qovery.model.reference_object_status_response_list import ReferenceObjectStatusResponseList
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
    api_instance = containers_api.ContainersApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID

    # example passing only required values which don't have defaults set
    try:
        # List all environment container statuses
        api_response = api_instance.get_environment_container_status(environment_id)
        pprint(api_response)
    except qovery.ApiException as e:
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
import qovery
from qovery.api import containers_api
from qovery.model.container_response_list import ContainerResponseList
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
    api_instance = containers_api.ContainersApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID

    # example passing only required values which don't have defaults set
    try:
        # List containers
        api_response = api_instance.list_container(environment_id)
        pprint(api_response)
    except qovery.ApiException as e:
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
> Status preview_container_environments(organization_id)

Preview container environments

Triggers a new container preview for each environment matching the following conditions - preview environment feature should be enabled for the container - the container should have the same image name and a different tag 

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import containers_api
from qovery.model.status import Status
from qovery.model.organization_container_preview_request import OrganizationContainerPreviewRequest
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
    api_instance = containers_api.ContainersApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    organization_container_preview_request = OrganizationContainerPreviewRequest(
        image_name="image_name_example",
        tag="tag_example",
    ) # OrganizationContainerPreviewRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Preview container environments
        api_response = api_instance.preview_container_environments(organization_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainersApi->preview_container_environments: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Preview container environments
        api_response = api_instance.preview_container_environments(organization_id, organization_container_preview_request=organization_container_preview_request)
        pprint(api_response)
    except qovery.ApiException as e:
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

