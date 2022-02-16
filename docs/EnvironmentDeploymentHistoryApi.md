# qovery.EnvironmentDeploymentHistoryApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_environment_deployment_history**](EnvironmentDeploymentHistoryApi.md#list_environment_deployment_history) | **GET** /environment/{environmentId}/deploymentHistory | List environment deployments


# **list_environment_deployment_history**
> DeploymentHistoryEnvironmentPaginatedResponseList list_environment_deployment_history(environment_id)

List environment deployments

List previous and current environment deployments with the status deployment and the related services. By default it returns the 20 last results. The response is paginated. In order to request the next page, you can use the startId query parameter

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from api import environment_deployment_history_api
from qovery.model.deployment_history_environment_paginated_response_list import DeploymentHistoryEnvironmentPaginatedResponseList
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
    api_instance = environment_deployment_history_api.EnvironmentDeploymentHistoryApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID
    start_id = "startId_example" # str | Starting point after which to return results (optional)

    # example passing only required values which don't have defaults set
    try:
        # List environment deployments
        api_response = api_instance.list_environment_deployment_history(environment_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling EnvironmentDeploymentHistoryApi->list_environment_deployment_history: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List environment deployments
        api_response = api_instance.list_environment_deployment_history(environment_id, start_id=start_id)
        pprint(api_response)
    except qovery.ApiException as e:
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

