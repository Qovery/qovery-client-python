# qovery.ContainerActionsApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deploy_container**](ContainerActionsApi.md#deploy_container) | **POST** /container/{containerId}/deploy | Deploy container
[**reboot_container**](ContainerActionsApi.md#reboot_container) | **POST** /container/{containerId}/restart-service | Reboot container
[**restart_container**](ContainerActionsApi.md#restart_container) | **POST** /container/{containerId}/restart | Deprecated - Restart container
[**stop_container**](ContainerActionsApi.md#stop_container) | **POST** /container/{containerId}/stop | Stop container


# **deploy_container**
> Status deploy_container(container_id, container_deploy_request=container_deploy_request)

Deploy container

You must provide a git commit id

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import qovery
from qovery.models.container_deploy_request import ContainerDeployRequest
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
    api_instance = qovery.ContainerActionsApi(api_client)
    container_id = 'container_id_example' # str | Container ID
    container_deploy_request = qovery.ContainerDeployRequest() # ContainerDeployRequest |  (optional)

    try:
        # Deploy container
        api_response = api_instance.deploy_container(container_id, container_deploy_request=container_deploy_request)
        print("The response of ContainerActionsApi->deploy_container:\n")
        pprint(api_response)
    except Exception as e:
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

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

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

# **reboot_container**
> Status reboot_container(container_id)

Reboot container

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import qovery
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
    api_instance = qovery.ContainerActionsApi(api_client)
    container_id = 'container_id_example' # str | Container ID

    try:
        # Reboot container
        api_response = api_instance.reboot_container(container_id)
        print("The response of ContainerActionsApi->reboot_container:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainerActionsApi->reboot_container: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Container ID | 

### Return type

[**Status**](Status.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Container reboot has been requested |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Operation is in progress |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restart_container**
> Status restart_container(container_id)

Deprecated - Restart container

**Deprecated** - Please use the \"Redeploy container\" endpoint now

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import qovery
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
    api_instance = qovery.ContainerActionsApi(api_client)
    container_id = 'container_id_example' # str | Container ID

    try:
        # Deprecated - Restart container
        api_response = api_instance.restart_container(container_id)
        print("The response of ContainerActionsApi->restart_container:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainerActionsApi->restart_container: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Container ID | 

### Return type

[**Status**](Status.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

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

Stop container

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import qovery
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
    api_instance = qovery.ContainerActionsApi(api_client)
    container_id = 'container_id_example' # str | Container ID

    try:
        # Stop container
        api_response = api_instance.stop_container(container_id)
        print("The response of ContainerActionsApi->stop_container:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainerActionsApi->stop_container: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Container ID | 

### Return type

[**Status**](Status.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

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

