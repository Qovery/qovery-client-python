# qovery.ContainersApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auto_deploy_container_environments**](ContainersApi.md#auto_deploy_container_environments) | **POST** /organization/{organizationId}/container/deploy | Auto deploy containers
[**create_container**](ContainersApi.md#create_container) | **POST** /environment/{environmentId}/container | Create a container
[**deploy_all_services**](ContainersApi.md#deploy_all_services) | **POST** /environment/{environmentId}/container/deploy | Deploy services
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

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import containers_api
from qovery.model.status import Status
from qovery.model.auto_deploy_container_environments_request import AutoDeployContainerEnvironmentsRequest
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
    api_instance = containers_api.ContainersApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    auto_deploy_container_environments_request = AutoDeployContainerEnvironmentsRequest(
        image_name="image_name_example",
        tag="tag_example",
    ) # AutoDeployContainerEnvironmentsRequest |  (optional)

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
        api_response = api_instance.auto_deploy_container_environments(organization_id, auto_deploy_container_environments_request=auto_deploy_container_environments_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainersApi->auto_deploy_container_environments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **auto_deploy_container_environments_request** | [**AutoDeployContainerEnvironmentsRequest**](AutoDeployContainerEnvironmentsRequest.md)|  | [optional]

### Return type

[**Status**](Status.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

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

# **create_container**
> ContainerResponse create_container(environment_id)

Create a container

### Example

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

[bearerAuth](../README.md#bearerAuth)

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

# **deploy_all_services**
> Status deploy_all_services(environment_id)

Deploy services

Update and deploy the selected services

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import containers_api
from qovery.model.deploy_all_request import DeployAllRequest
from qovery.model.status import Status
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
    api_instance = containers_api.ContainersApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID
    deploy_all_request = DeployAllRequest(
        applications=[
            DeployAllRequestApplicationsInner(
                application_id="application_id_example",
                git_commit_id="git_commit_id_example",
            ),
        ],
        containers=[
            DeployAllRequestContainersInner(
                id="id_example",
                image_tag="image_tag_example",
            ),
        ],
    ) # DeployAllRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Deploy services
        api_response = api_instance.deploy_all_services(environment_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainersApi->deploy_all_services: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Deploy services
        api_response = api_instance.deploy_all_services(environment_id, deploy_all_request=deploy_all_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainersApi->deploy_all_services: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID |
 **deploy_all_request** | [**DeployAllRequest**](DeployAllRequest.md)|  | [optional]

### Return type

[**Status**](Status.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Deployed services |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Operation is in progress |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_environment_container_current_scale**
> EnvironmentContainersCurrentScaleResponseList get_environment_container_current_scale(environment_id)

List current scaling information for each container

Returns min, max, and running number of instances for each container

### Example

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

[bearerAuth](../README.md#bearerAuth)

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

[bearerAuth](../README.md#bearerAuth)

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

[bearerAuth](../README.md#bearerAuth)

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

# Configure Bearer authorization (JWT): bearerAuth
configuration = qovery.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with qovery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = containers_api.ContainersApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID
    to_update = False # bool | return (or not) results that must be updated (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # List containers
        api_response = api_instance.list_container(environment_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainersApi->list_container: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List containers
        api_response = api_instance.list_container(environment_id, to_update=to_update)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainersApi->list_container: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID |
 **to_update** | **bool**| return (or not) results that must be updated | [optional] if omitted the server will use the default value of False

### Return type

[**ContainerResponseList**](ContainerResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

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

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import containers_api
from qovery.model.status import Status
from qovery.model.preview_container_environments_request import PreviewContainerEnvironmentsRequest
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
    api_instance = containers_api.ContainersApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    preview_container_environments_request = PreviewContainerEnvironmentsRequest(
        image_name="image_name_example",
        tag="tag_example",
    ) # PreviewContainerEnvironmentsRequest |  (optional)

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
        api_response = api_instance.preview_container_environments(organization_id, preview_container_environments_request=preview_container_environments_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainersApi->preview_container_environments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **preview_container_environments_request** | [**PreviewContainerEnvironmentsRequest**](PreviewContainerEnvironmentsRequest.md)|  | [optional]

### Return type

[**Status**](Status.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

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

