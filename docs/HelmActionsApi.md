# qovery.HelmActionsApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deploy_helm**](HelmActionsApi.md#deploy_helm) | **POST** /helm/{helmId}/deploy | Deploy helm
[**restart_helm**](HelmActionsApi.md#restart_helm) | **POST** /helm/{helmId}/restart | Deprecated - Restart helm
[**stop_helm**](HelmActionsApi.md#stop_helm) | **POST** /helm/{helmId}/stop | Stop helm


# **deploy_helm**
> Status deploy_helm(helm_id, force_event=force_event, helm_deploy_request=helm_deploy_request)

Deploy helm

You must provide a git commit id or an image tag depending on the source location of your code (git vs image repository).

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import os
import qovery
from qovery.models.helm_deploy_request import HelmDeployRequest
from qovery.models.helm_force_event import HelmForceEvent
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
    api_instance = qovery.HelmActionsApi(api_client)
    helm_id = 'helm_id_example' # str | Helm ID
    force_event = qovery.HelmForceEvent() # HelmForceEvent | When filled, it indicates the target event to be deployed.   If the concerned helm hasn't the target event provided, the helm won't be deployed.  (optional)
    helm_deploy_request = qovery.HelmDeployRequest() # HelmDeployRequest |  (optional)

    try:
        # Deploy helm
        api_response = api_instance.deploy_helm(helm_id, force_event=force_event, helm_deploy_request=helm_deploy_request)
        print("The response of HelmActionsApi->deploy_helm:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HelmActionsApi->deploy_helm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **helm_id** | **str**| Helm ID | 
 **force_event** | [**HelmForceEvent**](.md)| When filled, it indicates the target event to be deployed.   If the concerned helm hasn&#39;t the target event provided, the helm won&#39;t be deployed.  | [optional] 
 **helm_deploy_request** | [**HelmDeployRequest**](HelmDeployRequest.md)|  | [optional] 

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
**202** | Deploy helm |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Operation is in progress |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restart_helm**
> Status restart_helm(helm_id, force_event=force_event)

Deprecated - Restart helm

**Deprecated** - Please use the \"Redeploy helm\" endpoint now

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import os
import qovery
from qovery.models.helm_force_event import HelmForceEvent
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
    api_instance = qovery.HelmActionsApi(api_client)
    helm_id = 'helm_id_example' # str | Helm ID
    force_event = qovery.HelmForceEvent() # HelmForceEvent | When filled, it indicates the target event to be deployed.   If the concerned helm hasn't the target event provided, the helm won't be deployed.  (optional)

    try:
        # Deprecated - Restart helm
        api_response = api_instance.restart_helm(helm_id, force_event=force_event)
        print("The response of HelmActionsApi->restart_helm:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HelmActionsApi->restart_helm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **helm_id** | **str**| Helm ID | 
 **force_event** | [**HelmForceEvent**](.md)| When filled, it indicates the target event to be deployed.   If the concerned helm hasn&#39;t the target event provided, the helm won&#39;t be deployed.  | [optional] 

### Return type

[**Status**](Status.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Helm restart has been requested |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Operation is in progress |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_helm**
> Status stop_helm(helm_id)

Stop helm

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import os
import qovery
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
    api_instance = qovery.HelmActionsApi(api_client)
    helm_id = 'helm_id_example' # str | Helm ID

    try:
        # Stop helm
        api_response = api_instance.stop_helm(helm_id)
        print("The response of HelmActionsApi->stop_helm:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HelmActionsApi->stop_helm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **helm_id** | **str**| Helm ID | 

### Return type

[**Status**](Status.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Helm stop has been requested |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Helm is already stopped or an operation is in progress |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

