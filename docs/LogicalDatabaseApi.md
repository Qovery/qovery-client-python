# qovery.LogicalDatabaseApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_logical_database_on_database**](LogicalDatabaseApi.md#create_logical_database_on_database) | **POST** /database/{databaseId}/logicalDatabase | Create a logical database on the database
[**delete_logical_database**](LogicalDatabaseApi.md#delete_logical_database) | **DELETE** /logicalDatabase/{logicalDatabaseId} | Delete a Logical database
[**edit_logical_database**](LogicalDatabaseApi.md#edit_logical_database) | **PUT** /logicalDatabase/{logicalDatabaseId} | Edit a logical database
[**edit_logical_database_credentials**](LogicalDatabaseApi.md#edit_logical_database_credentials) | **PUT** /logicalDatabase/{logicalDatabaseId}/credentials | Edit logical database credentials
[**get_logical_database**](LogicalDatabaseApi.md#get_logical_database) | **GET** /logicalDatabase/{logicalDatabaseId} | Get logical database by ID
[**get_logical_database_credentials**](LogicalDatabaseApi.md#get_logical_database_credentials) | **GET** /logicalDatabase/{logicalDatabaseId}/credentials | Get  credentials of the logical database
[**list_logical_database_application**](LogicalDatabaseApi.md#list_logical_database_application) | **GET** /logicalDatabase/{logicalDatabaseId}/application | List linked applications
[**list_logical_database_database**](LogicalDatabaseApi.md#list_logical_database_database) | **GET** /database/{databaseId}/logicalDatabase | List logical databases of a database


# **create_logical_database_on_database**
> LogicalDatabase create_logical_database_on_database(database_id)

Create a logical database on the database

If you don't specify credentials, Qovery will autogenerate them.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import logical_database_api
from qovery.model.logical_database_request import LogicalDatabaseRequest
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
    api_instance = logical_database_api.LogicalDatabaseApi(api_client)
    database_id = "databaseId_example" # str | Database ID
    logical_database_request = LogicalDatabaseRequest(
        name="name_example",
        description="description_example",
    ) # LogicalDatabaseRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a logical database on the database
        api_response = api_instance.create_logical_database_on_database(database_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling LogicalDatabaseApi->create_logical_database_on_database: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a logical database on the database
        api_response = api_instance.create_logical_database_on_database(database_id, logical_database_request=logical_database_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling LogicalDatabaseApi->create_logical_database_on_database: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_id** | **str**| Database ID |
 **logical_database_request** | [**LogicalDatabaseRequest**](LogicalDatabaseRequest.md)|  | [optional]

### Return type

[**LogicalDatabase**](LogicalDatabase.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created database on the database |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Logical Database with this name already exists on the database |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_logical_database**
> delete_logical_database(logical_database_id)

Delete a Logical database

To delete a logical database you must have the project user permission

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import logical_database_api
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
    api_instance = logical_database_api.LogicalDatabaseApi(api_client)
    logical_database_id = "logicalDatabaseId_example" # str | Logical Database ID

    # example passing only required values which don't have defaults set
    try:
        # Delete a Logical database
        api_instance.delete_logical_database(logical_database_id)
    except qovery.ApiException as e:
        print("Exception when calling LogicalDatabaseApi->delete_logical_database: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_database_id** | **str**| Logical Database ID |

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

# **edit_logical_database**
> LogicalDatabase edit_logical_database(logical_database_id)

Edit a logical database

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import logical_database_api
from qovery.model.logical_database_request import LogicalDatabaseRequest
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
    api_instance = logical_database_api.LogicalDatabaseApi(api_client)
    logical_database_id = "logicalDatabaseId_example" # str | Logical Database ID
    logical_database_request = LogicalDatabaseRequest(
        name="name_example",
        description="description_example",
    ) # LogicalDatabaseRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Edit a logical database
        api_response = api_instance.edit_logical_database(logical_database_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling LogicalDatabaseApi->edit_logical_database: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit a logical database
        api_response = api_instance.edit_logical_database(logical_database_id, logical_database_request=logical_database_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling LogicalDatabaseApi->edit_logical_database: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_database_id** | **str**| Logical Database ID |
 **logical_database_request** | [**LogicalDatabaseRequest**](LogicalDatabaseRequest.md)|  | [optional]

### Return type

[**LogicalDatabase**](LogicalDatabase.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Edit a Logical Database |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_logical_database_credentials**
> Credentials edit_logical_database_credentials(logical_database_id)

Edit logical database credentials

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import logical_database_api
from qovery.model.credentials import Credentials
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
    api_instance = logical_database_api.LogicalDatabaseApi(api_client)
    logical_database_id = "logicalDatabaseId_example" # str | Logical Database ID
    credentials_request = CredentialsRequest(
        login="login_example",
        password="password_example",
    ) # CredentialsRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Edit logical database credentials
        api_response = api_instance.edit_logical_database_credentials(logical_database_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling LogicalDatabaseApi->edit_logical_database_credentials: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit logical database credentials
        api_response = api_instance.edit_logical_database_credentials(logical_database_id, credentials_request=credentials_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling LogicalDatabaseApi->edit_logical_database_credentials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_database_id** | **str**| Logical Database ID |
 **credentials_request** | [**CredentialsRequest**](CredentialsRequest.md)|  | [optional]

### Return type

[**Credentials**](Credentials.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Edit logical database credentials |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logical_database**
> LogicalDatabase get_logical_database(logical_database_id)

Get logical database by ID

A logical database exists inside a database. The database is a service that exists within an environment, that you can deploy, and that has allocated resources. A database can have several logical databases

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import logical_database_api
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
    api_instance = logical_database_api.LogicalDatabaseApi(api_client)
    logical_database_id = "logicalDatabaseId_example" # str | Logical Database ID

    # example passing only required values which don't have defaults set
    try:
        # Get logical database by ID
        api_response = api_instance.get_logical_database(logical_database_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling LogicalDatabaseApi->get_logical_database: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_database_id** | **str**| Logical Database ID |

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
**200** | Get logical database by ID |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logical_database_credentials**
> Credentials get_logical_database_credentials(logical_database_id)

Get  credentials of the logical database

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import logical_database_api
from qovery.model.credentials import Credentials
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
    api_instance = logical_database_api.LogicalDatabaseApi(api_client)
    logical_database_id = "logicalDatabaseId_example" # str | Logical Database ID

    # example passing only required values which don't have defaults set
    try:
        # Get  credentials of the logical database
        api_response = api_instance.get_logical_database_credentials(logical_database_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling LogicalDatabaseApi->get_logical_database_credentials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_database_id** | **str**| Logical Database ID |

### Return type

[**Credentials**](Credentials.md)

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

# **list_logical_database_application**
> ApplicationResponseList list_logical_database_application(logical_database_id)

List linked applications

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import logical_database_api
from qovery.model.application_response_list import ApplicationResponseList
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
    api_instance = logical_database_api.LogicalDatabaseApi(api_client)
    logical_database_id = "logicalDatabaseId_example" # str | Logical Database ID

    # example passing only required values which don't have defaults set
    try:
        # List linked applications
        api_response = api_instance.list_logical_database_application(logical_database_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling LogicalDatabaseApi->list_logical_database_application: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_database_id** | **str**| Logical Database ID |

### Return type

[**ApplicationResponseList**](ApplicationResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List linked applications |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_logical_database_database**
> LogicalDatabaseResponseList list_logical_database_database(database_id)

List logical databases of a database

A logical database exists inside a database. The database is a service that exists within an environment, that you can deploy, and that has allocated resources. A database can have several logical databases

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import logical_database_api
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
    api_instance = logical_database_api.LogicalDatabaseApi(api_client)
    database_id = "databaseId_example" # str | Database ID

    # example passing only required values which don't have defaults set
    try:
        # List logical databases of a database
        api_response = api_instance.list_logical_database_database(database_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling LogicalDatabaseApi->list_logical_database_database: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_id** | **str**| Database ID |

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
**200** | List logical databases |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

