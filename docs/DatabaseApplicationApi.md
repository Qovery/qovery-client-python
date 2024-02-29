# qovery.DatabaseApplicationApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_database_application**](DatabaseApplicationApi.md#list_database_application) | **GET** /database/{databaseId}/application | List applications using the database
[**remove_application_from_database**](DatabaseApplicationApi.md#remove_application_from_database) | **DELETE** /database/{databaseId}/application/{targetApplicationId} | Remove an application from this database 


# **list_database_application**
> ApplicationResponseList list_database_application(database_id)

List applications using the database

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import qovery
from qovery.models.application_response_list import ApplicationResponseList
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
    api_instance = qovery.DatabaseApplicationApi(api_client)
    database_id = 'database_id_example' # str | Database ID

    try:
        # List applications using the database
        api_response = api_instance.list_database_application(database_id)
        print("The response of DatabaseApplicationApi->list_database_application:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabaseApplicationApi->list_database_application: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_id** | **str**| Database ID | 

### Return type

[**ApplicationResponseList**](ApplicationResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

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

# **remove_application_from_database**
> remove_application_from_database(database_id, target_application_id)

Remove an application from this database 

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
    api_instance = qovery.DatabaseApplicationApi(api_client)
    database_id = 'database_id_example' # str | Database ID
    target_application_id = 'target_application_id_example' # str | Target application ID

    try:
        # Remove an application from this database 
        api_instance.remove_application_from_database(database_id, target_application_id)
    except Exception as e:
        print("Exception when calling DatabaseApplicationApi->remove_application_from_database: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_id** | **str**| Database ID | 
 **target_application_id** | **str**| Target application ID | 

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
**204** | no content |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

