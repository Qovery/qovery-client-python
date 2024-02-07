# qovery.ApplicationConfigurationApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edit_advanced_settings**](ApplicationConfigurationApi.md#edit_advanced_settings) | **PUT** /application/{applicationId}/advancedSettings | Edit advanced settings
[**edit_application_network**](ApplicationConfigurationApi.md#edit_application_network) | **PUT** /application/{applicationId}/network | Edit Application Network
[**get_advanced_settings**](ApplicationConfigurationApi.md#get_advanced_settings) | **GET** /application/{applicationId}/advancedSettings | Get advanced settings
[**get_application_network**](ApplicationConfigurationApi.md#get_application_network) | **GET** /application/{applicationId}/network | Get Application Network information


# **edit_advanced_settings**
> ApplicationAdvancedSettings edit_advanced_settings(application_id, application_advanced_settings=application_advanced_settings)

Edit advanced settings

Edit advanced settings by returning table of advanced settings.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import os
import qovery
from qovery.models.application_advanced_settings import ApplicationAdvancedSettings
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
    api_instance = qovery.ApplicationConfigurationApi(api_client)
    application_id = 'application_id_example' # str | Application ID
    application_advanced_settings = qovery.ApplicationAdvancedSettings() # ApplicationAdvancedSettings |  (optional)

    try:
        # Edit advanced settings
        api_response = api_instance.edit_advanced_settings(application_id, application_advanced_settings=application_advanced_settings)
        print("The response of ApplicationConfigurationApi->edit_advanced_settings:\n")
        pprint(api_response)
    except Exception as e:
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
> ApplicationNetwork edit_application_network(application_id, application_network_request=application_network_request)

Edit Application Network

Edit the Network settings of the application.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import os
import qovery
from qovery.models.application_network import ApplicationNetwork
from qovery.models.application_network_request import ApplicationNetworkRequest
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
    api_instance = qovery.ApplicationConfigurationApi(api_client)
    application_id = 'application_id_example' # str | Application ID
    application_network_request = qovery.ApplicationNetworkRequest() # ApplicationNetworkRequest |  (optional)

    try:
        # Edit Application Network
        api_response = api_instance.edit_application_network(application_id, application_network_request=application_network_request)
        print("The response of ApplicationConfigurationApi->edit_application_network:\n")
        pprint(api_response)
    except Exception as e:
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

Get list and values of the advanced settings of the application. Default values for each setting are available in [our documentation](https://hub.qovery.com/docs/using-qovery/configuration/advanced-settings/) 

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import os
import qovery
from qovery.models.application_advanced_settings import ApplicationAdvancedSettings
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
    api_instance = qovery.ApplicationConfigurationApi(api_client)
    application_id = 'application_id_example' # str | Application ID

    try:
        # Get advanced settings
        api_response = api_instance.get_advanced_settings(application_id)
        print("The response of ApplicationConfigurationApi->get_advanced_settings:\n")
        pprint(api_response)
    except Exception as e:
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
import os
import qovery
from qovery.models.application_network import ApplicationNetwork
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
    api_instance = qovery.ApplicationConfigurationApi(api_client)
    application_id = 'application_id_example' # str | Application ID

    try:
        # Get Application Network information
        api_response = api_instance.get_application_network(application_id)
        print("The response of ApplicationConfigurationApi->get_application_network:\n")
        pprint(api_response)
    except Exception as e:
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

