# qovery.DatabaseMainCallsApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_database**](DatabaseMainCallsApi.md#delete_database) | **DELETE** /database/{databaseId} | Delete a database 
[**edit_database**](DatabaseMainCallsApi.md#edit_database) | **PUT** /database/{databaseId} | Edit a database 
[**edit_database_credentials**](DatabaseMainCallsApi.md#edit_database_credentials) | **PUT** /database/{databaseId}/masterCredentials | Edit database  master credentials
[**get_database**](DatabaseMainCallsApi.md#get_database) | **GET** /database/{databaseId} | Get database by ID
[**get_database_master_credentials**](DatabaseMainCallsApi.md#get_database_master_credentials) | **GET** /database/{databaseId}/masterCredentials | Get master credentials of the database
[**get_database_status**](DatabaseMainCallsApi.md#get_database_status) | **GET** /database/{databaseId}/status | Get database status
[**list_database_version**](DatabaseMainCallsApi.md#list_database_version) | **GET** /database/{databaseId}/version | List eligible versions for the database


# **delete_database**
> delete_database(database_id)

Delete a database 

To delete a database you must have the admin permission

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from api import database_main_calls_api
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
    api_instance = database_main_calls_api.DatabaseMainCallsApi(api_client)
    database_id = "databaseId_example" # str | Database ID

    # example passing only required values which don't have defaults set
    try:
        # Delete a database 
        api_instance.delete_database(database_id)
    except qovery.ApiException as e:
        print("Exception when calling DatabaseMainCallsApi->delete_database: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_id** | **str**| Database ID |

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

# **edit_database**
> DatabaseResponse edit_database(database_id)

Edit a database 

To edit a database  you must have the admin permission

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from api import database_main_calls_api
from qovery.model.database_edit_request import DatabaseEditRequest
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
    api_instance = database_main_calls_api.DatabaseMainCallsApi(api_client)
    database_id = "databaseId_example" # str | Database ID
    database_edit_request = DatabaseEditRequest(
        name="name_example",
        version="10.1",
        accessibility="PUBLIC",
        cpu=1250,
        memory=1024,
        storage=4,
    ) # DatabaseEditRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Edit a database 
        api_response = api_instance.edit_database(database_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling DatabaseMainCallsApi->edit_database: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit a database 
        api_response = api_instance.edit_database(database_id, database_edit_request=database_edit_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling DatabaseMainCallsApi->edit_database: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_id** | **str**| Database ID |
 **database_edit_request** | [**DatabaseEditRequest**](DatabaseEditRequest.md)|  | [optional]

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
**200** | Edit a database  |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Database  name within the environment is already taken |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_database_credentials**
> CredentialsResponse edit_database_credentials(database_id)

Edit database  master credentials

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from api import database_main_calls_api
from qovery.model.credentials_response import CredentialsResponse
from qovery.model.credentials_request import CredentialsRequest
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
    api_instance = database_main_calls_api.DatabaseMainCallsApi(api_client)
    database_id = "databaseId_example" # str | Database ID
    credentials_request = CredentialsRequest(
        login="login_example",
        password="password_example",
    ) # CredentialsRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Edit database  master credentials
        api_response = api_instance.edit_database_credentials(database_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling DatabaseMainCallsApi->edit_database_credentials: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit database  master credentials
        api_response = api_instance.edit_database_credentials(database_id, credentials_request=credentials_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling DatabaseMainCallsApi->edit_database_credentials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_id** | **str**| Database ID |
 **credentials_request** | [**CredentialsRequest**](CredentialsRequest.md)|  | [optional]

### Return type

[**CredentialsResponse**](CredentialsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Edit database credentials |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_database**
> DatabaseResponse get_database(database_id)

Get database by ID

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from api import database_main_calls_api
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
    api_instance = database_main_calls_api.DatabaseMainCallsApi(api_client)
    database_id = "databaseId_example" # str | Database ID

    # example passing only required values which don't have defaults set
    try:
        # Get database by ID
        api_response = api_instance.get_database(database_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling DatabaseMainCallsApi->get_database: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_id** | **str**| Database ID |

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
**200** | Get database  by ID |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_database_master_credentials**
> CredentialsResponse get_database_master_credentials(database_id)

Get master credentials of the database

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from api import database_main_calls_api
from qovery.model.credentials_response import CredentialsResponse
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
    api_instance = database_main_calls_api.DatabaseMainCallsApi(api_client)
    database_id = "databaseId_example" # str | Database ID

    # example passing only required values which don't have defaults set
    try:
        # Get master credentials of the database
        api_response = api_instance.get_database_master_credentials(database_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling DatabaseMainCallsApi->get_database_master_credentials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_id** | **str**| Database ID |

### Return type

[**CredentialsResponse**](CredentialsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | get credentials |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_database_status**
> Status get_database_status(database_id)

Get database status

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from api import database_main_calls_api
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
    api_instance = database_main_calls_api.DatabaseMainCallsApi(api_client)
    database_id = "databaseId_example" # str | Database ID

    # example passing only required values which don't have defaults set
    try:
        # Get database status
        api_response = api_instance.get_database_status(database_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling DatabaseMainCallsApi->get_database_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_id** | **str**| Database ID |

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
**200** | Get status |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_database_version**
> VersionResponseList list_database_version(database_id)

List eligible versions for the database

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from api import database_main_calls_api
from qovery.model.version_response_list import VersionResponseList
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
    api_instance = database_main_calls_api.DatabaseMainCallsApi(api_client)
    database_id = "databaseId_example" # str | Database ID

    # example passing only required values which don't have defaults set
    try:
        # List eligible versions for the database
        api_response = api_instance.list_database_version(database_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling DatabaseMainCallsApi->list_database_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_id** | **str**| Database ID |

### Return type

[**VersionResponseList**](VersionResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List eligible versions |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

