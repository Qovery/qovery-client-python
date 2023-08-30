# qovery.ApplicationConfigurationApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edit_advanced_settings**](ApplicationConfigurationApi.md#edit_advanced_settings) | **PUT** /application/{applicationId}/advancedSettings | Edit advanced settings
[**edit_application_network**](ApplicationConfigurationApi.md#edit_application_network) | **PUT** /application/{applicationId}/network | Edit Application Network
[**get_advanced_settings**](ApplicationConfigurationApi.md#get_advanced_settings) | **GET** /application/{applicationId}/advancedSettings | Get advanced settings
[**get_application_network**](ApplicationConfigurationApi.md#get_application_network) | **GET** /application/{applicationId}/network | Get Application Network information


# **edit_advanced_settings**
> ApplicationAdvancedSettings edit_advanced_settings(application_id)

Edit advanced settings

Edit advanced settings by returning table of advanced settings.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import application_configuration_api
from qovery.model.application_advanced_settings import ApplicationAdvancedSettings
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
    api_instance = application_configuration_api.ApplicationConfigurationApi(api_client)
    application_id = "applicationId_example" # str | Application ID
    application_advanced_settings = ApplicationAdvancedSettings(
        deployment_custom_domain_check_enabled=True,
        deployment_termination_grace_period_seconds=60,
        deployment_affinity_node_required={
            "key": "key_example",
        },
        deployment_antiaffinity_pod="Preferred",
        deployment_update_strategy_type="RollingUpdate",
        deployment_update_strategy_rolling_update_max_unavailable_percent=25,
        deployment_update_strategy_rolling_update_max_surge_percent=25,
        build_timeout_max_sec=1800,
        build_cpu_max_in_milli=4000,
        build_ram_max_in_gib=8,
        network_ingress_proxy_body_size_mb=100,
        network_ingress_enable_cors=False,
        network_ingress_cors_allow_origin="*",
        network_ingress_cors_allow_methods="GET, PUT, POST, DELETE, PATCH, OPTIONS",
        network_ingress_cors_allow_headers="DNT,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range,Authorization",
        network_ingress_proxy_buffer_size_kb=4,
        network_ingress_keepalive_time_seconds=3600,
        network_ingress_keepalive_timeout_seconds=60,
        network_ingress_send_timeout_seconds=60,
        network_ingress_proxy_connect_timeout_seconds=60,
        network_ingress_proxy_send_timeout_seconds=60,
        network_ingress_proxy_read_timeout_seconds=60,
        network_ingress_whitelist_source_range="0.0.0.0/0",
        network_ingress_denylist_source_range="",
        network_ingress_basic_auth_env_var="",
        network_ingress_enable_sticky_session=False,
        network_ingress_grpc_send_timeout_seconds=60,
        network_ingress_grpc_read_timeout_seconds=60,
        hpa_cpu_average_utilization_percent=60,
        security_service_account_name="",
    ) # ApplicationAdvancedSettings |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Edit advanced settings
        api_response = api_instance.edit_advanced_settings(application_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationConfigurationApi->edit_advanced_settings: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit advanced settings
        api_response = api_instance.edit_advanced_settings(application_id, application_advanced_settings=application_advanced_settings)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationConfigurationApi->edit_advanced_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID |
 **application_advanced_settings** | [**ApplicationAdvancedSettings**](ApplicationAdvancedSettings.md)|  | [optional]

### Return type

[**ApplicationAdvancedSettings**](ApplicationAdvancedSettings.md)

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

# **edit_application_network**
> ApplicationNetwork edit_application_network(application_id)

Edit Application Network

Edit the Network settings of the application.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import application_configuration_api
from qovery.model.application_network import ApplicationNetwork
from qovery.model.application_network_request import ApplicationNetworkRequest
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
    api_instance = application_configuration_api.ApplicationConfigurationApi(api_client)
    application_id = "applicationId_example" # str | Application ID
    application_network_request = ApplicationNetworkRequest(
        sticky_session=False,
    ) # ApplicationNetworkRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Edit Application Network
        api_response = api_instance.edit_application_network(application_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationConfigurationApi->edit_application_network: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit Application Network
        api_response = api_instance.edit_application_network(application_id, application_network_request=application_network_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationConfigurationApi->edit_application_network: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID |
 **application_network_request** | [**ApplicationNetworkRequest**](ApplicationNetworkRequest.md)|  | [optional]

### Return type

[**ApplicationNetwork**](ApplicationNetwork.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Updated application network setting |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_advanced_settings**
> ApplicationAdvancedSettings get_advanced_settings(application_id)

Get advanced settings

Get list and values of the advanced settings of the application.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import application_configuration_api
from qovery.model.application_advanced_settings import ApplicationAdvancedSettings
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
    api_instance = application_configuration_api.ApplicationConfigurationApi(api_client)
    application_id = "applicationId_example" # str | Application ID

    # example passing only required values which don't have defaults set
    try:
        # Get advanced settings
        api_response = api_instance.get_advanced_settings(application_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationConfigurationApi->get_advanced_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID |

### Return type

[**ApplicationAdvancedSettings**](ApplicationAdvancedSettings.md)

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

# **get_application_network**
> ApplicationNetwork get_application_network(application_id)

Get Application Network information

Get status of the application network settings.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import application_configuration_api
from qovery.model.application_network import ApplicationNetwork
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
    api_instance = application_configuration_api.ApplicationConfigurationApi(api_client)
    application_id = "applicationId_example" # str | Application ID

    # example passing only required values which don't have defaults set
    try:
        # Get Application Network information
        api_response = api_instance.get_application_network(application_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationConfigurationApi->get_application_network: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID |

### Return type

[**ApplicationNetwork**](ApplicationNetwork.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Network information |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

