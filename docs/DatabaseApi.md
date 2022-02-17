# qovery.DatabaseApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_logical_database_on_database**](DatabaseApi.md#create_logical_database_on_database) | **POST** /database/{databaseId}/logicalDatabase | Create a logical database on the database


# **create_logical_database_on_database**
> LogicalDatabaseResponse create_logical_database_on_database(database_id)

Create a logical database on the database

If you don't specify credentials, Qovery will autogenerate them.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import database_api
from qovery.model.logical_database_request import LogicalDatabaseRequest
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
    api_instance = database_api.DatabaseApi(api_client)
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
        print("Exception when calling DatabaseApi->create_logical_database_on_database: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a logical database on the database
        api_response = api_instance.create_logical_database_on_database(database_id, logical_database_request=logical_database_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling DatabaseApi->create_logical_database_on_database: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_id** | **str**| Database ID |
 **logical_database_request** | [**LogicalDatabaseRequest**](LogicalDatabaseRequest.md)|  | [optional]

### Return type

[**LogicalDatabaseResponse**](LogicalDatabaseResponse.md)

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

