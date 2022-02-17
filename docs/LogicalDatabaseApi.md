# qovery.LogicalDatabaseApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edit_logical_database_credentials**](LogicalDatabaseApi.md#edit_logical_database_credentials) | **PUT** /logicalDatabase/{logicalDatabaseId}/credentials | Edit logical database credentials


# **edit_logical_database_credentials**
> CredentialsResponse edit_logical_database_credentials(logical_database_id)

Edit logical database credentials

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import logical_database_api
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

[**CredentialsResponse**](CredentialsResponse.md)

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

