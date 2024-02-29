# qovery.ContainerMainCallsApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_container**](ContainerMainCallsApi.md#delete_container) | **DELETE** /container/{containerId} | Delete container
[**edit_container**](ContainerMainCallsApi.md#edit_container) | **PUT** /container/{containerId} | Edit container
[**get_container**](ContainerMainCallsApi.md#get_container) | **GET** /container/{containerId} | Get container by ID
[**get_container_status**](ContainerMainCallsApi.md#get_container_status) | **GET** /container/{containerId}/status | Get container status
[**list_container_links**](ContainerMainCallsApi.md#list_container_links) | **GET** /container/{containerId}/link | List all URLs of the container


# **delete_container**
> delete_container(container_id)

Delete container

To delete the container you must have the admin permission

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
    api_instance = qovery.ContainerMainCallsApi(api_client)
    container_id = 'container_id_example' # str | Container ID

    try:
        # Delete container
        api_instance.delete_container(container_id)
    except Exception as e:
        print("Exception when calling ContainerMainCallsApi->delete_container: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Container ID | 

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

# **edit_container**
> ContainerResponse edit_container(container_id, container_request=container_request)

Edit container

- To edit the container you must have the admin permission. - For port edition, if you provide a port id, we will update the corresponding port. If you don't we will create a new one. If you remove a port from the payload, we will delete it. - For storage edition, if you provide a storage id, we will update the corresponding storage. If you don't we will create a new one. If you remove a storage from the payload, we will delete it. 

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
    api_instance = qovery.ContainerMainCallsApi(api_client)
    container_id = 'container_id_example' # str | Container ID
    container_request = qovery.ContainerRequest() # ContainerRequest |  (optional)

    try:
        # Edit container
        api_response = api_instance.edit_container(container_id, container_request=container_request)
        print("The response of ContainerMainCallsApi->edit_container:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainerMainCallsApi->edit_container: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Container ID | 
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
**200** | Edit container |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Container name within the environment is already taken |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_container**
> ContainerResponse get_container(container_id)

Get container by ID

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import qovery
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
    api_instance = qovery.ContainerMainCallsApi(api_client)
    container_id = 'container_id_example' # str | Container ID

    try:
        # Get container by ID
        api_response = api_instance.get_container(container_id)
        print("The response of ContainerMainCallsApi->get_container:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainerMainCallsApi->get_container: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Container ID | 

### Return type

[**ContainerResponse**](ContainerResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get container by ID |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_container_status**
> Status get_container_status(container_id)

Get container status

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
    api_instance = qovery.ContainerMainCallsApi(api_client)
    container_id = 'container_id_example' # str | Container ID

    try:
        # Get container status
        api_response = api_instance.get_container_status(container_id)
        print("The response of ContainerMainCallsApi->get_container_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainerMainCallsApi->get_container_status: %s\n" % e)
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
**200** | Get status |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_container_links**
> LinkResponseList list_container_links(container_id)

List all URLs of the container

This will return all the custom domains and Qovery autogenerated domain for the given container

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import qovery
from qovery.models.link_response_list import LinkResponseList
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
    api_instance = qovery.ContainerMainCallsApi(api_client)
    container_id = 'container_id_example' # str | Container ID

    try:
        # List all URLs of the container
        api_response = api_instance.list_container_links(container_id)
        print("The response of ContainerMainCallsApi->list_container_links:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainerMainCallsApi->list_container_links: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Container ID | 

### Return type

[**LinkResponseList**](LinkResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List links |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

