# qovery.HelmConfigurationApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edit_helm_advanced_settings**](HelmConfigurationApi.md#edit_helm_advanced_settings) | **PUT** /helm/{helmId}/advancedSettings | Edit advanced settings
[**get_helm_advanced_settings**](HelmConfigurationApi.md#get_helm_advanced_settings) | **GET** /helm/{helmId}/advancedSettings | Get advanced settings


# **edit_helm_advanced_settings**
> HelmAdvancedSettings edit_helm_advanced_settings(helm_id, helm_advanced_settings=helm_advanced_settings)

Edit advanced settings

Edit advanced settings by returning table of advanced settings.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import os
import qovery
from qovery.models.helm_advanced_settings import HelmAdvancedSettings
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
    api_instance = qovery.HelmConfigurationApi(api_client)
    helm_id = 'helm_id_example' # str | Helm ID
    helm_advanced_settings = qovery.HelmAdvancedSettings() # HelmAdvancedSettings |  (optional)

    try:
        # Edit advanced settings
        api_response = api_instance.edit_helm_advanced_settings(helm_id, helm_advanced_settings=helm_advanced_settings)
        print("The response of HelmConfigurationApi->edit_helm_advanced_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HelmConfigurationApi->edit_helm_advanced_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **helm_id** | **str**| Helm ID | 
 **helm_advanced_settings** | [**HelmAdvancedSettings**](HelmAdvancedSettings.md)|  | [optional] 

### Return type

[**HelmAdvancedSettings**](HelmAdvancedSettings.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Updated advanced settings |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_helm_advanced_settings**
> HelmAdvancedSettings get_helm_advanced_settings(helm_id)

Get advanced settings

Get list and values of the advanced settings of the helm.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import os
import qovery
from qovery.models.helm_advanced_settings import HelmAdvancedSettings
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
    api_instance = qovery.HelmConfigurationApi(api_client)
    helm_id = 'helm_id_example' # str | Helm ID

    try:
        # Get advanced settings
        api_response = api_instance.get_helm_advanced_settings(helm_id)
        print("The response of HelmConfigurationApi->get_helm_advanced_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HelmConfigurationApi->get_helm_advanced_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **helm_id** | **str**| Helm ID | 

### Return type

[**HelmAdvancedSettings**](HelmAdvancedSettings.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Advanced settings list |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

