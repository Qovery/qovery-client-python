# qovery.DatabasesApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_database**](DatabasesApi.md#create_database) | **POST** /environment/{environmentId}/database | Create a database
[**get_environment_database_status**](DatabasesApi.md#get_environment_database_status) | **GET** /environment/{environmentId}/database/status | List all environment databases statuses
[**list_database**](DatabasesApi.md#list_database) | **GET** /environment/{environmentId}/database | List environment databases
[**list_environment_database_config**](DatabasesApi.md#list_environment_database_config) | **GET** /environment/{environmentId}/databaseConfiguration | List eligible database types, versions and modes for the environment
[**list_environment_database_current_metric**](DatabasesApi.md#list_environment_database_current_metric) | **GET** /environment/{environmentId}/database/currentMetric | List current metric consumption for each database


# **create_database**
> DatabaseResponse create_database(environment_id)

Create a database

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from api import databases_api
from qovery.model.database_request import DatabaseRequest
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
    api_instance = databases_api.DatabasesApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID
    database_request = DatabaseRequest(
        name="name_example",
        type="POSTGRESQL",
        version="10.1",
        mode="MANAGED",
        accessibility="PRIVATE",
        cpu=1250,
        memory=1024,
        storage=10240,
    ) # DatabaseRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a database
        api_response = api_instance.create_database(environment_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling DatabasesApi->create_database: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a database
        api_response = api_instance.create_database(environment_id, database_request=database_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling DatabasesApi->create_database: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID |
 **database_request** | [**DatabaseRequest**](DatabaseRequest.md)|  | [optional]

### Return type

[**DatabaseResponse**](DatabaseResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create database  |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Database name within the environment is already taken |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_environment_database_status**
> ReferenceObjectStatusResponseList get_environment_database_status(environment_id)

List all environment databases statuses

Returns a list of databases with only their id and status.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from api import databases_api
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
    api_instance = databases_api.DatabasesApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID

    # example passing only required values which don't have defaults set
    try:
        # List all environment databases statuses
        api_response = api_instance.get_environment_database_status(environment_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling DatabasesApi->get_environment_database_status: %s\n" % e)
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

# **list_database**
> DatabaseResponseList list_database(environment_id)

List environment databases

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from api import databases_api
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
    api_instance = databases_api.DatabasesApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID

    # example passing only required values which don't have defaults set
    try:
        # List environment databases
        api_response = api_instance.list_database(environment_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling DatabasesApi->list_database: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID |

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
**200** | List databases |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_environment_database_config**
> DatabaseConfigurationResponseList list_environment_database_config(environment_id)

List eligible database types, versions and modes for the environment

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from api import databases_api
from qovery.model.database_configuration_response_list import DatabaseConfigurationResponseList
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
    api_instance = databases_api.DatabasesApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID

    # example passing only required values which don't have defaults set
    try:
        # List eligible database types, versions and modes for the environment
        api_response = api_instance.list_environment_database_config(environment_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling DatabasesApi->list_environment_database_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID |

### Return type

[**DatabaseConfigurationResponseList**](DatabaseConfigurationResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List eligible database |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_environment_database_current_metric**
> EnvironmentDatabasesCurrentMetricResponseList list_environment_database_current_metric(environment_id)

List current metric consumption for each database

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from api import databases_api
from qovery.model.environment_databases_current_metric_response_list import EnvironmentDatabasesCurrentMetricResponseList
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
    api_instance = databases_api.DatabasesApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID

    # example passing only required values which don't have defaults set
    try:
        # List current metric consumption for each database
        api_response = api_instance.list_environment_database_current_metric(environment_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling DatabasesApi->list_environment_database_current_metric: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID |

### Return type

[**EnvironmentDatabasesCurrentMetricResponseList**](EnvironmentDatabasesCurrentMetricResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List current metric for each database |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

