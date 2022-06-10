# qovery.ApplicationConfigurationApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edit_advanced_settings**](ApplicationConfigurationApi.md#edit_advanced_settings) | **PUT** /application/{applicationId}/advancedSettings | Edit advanced settings
[**edit_application_network**](ApplicationConfigurationApi.md#edit_application_network) | **PUT** /application/{applicationId}/network | Edit Application Network
[**get_advanced_settings**](ApplicationConfigurationApi.md#get_advanced_settings) | **GET** /application/{applicationId}/advancedSettings | Get advanced settings
[**get_application_network**](ApplicationConfigurationApi.md#get_application_network) | **GET** /application/{applicationId}/network | Get Application Network information


# **edit_advanced_settings**
> ApplicationAdvancedSettingsResponse edit_advanced_settings(application_id)

Edit advanced settings

Edit advanced settings by returning table of advanced settings.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import application_configuration_api
from qovery.model.application_advanced_settings_request import ApplicationAdvancedSettingsRequest
from qovery.model.application_advanced_settings_response import ApplicationAdvancedSettingsResponse
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
    api_instance = application_configuration_api.ApplicationConfigurationApi(api_client)
    application_id = "applicationId_example" # str | Application ID
    application_advanced_settings_request = ApplicationAdvancedSettingsRequest([
        ApplicationAdvancedSettings(
            deployment_delay_start_time_sec=30,
            deployment_custom_domain_check_enabled=True,
            build_timeout_max_sec=1800,
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
            hpa_cpu_average_utilization_percent=60,
        ),
    ]) # ApplicationAdvancedSettingsRequest |  (optional)

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
        api_response = api_instance.edit_advanced_settings(application_id, application_advanced_settings_request=application_advanced_settings_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationConfigurationApi->edit_advanced_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID |
 **application_advanced_settings_request** | [**ApplicationAdvancedSettingsRequest**](ApplicationAdvancedSettingsRequest.md)|  | [optional]

### Return type

[**ApplicationAdvancedSettingsResponse**](ApplicationAdvancedSettingsResponse.md)

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

# **edit_application_network**
> ApplicationNetwork edit_application_network(application_id)

Edit Application Network

Edit the Network settings of the application.

### Example

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

[bearerAuth](../README.md#bearerAuth)

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
> ApplicationAdvancedSettingsResponse get_advanced_settings(application_id)

Get advanced settings

Get list and values of the advanced settings of the application.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import application_configuration_api
from qovery.model.application_advanced_settings_response import ApplicationAdvancedSettingsResponse
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

[**ApplicationAdvancedSettingsResponse**](ApplicationAdvancedSettingsResponse.md)

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

# **get_application_network**
> ApplicationNetwork get_application_network(application_id)

Get Application Network information

Get status of the application network settings.

### Example

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

