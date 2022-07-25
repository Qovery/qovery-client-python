# qovery.ContainerActionsApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deploy_container**](ContainerActionsApi.md#deploy_container) | **POST** /container/{containerId}/deploy | NOT YET IMPLEMENTED - Deploy container
[**preview_environment_container**](ContainerActionsApi.md#preview_environment_container) | **POST** /container/{containerId}/previewEnvironment | NOT YET IMPLEMENTED - Deploy a preview environment with your container application
[**restart_container**](ContainerActionsApi.md#restart_container) | **POST** /container/{containerId}/restart | NOT YET IMPLEMENTED - Restart container
[**stop_container**](ContainerActionsApi.md#stop_container) | **POST** /container/{containerId}/stop | NOT YET IMPLEMENTED - Stop container


# **deploy_container**
> Status deploy_container(container_id)

NOT YET IMPLEMENTED - Deploy container

You must provide a git commit id

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import container_actions_api
from qovery.model.status import Status
from qovery.model.container_deploy_request import ContainerDeployRequest
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
    api_instance = container_actions_api.ContainerActionsApi(api_client)
    container_id = "containerId_example" # str | Container ID
    container_deploy_request = ContainerDeployRequest(
        image_tag="image_tag_example",
    ) # ContainerDeployRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # NOT YET IMPLEMENTED - Deploy container
        api_response = api_instance.deploy_container(container_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainerActionsApi->deploy_container: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # NOT YET IMPLEMENTED - Deploy container
        api_response = api_instance.deploy_container(container_id, container_deploy_request=container_deploy_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainerActionsApi->deploy_container: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Container ID |
 **container_deploy_request** | [**ContainerDeployRequest**](ContainerDeployRequest.md)|  | [optional]

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
**202** | Deploy container |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Operation is in progress |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preview_environment_container**
> Status preview_environment_container(container_id)

NOT YET IMPLEMENTED - Deploy a preview environment with your container application

You must provide the image tag.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import container_actions_api
from qovery.model.status import Status
from qovery.model.container_deploy_request import ContainerDeployRequest
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
    api_instance = container_actions_api.ContainerActionsApi(api_client)
    container_id = "containerId_example" # str | Container ID
    container_deploy_request = ContainerDeployRequest(
        image_tag="image_tag_example",
    ) # ContainerDeployRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # NOT YET IMPLEMENTED - Deploy a preview environment with your container application
        api_response = api_instance.preview_environment_container(container_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainerActionsApi->preview_environment_container: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # NOT YET IMPLEMENTED - Deploy a preview environment with your container application
        api_response = api_instance.preview_environment_container(container_id, container_deploy_request=container_deploy_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainerActionsApi->preview_environment_container: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Container ID |
 **container_deploy_request** | [**ContainerDeployRequest**](ContainerDeployRequest.md)|  | [optional]

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
**202** | Deploy container |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Operation is in progress |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restart_container**
> Status restart_container(container_id)

NOT YET IMPLEMENTED - Restart container

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import container_actions_api
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
    api_instance = container_actions_api.ContainerActionsApi(api_client)
    container_id = "containerId_example" # str | Container ID

    # example passing only required values which don't have defaults set
    try:
        # NOT YET IMPLEMENTED - Restart container
        api_response = api_instance.restart_container(container_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainerActionsApi->restart_container: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Container ID |

### Return type

[**Status**](Status.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Container restart has been requested |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Operation is in progress |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_container**
> Status stop_container(container_id)

NOT YET IMPLEMENTED - Stop container

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import container_actions_api
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
    api_instance = container_actions_api.ContainerActionsApi(api_client)
    container_id = "containerId_example" # str | Container ID

    # example passing only required values which don't have defaults set
    try:
        # NOT YET IMPLEMENTED - Stop container
        api_response = api_instance.stop_container(container_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainerActionsApi->stop_container: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Container ID |

### Return type

[**Status**](Status.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Container stop has been requested |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Container is already stopped or an operation is in progress |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

