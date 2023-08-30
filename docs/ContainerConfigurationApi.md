# qovery.ContainerConfigurationApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edit_container_advanced_settings**](ContainerConfigurationApi.md#edit_container_advanced_settings) | **PUT** /container/{containerId}/advancedSettings | Edit advanced settings
[**edit_container_network**](ContainerConfigurationApi.md#edit_container_network) | **PUT** /container/{containerId}/network | Edit Container Network
[**get_container_advanced_settings**](ContainerConfigurationApi.md#get_container_advanced_settings) | **GET** /container/{containerId}/advancedSettings | Get advanced settings
[**get_container_network**](ContainerConfigurationApi.md#get_container_network) | **GET** /container/{containerId}/network | Get Container Network information


# **edit_container_advanced_settings**
> ContainerAdvancedSettings edit_container_advanced_settings(container_id)

Edit advanced settings

Edit advanced settings by returning table of advanced settings.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import container_configuration_api
from qovery.model.container_advanced_settings import ContainerAdvancedSettings
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
    api_instance = container_configuration_api.ContainerConfigurationApi(api_client)
    container_id = "containerId_example" # str | Container ID
    container_advanced_settings = ContainerAdvancedSettings(
        deployment_custom_domain_check_enabled=True,
        deployment_termination_grace_period_seconds=60,
        deployment_affinity_node_required={
            "key": "key_example",
        },
        deployment_antiaffinity_pod="Preferred",
        deployment_update_strategy_type="RollingUpdate",
        deployment_update_strategy_rolling_update_max_unavailable_percent=25,
        deployment_update_strategy_rolling_update_max_surge_percent=25,
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
        network_ingress_grpc_send_timeout_seconds=60,
        network_ingress_grpc_read_timeout_seconds=60,
        network_ingress_whitelist_source_range="0.0.0.0/0",
        network_ingress_denylist_source_range="",
        network_ingress_basic_auth_env_var="",
        network_ingress_enable_sticky_session=False,
        security_service_account_name="",
        hpa_cpu_average_utilization_percent=60,
    ) # ContainerAdvancedSettings |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Edit advanced settings
        api_response = api_instance.edit_container_advanced_settings(container_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainerConfigurationApi->edit_container_advanced_settings: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit advanced settings
        api_response = api_instance.edit_container_advanced_settings(container_id, container_advanced_settings=container_advanced_settings)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainerConfigurationApi->edit_container_advanced_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Container ID |
 **container_advanced_settings** | [**ContainerAdvancedSettings**](ContainerAdvancedSettings.md)|  | [optional]

### Return type

[**ContainerAdvancedSettings**](ContainerAdvancedSettings.md)

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

# **edit_container_network**
> ContainerNetwork edit_container_network(container_id)

Edit Container Network

Edit the Network settings of the container.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import container_configuration_api
from qovery.model.container_network_request import ContainerNetworkRequest
from qovery.model.container_network import ContainerNetwork
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
    api_instance = container_configuration_api.ContainerConfigurationApi(api_client)
    container_id = "containerId_example" # str | Container ID
    container_network_request = ContainerNetworkRequest(
        sticky_session=False,
    ) # ContainerNetworkRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Edit Container Network
        api_response = api_instance.edit_container_network(container_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainerConfigurationApi->edit_container_network: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit Container Network
        api_response = api_instance.edit_container_network(container_id, container_network_request=container_network_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainerConfigurationApi->edit_container_network: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Container ID |
 **container_network_request** | [**ContainerNetworkRequest**](ContainerNetworkRequest.md)|  | [optional]

### Return type

[**ContainerNetwork**](ContainerNetwork.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Updated container network setting |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_container_advanced_settings**
> ContainerAdvancedSettings get_container_advanced_settings(container_id)

Get advanced settings

Get list and values of the advanced settings of the container.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import container_configuration_api
from qovery.model.container_advanced_settings import ContainerAdvancedSettings
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
    api_instance = container_configuration_api.ContainerConfigurationApi(api_client)
    container_id = "containerId_example" # str | Container ID

    # example passing only required values which don't have defaults set
    try:
        # Get advanced settings
        api_response = api_instance.get_container_advanced_settings(container_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainerConfigurationApi->get_container_advanced_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Container ID |

### Return type

[**ContainerAdvancedSettings**](ContainerAdvancedSettings.md)

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

# **get_container_network**
> ContainerNetwork get_container_network(container_id)

Get Container Network information

Get status of the container network settings.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import container_configuration_api
from qovery.model.container_network import ContainerNetwork
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
    api_instance = container_configuration_api.ContainerConfigurationApi(api_client)
    container_id = "containerId_example" # str | Container ID

    # example passing only required values which don't have defaults set
    try:
        # Get Container Network information
        api_response = api_instance.get_container_network(container_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainerConfigurationApi->get_container_network: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Container ID |

### Return type

[**ContainerNetwork**](ContainerNetwork.md)

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

