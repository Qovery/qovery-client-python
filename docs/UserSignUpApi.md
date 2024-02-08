# qovery.UserSignUpApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user_sign_up**](UserSignUpApi.md#create_user_sign_up) | **POST** /admin/userSignUp | Send Sign Up request
[**get_user_sign_up**](UserSignUpApi.md#get_user_sign_up) | **GET** /admin/userSignUp | Get Sign up information


# **create_user_sign_up**
> create_user_sign_up()

Send Sign Up request

Send a Sign Up request containing the user information

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import user_sign_up_api
from qovery.model.sign_up_request import SignUpRequest
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
    api_instance = user_sign_up_api.UserSignUpApi(api_client)
    sign_up_request = SignUpRequest(
        first_name="first_name_example",
        last_name="last_name_example",
        user_email="user_email_example",
        type_of_use=TypeOfUseEnum("PERSONAL"),
        qovery_usage="qovery_usage_example",
        company_name="company_name_example",
        company_size=CompanySizeEnum("1-10"),
        user_role="user_role_example",
        qovery_usage_other="qovery_usage_other_example",
        user_questions="user_questions_example",
        current_step="current_step_example",
        dx_auth=True,
    ) # SignUpRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Send Sign Up request
        api_instance.create_user_sign_up(sign_up_request=sign_up_request)
    except qovery.ApiException as e:
        print("Exception when calling UserSignUpApi->create_user_sign_up: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sign_up_request** | [**SignUpRequest**](SignUpRequest.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sign up request stored |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_sign_up**
> SignUp get_user_sign_up()

Get Sign up information

Retrieve the Sign Up information of the user

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import user_sign_up_api
from qovery.model.sign_up import SignUp
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
    api_instance = user_sign_up_api.UserSignUpApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Sign up information
        api_response = api_instance.get_user_sign_up()
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling UserSignUpApi->get_user_sign_up: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SignUp**](SignUp.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | If a previous sign up request for the same user has been found, the information is returned in the payload |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

