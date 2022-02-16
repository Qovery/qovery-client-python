# qovery.ApplicationDatabaseApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_databaseto_application**](ApplicationDatabaseApi.md#attach_databaseto_application) | **POST** /application/{applicationId}/database/{targetDatabaseId} | Link a database to the application
[**attach_logical_databaseto_application**](ApplicationDatabaseApi.md#attach_logical_databaseto_application) | **POST** /application/{applicationId}/logicalDatabase/{targetLogicalDatabaseId} | Link a logical database to the application
[**list_application_database**](ApplicationDatabaseApi.md#list_application_database) | **GET** /application/{applicationId}/database | List linked databases
[**list_application_logical_database**](ApplicationDatabaseApi.md#list_application_logical_database) | **GET** /application/{applicationId}/logicalDatabase | List linked logical databases
[**remove_database_from_application**](ApplicationDatabaseApi.md#remove_database_from_application) | **DELETE** /application/{applicationId}/database/{targetDatabaseId} | Remove database link to this application.
[**remove_logical_database_from_application**](ApplicationDatabaseApi.md#remove_logical_database_from_application) | **DELETE** /application/{applicationId}/logicalDatabase/{targetLogicalDatabaseId} | Remove logical database link to this application.


# **attach_databaseto_application**
> DatabaseResponse attach_databaseto_application(application_id, target_database_id)

Link a database to the application

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from api import application_database_api
from qovery.model.database_response import DatabaseResponse
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
    api_instance = application_database_api.ApplicationDatabaseApi(api_client)
    application_id = "applicationId_example" # str | Application ID
    target_database_id = "targetDatabaseId_example" # str | Target database ID

    # example passing only required values which don't have defaults set
    try:
        # Link a database to the application
        api_response = api_instance.attach_databaseto_application(application_id, target_database_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationDatabaseApi->attach_databaseto_application: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID |
 **target_database_id** | **str**| Target database ID |

### Return type

[**DatabaseResponse**](DatabaseResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Linked the database to the application |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | This database is already linked to the application |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_logical_databaseto_application**
> LogicalDatabaseResponse attach_logical_databaseto_application(application_id, target_logical_database_id)

Link a logical database to the application

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from api import application_database_api
from qovery.model.logical_database_response import LogicalDatabaseResponse
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
    api_instance = application_database_api.ApplicationDatabaseApi(api_client)
    application_id = "applicationId_example" # str | Application ID
    target_logical_database_id = "targetLogicalDatabaseId_example" # str | Target database ID

    # example passing only required values which don't have defaults set
    try:
        # Link a logical database to the application
        api_response = api_instance.attach_logical_databaseto_application(application_id, target_logical_database_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationDatabaseApi->attach_logical_databaseto_application: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID |
 **target_logical_database_id** | **str**| Target database ID |

### Return type

[**LogicalDatabaseResponse**](LogicalDatabaseResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Linked the Logical database to the application |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | This logical database is already linked to the application |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_application_database**
> DatabaseResponseList list_application_database(application_id)

List linked databases

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from api import application_database_api
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
    api_instance = application_database_api.ApplicationDatabaseApi(api_client)
    application_id = "applicationId_example" # str | Application ID

    # example passing only required values which don't have defaults set
    try:
        # List linked databases
        api_response = api_instance.list_application_database(application_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationDatabaseApi->list_application_database: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID |

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

# **list_application_logical_database**
> LogicalDatabaseResponseList list_application_logical_database(application_id)

List linked logical databases

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from api import application_database_api
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
    api_instance = application_database_api.ApplicationDatabaseApi(api_client)
    application_id = "applicationId_example" # str | Application ID

    # example passing only required values which don't have defaults set
    try:
        # List linked logical databases
        api_response = api_instance.list_application_logical_database(application_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationDatabaseApi->list_application_logical_database: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID |

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

# **remove_database_from_application**
> remove_database_from_application(application_id, target_database_id)

Remove database link to this application.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from api import application_database_api
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
    api_instance = application_database_api.ApplicationDatabaseApi(api_client)
    application_id = "applicationId_example" # str | Application ID
    target_database_id = "targetDatabaseId_example" # str | Target database ID

    # example passing only required values which don't have defaults set
    try:
        # Remove database link to this application.
        api_instance.remove_database_from_application(application_id, target_database_id)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationDatabaseApi->remove_database_from_application: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID |
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

# **remove_logical_database_from_application**
> remove_logical_database_from_application(application_id, target_logical_database_id)

Remove logical database link to this application.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from api import application_database_api
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
    api_instance = application_database_api.ApplicationDatabaseApi(api_client)
    application_id = "applicationId_example" # str | Application ID
    target_logical_database_id = "targetLogicalDatabaseId_example" # str | Target database ID

    # example passing only required values which don't have defaults set
    try:
        # Remove logical database link to this application.
        api_instance.remove_logical_database_from_application(application_id, target_logical_database_id)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationDatabaseApi->remove_logical_database_from_application: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID |
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

