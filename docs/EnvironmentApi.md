# qovery.EnvironmentApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deploy_all_applications**](EnvironmentApi.md#deploy_all_applications) | **POST** /environment/{environmentId}/application/deploy | Deploy applications


# **deploy_all_applications**
> Status deploy_all_applications(environment_id, deploy_all_request=deploy_all_request)

Deploy applications

Start a deployment of the environment. Any of the services within the chosen environment based on the following rule: a service is deployed only if a new version is specified in the payload for that application/container or if there was a change in its configuration that needs to be applied (vCPU,RAM etc..)

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import os
import qovery
from qovery.models.deploy_all_request import DeployAllRequest
from qovery.models.status import Status
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
    api_instance = qovery.EnvironmentApi(api_client)
    environment_id = 'environment_id_example' # str | Environment ID
    deploy_all_request = qovery.DeployAllRequest() # DeployAllRequest |  (optional)

    try:
        # Deploy applications
        api_response = api_instance.deploy_all_applications(environment_id, deploy_all_request=deploy_all_request)
        print("The response of EnvironmentApi->deploy_all_applications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentApi->deploy_all_applications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID | 
 **deploy_all_request** | [**DeployAllRequest**](DeployAllRequest.md)|  | [optional] 

### Return type

[**Status**](Status.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Deployed applications |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Operation is in progress |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

