# qovery.ContainerConfigurationApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edit_container_advanced_settings**](ContainerConfigurationApi.md#edit_container_advanced_settings) | **PUT** /container/{containerId}/advancedSettings | NOT YET IMPLEMENTED - Edit advanced settings
[**edit_container_network**](ContainerConfigurationApi.md#edit_container_network) | **PUT** /container/{containerId}/network | NOT YET IMPLEMENTED - Edit Container Network
[**get_container_advanced_settings**](ContainerConfigurationApi.md#get_container_advanced_settings) | **GET** /container/{containerId}/advancedSettings | NOT YET IMPLEMENTED - Get advanced settings
[**get_container_network**](ContainerConfigurationApi.md#get_container_network) | **GET** /container/{containerId}/network | NOT YET IMPLEMENTED - Get Container Network information


# **edit_container_advanced_settings**
> ContainerAdvancedSettingsResponse edit_container_advanced_settings(container_id)

NOT YET IMPLEMENTED - Edit advanced settings

Edit advanced settings by returning table of advanced settings.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import container_configuration_api
from qovery.model.container_advanced_settings_response import ContainerAdvancedSettingsResponse
from qovery.model.container_advanced_settings_request import ContainerAdvancedSettingsRequest
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
    api_instance = container_configuration_api.ContainerConfigurationApi(api_client)
    container_id = "containerId_example" # str | Container ID
    container_advanced_settings_request = ContainerAdvancedSettingsRequest([
        ContainerAdvancedSettings(
            deployment_custom_domain_check_enabled=True,
            network_ingress_proxy_body_size_mb=100,
            network_ingress_enable_cors=False,
            network_ingress_cors_allow_origin="*",
            network_ingress_cors_allow_methods="GET, PUT, POST, DELETE, PATCH, OPTIONS",
            network_ingress_cors_allow_headers="DNT,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range,Authorization",
            readiness_probe_type="TCP",
            readiness_probe_http_get_path="/",
            readiness_probe_initial_delay_seconds=30,
            readiness_probe_period_seconds=10,
            readiness_probe_timeout_seconds=1,
            readiness_probe_success_threshold=1,
            readiness_probe_failure_threshold=3,
            liveness_probe_type="TCP",
            liveness_probe_http_get_path="/",
            liveness_probe_initial_delay_seconds=30,
            liveness_probe_period_seconds=10,
            liveness_probe_timeout_seconds=5,
            liveness_probe_success_threshold=1,
            liveness_probe_failure_threshold=3,
        ),
    ]) # ContainerAdvancedSettingsRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # NOT YET IMPLEMENTED - Edit advanced settings
        api_response = api_instance.edit_container_advanced_settings(container_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainerConfigurationApi->edit_container_advanced_settings: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # NOT YET IMPLEMENTED - Edit advanced settings
        api_response = api_instance.edit_container_advanced_settings(container_id, container_advanced_settings_request=container_advanced_settings_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainerConfigurationApi->edit_container_advanced_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Container ID |
 **container_advanced_settings_request** | [**ContainerAdvancedSettingsRequest**](ContainerAdvancedSettingsRequest.md)|  | [optional]

### Return type

[**ContainerAdvancedSettingsResponse**](ContainerAdvancedSettingsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

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

NOT YET IMPLEMENTED - Edit Container Network

Edit the Network settings of the container.

### Example

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
        # NOT YET IMPLEMENTED - Edit Container Network
        api_response = api_instance.edit_container_network(container_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainerConfigurationApi->edit_container_network: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # NOT YET IMPLEMENTED - Edit Container Network
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

[bearerAuth](../README.md#bearerAuth)

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
> ContainerAdvancedSettingsResponse get_container_advanced_settings(container_id)

NOT YET IMPLEMENTED - Get advanced settings

Get list and values of the advanced settings of the container.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import container_configuration_api
from qovery.model.container_advanced_settings_response import ContainerAdvancedSettingsResponse
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
    api_instance = container_configuration_api.ContainerConfigurationApi(api_client)
    container_id = "containerId_example" # str | Container ID

    # example passing only required values which don't have defaults set
    try:
        # NOT YET IMPLEMENTED - Get advanced settings
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

[**ContainerAdvancedSettingsResponse**](ContainerAdvancedSettingsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

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

NOT YET IMPLEMENTED - Get Container Network information

Get status of the container network settings.

### Example

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
        # NOT YET IMPLEMENTED - Get Container Network information
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

[bearerAuth](../README.md#bearerAuth)

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

