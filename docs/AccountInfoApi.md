# qovery.AccountInfoApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edit_account_information**](AccountInfoApi.md#edit_account_information) | **PUT** /account | Edit account information
[**get_account_information**](AccountInfoApi.md#get_account_information) | **GET** /account | Get Account information


# **edit_account_information**
> AccountInfo edit_account_information()

Edit account information

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import account_info_api
from qovery.model.account_info import AccountInfo
from qovery.model.account_info_edit_request import AccountInfoEditRequest
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
    api_instance = account_info_api.AccountInfoApi(api_client)
    account_info_edit_request = AccountInfoEditRequest(
        communication_email="communication_email_example",
    ) # AccountInfoEditRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit account information
        api_response = api_instance.edit_account_information(account_info_edit_request=account_info_edit_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling AccountInfoApi->edit_account_information: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_info_edit_request** | [**AccountInfoEditRequest**](AccountInfoEditRequest.md)|  | [optional]

### Return type

[**AccountInfo**](AccountInfo.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Edit application |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_information**
> AccountInfo get_account_information()

Get Account information

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import account_info_api
from qovery.model.account_info import AccountInfo
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
    api_instance = account_info_api.AccountInfoApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Account information
        api_response = api_instance.get_account_information()
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling AccountInfoApi->get_account_information: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AccountInfo**](AccountInfo.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get account info |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

