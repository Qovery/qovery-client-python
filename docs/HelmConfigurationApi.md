# qovery.HelmConfigurationApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edit_helm_advanced_settings**](HelmConfigurationApi.md#edit_helm_advanced_settings) | **PUT** /helm/{helmId}/advancedSettings | Edit advanced settings
[**get_helm_advanced_settings**](HelmConfigurationApi.md#get_helm_advanced_settings) | **GET** /helm/{helmId}/advancedSettings | Get advanced settings


# **edit_helm_advanced_settings**
> HelmAdvancedSettings edit_helm_advanced_settings(helm_id)

Edit advanced settings

Edit advanced settings by returning table of advanced settings.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import helm_configuration_api
from qovery.model.helm_advanced_settings import HelmAdvancedSettings
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
    api_instance = helm_configuration_api.HelmConfigurationApi(api_client)
    helm_id = "helmId_example" # str | Helm ID
    helm_advanced_settings = HelmAdvancedSettings(
        network_ingress_proxy_body_size_mb=1,
        network_ingress_enable_cors=True,
        network_ingress_cors_allow_origin="network_ingress_cors_allow_origin_example",
        network_ingress_cors_allow_methods="network_ingress_cors_allow_methods_example",
        network_ingress_cors_allow_headers="network_ingress_cors_allow_headers_example",
        network_ingress_proxy_buffer_size_kb=1,
        network_ingress_keepalive_time_seconds=1,
        network_ingress_keepalive_timeout_seconds=1,
        network_ingress_send_timeout_seconds=1,
        network_ingress_proxy_connect_timeout_seconds=1,
        network_ingress_proxy_send_timeout_seconds=1,
        network_ingress_proxy_read_timeout_seconds=1,
        network_ingress_proxy_buffering="network_ingress_proxy_buffering_example",
        network_ingress_proxy_request_buffering="network_ingress_proxy_request_buffering_example",
        network_ingress_grpc_send_timeout_seconds=1,
        network_ingress_grpc_read_timeout_seconds=1,
        network_ingress_whitelist_source_range="network_ingress_whitelist_source_range_example",
        network_ingress_denylist_source_range="network_ingress_denylist_source_range_example",
        network_ingress_extra_headers="{"X-Frame-Options":"DENY ","X-Content-Type-Options":"nosniff"}",
        network_ingress_basic_auth_env_var="network_ingress_basic_auth_env_var_example",
        network_ingress_enable_sticky_session=True,
    ) # HelmAdvancedSettings |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Edit advanced settings
        api_response = api_instance.edit_helm_advanced_settings(helm_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling HelmConfigurationApi->edit_helm_advanced_settings: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit advanced settings
        api_response = api_instance.edit_helm_advanced_settings(helm_id, helm_advanced_settings=helm_advanced_settings)
        pprint(api_response)
    except qovery.ApiException as e:
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
import qovery
from qovery.api import helm_configuration_api
from qovery.model.helm_advanced_settings import HelmAdvancedSettings
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
    api_instance = helm_configuration_api.HelmConfigurationApi(api_client)
    helm_id = "helmId_example" # str | Helm ID

    # example passing only required values which don't have defaults set
    try:
        # Get advanced settings
        api_response = api_instance.get_helm_advanced_settings(helm_id)
        pprint(api_response)
    except qovery.ApiException as e:
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

