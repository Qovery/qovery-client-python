# qovery.HelmCustomDomainApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_helm_custom_domain**](HelmCustomDomainApi.md#delete_helm_custom_domain) | **DELETE** /helm/{helmId}/customDomain/{customDomainId} | Delete a Custom Domain
[**edit_helm_custom_domain**](HelmCustomDomainApi.md#edit_helm_custom_domain) | **PUT** /helm/{helmId}/customDomain/{customDomainId} | Edit a Custom Domain
[**get_helm_custom_domain**](HelmCustomDomainApi.md#get_helm_custom_domain) | **GET** /helm/{helmId}/customDomain/{customDomainId} | Get a Custom Domain


# **delete_helm_custom_domain**
> delete_helm_custom_domain(helm_id, custom_domain_id)

Delete a Custom Domain

To delete an CustomDomain you must have the project user permission

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import helm_custom_domain_api
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
    api_instance = helm_custom_domain_api.HelmCustomDomainApi(api_client)
    helm_id = "helmId_example" # str | Helm ID
    custom_domain_id = "customDomainId_example" # str | Custom Domain ID

    # example passing only required values which don't have defaults set
    try:
        # Delete a Custom Domain
        api_instance.delete_helm_custom_domain(helm_id, custom_domain_id)
    except qovery.ApiException as e:
        print("Exception when calling HelmCustomDomainApi->delete_helm_custom_domain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **helm_id** | **str**| Helm ID |
 **custom_domain_id** | **str**| Custom Domain ID |

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was deleted successfully |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_helm_custom_domain**
> CustomDomain edit_helm_custom_domain(helm_id, custom_domain_id)

Edit a Custom Domain

To edit a Custom Domain you must have the project user permission

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import helm_custom_domain_api
from qovery.model.custom_domain import CustomDomain
from qovery.model.custom_domain_request import CustomDomainRequest
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
    api_instance = helm_custom_domain_api.HelmCustomDomainApi(api_client)
    helm_id = "helmId_example" # str | Helm ID
    custom_domain_id = "customDomainId_example" # str | Custom Domain ID
    custom_domain_request = CustomDomainRequest(
        domain="my.domain.tld",
        generate_certificate=True,
    ) # CustomDomainRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Edit a Custom Domain
        api_response = api_instance.edit_helm_custom_domain(helm_id, custom_domain_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling HelmCustomDomainApi->edit_helm_custom_domain: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit a Custom Domain
        api_response = api_instance.edit_helm_custom_domain(helm_id, custom_domain_id, custom_domain_request=custom_domain_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling HelmCustomDomainApi->edit_helm_custom_domain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **helm_id** | **str**| Helm ID |
 **custom_domain_id** | **str**| Custom Domain ID |
 **custom_domain_request** | [**CustomDomainRequest**](CustomDomainRequest.md)|  | [optional]

### Return type

[**CustomDomain**](CustomDomain.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Edit a CustomDomain |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_helm_custom_domain**
> CustomDomain get_helm_custom_domain(helm_id, custom_domain_id)

Get a Custom Domain

Get a custom domain

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import helm_custom_domain_api
from qovery.model.custom_domain import CustomDomain
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
    api_instance = helm_custom_domain_api.HelmCustomDomainApi(api_client)
    helm_id = "helmId_example" # str | Helm ID
    custom_domain_id = "customDomainId_example" # str | Custom Domain ID

    # example passing only required values which don't have defaults set
    try:
        # Get a Custom Domain
        api_response = api_instance.get_helm_custom_domain(helm_id, custom_domain_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling HelmCustomDomainApi->get_helm_custom_domain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **helm_id** | **str**| Helm ID |
 **custom_domain_id** | **str**| Custom Domain ID |

### Return type

[**CustomDomain**](CustomDomain.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a CustomDomain |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

