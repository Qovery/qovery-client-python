# qovery.HelmDeploymentRestrictionApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_helm_deployment_restriction**](HelmDeploymentRestrictionApi.md#create_helm_deployment_restriction) | **POST** /helm/{helmId}/deploymentRestriction | Create a helm deployment restriction
[**delete_helm_deployment_restriction**](HelmDeploymentRestrictionApi.md#delete_helm_deployment_restriction) | **DELETE** /helm/{helmId}/deploymentRestriction/{deploymentRestrictionId} | Delete a helm deployment restriction
[**edit_helm_deployment_restriction**](HelmDeploymentRestrictionApi.md#edit_helm_deployment_restriction) | **PUT** /helm/{helmId}/deploymentRestriction/{deploymentRestrictionId} | Edit a helm deployment restriction
[**get_helm_deployment_restrictions**](HelmDeploymentRestrictionApi.md#get_helm_deployment_restrictions) | **GET** /helm/{helmId}/deploymentRestriction | Get helm deployment restrictions


# **create_helm_deployment_restriction**
> HelmDeploymentRestrictionResponse create_helm_deployment_restriction(helm_id, helm_deployment_restriction_request=helm_deployment_restriction_request)

Create a helm deployment restriction

Create a helm deployment restriction

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import os
import qovery
from qovery.models.helm_deployment_restriction_request import HelmDeploymentRestrictionRequest
from qovery.models.helm_deployment_restriction_response import HelmDeploymentRestrictionResponse
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
    api_instance = qovery.HelmDeploymentRestrictionApi(api_client)
    helm_id = 'helm_id_example' # str | Helm ID
    helm_deployment_restriction_request = qovery.HelmDeploymentRestrictionRequest() # HelmDeploymentRestrictionRequest |  (optional)

    try:
        # Create a helm deployment restriction
        api_response = api_instance.create_helm_deployment_restriction(helm_id, helm_deployment_restriction_request=helm_deployment_restriction_request)
        print("The response of HelmDeploymentRestrictionApi->create_helm_deployment_restriction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HelmDeploymentRestrictionApi->create_helm_deployment_restriction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **helm_id** | **str**| Helm ID | 
 **helm_deployment_restriction_request** | [**HelmDeploymentRestrictionRequest**](HelmDeploymentRestrictionRequest.md)|  | [optional] 

### Return type

[**HelmDeploymentRestrictionResponse**](HelmDeploymentRestrictionResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Added an helm deployment restriction |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**409** | A Helm deployment restriction with same properties already exists for this helm |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_helm_deployment_restriction**
> delete_helm_deployment_restriction(helm_id, deployment_restriction_id)

Delete a helm deployment restriction

Delete a helm deployment restriction

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
    api_instance = qovery.HelmDeploymentRestrictionApi(api_client)
    helm_id = 'helm_id_example' # str | Helm ID
    deployment_restriction_id = 'deployment_restriction_id_example' # str | Deployment Restriction ID

    try:
        # Delete a helm deployment restriction
        api_instance.delete_helm_deployment_restriction(helm_id, deployment_restriction_id)
    except Exception as e:
        print("Exception when calling HelmDeploymentRestrictionApi->delete_helm_deployment_restriction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **helm_id** | **str**| Helm ID | 
 **deployment_restriction_id** | **str**| Deployment Restriction ID | 

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
**204** | The resource was deleted successfully |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_helm_deployment_restriction**
> HelmDeploymentRestrictionResponse edit_helm_deployment_restriction(helm_id, deployment_restriction_id, helm_deployment_restriction_request=helm_deployment_restriction_request)

Edit a helm deployment restriction

Edit a helm deployment restriction

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import os
import qovery
from qovery.models.helm_deployment_restriction_request import HelmDeploymentRestrictionRequest
from qovery.models.helm_deployment_restriction_response import HelmDeploymentRestrictionResponse
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
    api_instance = qovery.HelmDeploymentRestrictionApi(api_client)
    helm_id = 'helm_id_example' # str | Helm ID
    deployment_restriction_id = 'deployment_restriction_id_example' # str | Deployment Restriction ID
    helm_deployment_restriction_request = qovery.HelmDeploymentRestrictionRequest() # HelmDeploymentRestrictionRequest |  (optional)

    try:
        # Edit a helm deployment restriction
        api_response = api_instance.edit_helm_deployment_restriction(helm_id, deployment_restriction_id, helm_deployment_restriction_request=helm_deployment_restriction_request)
        print("The response of HelmDeploymentRestrictionApi->edit_helm_deployment_restriction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HelmDeploymentRestrictionApi->edit_helm_deployment_restriction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **helm_id** | **str**| Helm ID | 
 **deployment_restriction_id** | **str**| Deployment Restriction ID | 
 **helm_deployment_restriction_request** | [**HelmDeploymentRestrictionRequest**](HelmDeploymentRestrictionRequest.md)|  | [optional] 

### Return type

[**HelmDeploymentRestrictionResponse**](HelmDeploymentRestrictionResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Edit a helm deployment restriction |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_helm_deployment_restrictions**
> HelmDeploymentRestrictionResponseList get_helm_deployment_restrictions(helm_id)

Get helm deployment restrictions

Get helm deployment restrictions

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import os
import qovery
from qovery.models.helm_deployment_restriction_response_list import HelmDeploymentRestrictionResponseList
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
    api_instance = qovery.HelmDeploymentRestrictionApi(api_client)
    helm_id = 'helm_id_example' # str | Helm ID

    try:
        # Get helm deployment restrictions
        api_response = api_instance.get_helm_deployment_restrictions(helm_id)
        print("The response of HelmDeploymentRestrictionApi->get_helm_deployment_restrictions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HelmDeploymentRestrictionApi->get_helm_deployment_restrictions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **helm_id** | **str**| Helm ID | 

### Return type

[**HelmDeploymentRestrictionResponseList**](HelmDeploymentRestrictionResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get helm deployment restrictions |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

