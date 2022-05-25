# qovery.ContainerDatabaseApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_database_to_container**](ContainerDatabaseApi.md#attach_database_to_container) | **POST** /container/{containerId}/database/{targetDatabaseId} | Link a database to the container
[**attach_logical_database_to_container**](ContainerDatabaseApi.md#attach_logical_database_to_container) | **POST** /container/{containerId}/logicalDatabase/{targetLogicalDatabaseId} | Link a logical database to the container
[**list_container_database**](ContainerDatabaseApi.md#list_container_database) | **GET** /container/{containerId}/database | List linked databases
[**list_container_logical_database**](ContainerDatabaseApi.md#list_container_logical_database) | **GET** /container/{containerId}/logicalDatabase | List linked logical databases
[**remove_database_from_container**](ContainerDatabaseApi.md#remove_database_from_container) | **DELETE** /container/{containerId}/database/{targetDatabaseId} | Remove database link to this container.
[**remove_logical_database_from_container**](ContainerDatabaseApi.md#remove_logical_database_from_container) | **DELETE** /container/{containerId}/logicalDatabase/{targetLogicalDatabaseId} | Remove logical database link to this container.


# **attach_database_to_container**
> Database attach_database_to_container(container_id, target_database_id)

Link a database to the container

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import container_database_api
from qovery.model.database import Database
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
    api_instance = container_database_api.ContainerDatabaseApi(api_client)
    container_id = "containerId_example" # str | Container ID
    target_database_id = "targetDatabaseId_example" # str | Target database ID

    # example passing only required values which don't have defaults set
    try:
        # Link a database to the container
        api_response = api_instance.attach_database_to_container(container_id, target_database_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainerDatabaseApi->attach_database_to_container: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Container ID |
 **target_database_id** | **str**| Target database ID |

### Return type

[**Database**](Database.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Linked the database to the container |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | This database is already linked to the container |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_logical_database_to_container**
> LogicalDatabase attach_logical_database_to_container(container_id, target_logical_database_id)

Link a logical database to the container

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import container_database_api
from qovery.model.logical_database import LogicalDatabase
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
    api_instance = container_database_api.ContainerDatabaseApi(api_client)
    container_id = "containerId_example" # str | Container ID
    target_logical_database_id = "targetLogicalDatabaseId_example" # str | Target database ID

    # example passing only required values which don't have defaults set
    try:
        # Link a logical database to the container
        api_response = api_instance.attach_logical_database_to_container(container_id, target_logical_database_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainerDatabaseApi->attach_logical_database_to_container: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Container ID |
 **target_logical_database_id** | **str**| Target database ID |

### Return type

[**LogicalDatabase**](LogicalDatabase.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Linked the logical database to the container |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | This logical database is already linked to the container |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_container_database**
> DatabaseResponseList list_container_database(container_id)

List linked databases

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import container_database_api
from qovery.model.database_response_list import DatabaseResponseList
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
    api_instance = container_database_api.ContainerDatabaseApi(api_client)
    container_id = "containerId_example" # str | Container ID

    # example passing only required values which don't have defaults set
    try:
        # List linked databases
        api_response = api_instance.list_container_database(container_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainerDatabaseApi->list_container_database: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Container ID |

### Return type

[**DatabaseResponseList**](DatabaseResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List linked databases |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_container_logical_database**
> LogicalDatabaseResponseList list_container_logical_database(container_id)

List linked logical databases

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import container_database_api
from qovery.model.logical_database_response_list import LogicalDatabaseResponseList
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
    api_instance = container_database_api.ContainerDatabaseApi(api_client)
    container_id = "containerId_example" # str | Container ID

    # example passing only required values which don't have defaults set
    try:
        # List linked logical databases
        api_response = api_instance.list_container_logical_database(container_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainerDatabaseApi->list_container_logical_database: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Container ID |

### Return type

[**LogicalDatabaseResponseList**](LogicalDatabaseResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List linked databases |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_database_from_container**
> remove_database_from_container(container_id, target_database_id)

Remove database link to this container.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import container_database_api
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
    api_instance = container_database_api.ContainerDatabaseApi(api_client)
    container_id = "containerId_example" # str | Container ID
    target_database_id = "targetDatabaseId_example" # str | Target database ID

    # example passing only required values which don't have defaults set
    try:
        # Remove database link to this container.
        api_instance.remove_database_from_container(container_id, target_database_id)
    except qovery.ApiException as e:
        print("Exception when calling ContainerDatabaseApi->remove_database_from_container: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Container ID |
 **target_database_id** | **str**| Target database ID |

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
**204** | no content |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_logical_database_from_container**
> remove_logical_database_from_container(container_id, target_logical_database_id)

Remove logical database link to this container.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import container_database_api
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
    api_instance = container_database_api.ContainerDatabaseApi(api_client)
    container_id = "containerId_example" # str | Container ID
    target_logical_database_id = "targetLogicalDatabaseId_example" # str | Target database ID

    # example passing only required values which don't have defaults set
    try:
        # Remove logical database link to this container.
        api_instance.remove_logical_database_from_container(container_id, target_logical_database_id)
    except qovery.ApiException as e:
        print("Exception when calling ContainerDatabaseApi->remove_logical_database_from_container: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Container ID |
 **target_logical_database_id** | **str**| Target database ID |

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
**204** | no content |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

