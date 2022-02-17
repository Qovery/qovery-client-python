# qovery.ApplicationConfigurationApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edit_application_network**](ApplicationConfigurationApi.md#edit_application_network) | **PUT** /application/{applicationId}/network | Edit Application Network
[**get_application_network**](ApplicationConfigurationApi.md#get_application_network) | **GET** /application/{applicationId}/network | Get Application Network information


# **edit_application_network**
> ApplicationNetworkResponse edit_application_network(application_id)

Edit Application Network

Edit the Network settings of the application.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import application_configuration_api
from qovery.model.application_network_request import ApplicationNetworkRequest
from qovery.model.application_network_response import ApplicationNetworkResponse
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

[**ApplicationNetworkResponse**](ApplicationNetworkResponse.md)

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

# **get_application_network**
> ApplicationNetworkResponse get_application_network(application_id)

Get Application Network information

Get status of the application network settings.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import application_configuration_api
from qovery.model.application_network_response import ApplicationNetworkResponse
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

[**ApplicationNetworkResponse**](ApplicationNetworkResponse.md)

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

