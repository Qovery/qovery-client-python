# qovery.EnvironmentDeploymentHistoryApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_environment_deployment_history**](EnvironmentDeploymentHistoryApi.md#list_environment_deployment_history) | **GET** /environment/{environmentId}/deploymentHistory | List environment deployments


# **list_environment_deployment_history**
> DeploymentHistoryEnvironmentPaginatedResponseList list_environment_deployment_history(environment_id, start_id=start_id)

List environment deployments

List previous and current environment deployments with the status deployment and the related services. By default it returns the 20 last results. The response is paginated. In order to request the next page, you can use the startId query parameter

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import qovery
from qovery.models.deployment_history_environment_paginated_response_list import DeploymentHistoryEnvironmentPaginatedResponseList
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
    api_instance = qovery.EnvironmentDeploymentHistoryApi(api_client)
    environment_id = 'environment_id_example' # str | Environment ID
    start_id = 'start_id_example' # str | Starting point after which to return results (optional)

    try:
        # List environment deployments
        api_response = api_instance.list_environment_deployment_history(environment_id, start_id=start_id)
        print("The response of EnvironmentDeploymentHistoryApi->list_environment_deployment_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentDeploymentHistoryApi->list_environment_deployment_history: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID | 
 **start_id** | **str**| Starting point after which to return results | [optional] 

### Return type

[**DeploymentHistoryEnvironmentPaginatedResponseList**](DeploymentHistoryEnvironmentPaginatedResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

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

