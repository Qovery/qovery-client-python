# qovery.HelmDeploymentHistoryApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_helm_deployment_history**](HelmDeploymentHistoryApi.md#list_helm_deployment_history) | **GET** /helm/{helmId}/deploymentHistory | List helm deployments


# **list_helm_deployment_history**
> ListHelmDeploymentHistory200Response list_helm_deployment_history(helm_id)

List helm deployments

Returns the 20 last helm deployments

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import helm_deployment_history_api
from qovery.model.list_helm_deployment_history200_response import ListHelmDeploymentHistory200Response
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
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = qovery.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with qovery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = helm_deployment_history_api.HelmDeploymentHistoryApi(api_client)
    helm_id = "helmId_example" # str | Helm ID

    # example passing only required values which don't have defaults set
    try:
        # List helm deployments
        api_response = api_instance.list_helm_deployment_history(helm_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling HelmDeploymentHistoryApi->list_helm_deployment_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **helm_id** | **str**| Helm ID |

### Return type

[**ListHelmDeploymentHistory200Response**](ListHelmDeploymentHistory200Response.md)

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

