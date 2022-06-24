# qovery.DatabaseDeploymentHistoryApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_database_deployment_history**](DatabaseDeploymentHistoryApi.md#list_database_deployment_history) | **GET** /database/{databaseId}/deploymentHistory | List database deploys


# **list_database_deployment_history**
> ListDatabaseDeploymentHistory200Response list_database_deployment_history(database_id)

List database deploys

By default it returns the 20 last results. The response is paginated.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import database_deployment_history_api
from qovery.model.list_database_deployment_history200_response import ListDatabaseDeploymentHistory200Response
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
    api_instance = database_deployment_history_api.DatabaseDeploymentHistoryApi(api_client)
    database_id = "databaseId_example" # str | Database ID

    # example passing only required values which don't have defaults set
    try:
        # List database deploys
        api_response = api_instance.list_database_deployment_history(database_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling DatabaseDeploymentHistoryApi->list_database_deployment_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_id** | **str**| Database ID |

### Return type

[**ListDatabaseDeploymentHistory200Response**](ListDatabaseDeploymentHistory200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List deployment history |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

