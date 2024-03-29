# qovery.OrganizationApiTokenApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_organization_api_token**](OrganizationApiTokenApi.md#create_organization_api_token) | **POST** /organization/{organizationId}/apiToken | Create an organization api token
[**delete_organization_api_token**](OrganizationApiTokenApi.md#delete_organization_api_token) | **DELETE** /organization/{organizationId}/apiToken/{apiTokenId} | Delete organization api token
[**list_organization_api_tokens**](OrganizationApiTokenApi.md#list_organization_api_tokens) | **GET** /organization/{organizationId}/apiToken | List organization api tokens


# **create_organization_api_token**
> OrganizationApiTokenCreate create_organization_api_token(organization_id, organization_api_token_create_request=organization_api_token_create_request)

Create an organization api token

Create an organization api token. You can use the generated token to interact in a programmatic way with our API.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import qovery
from qovery.models.organization_api_token_create import OrganizationApiTokenCreate
from qovery.models.organization_api_token_create_request import OrganizationApiTokenCreateRequest
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
    api_instance = qovery.OrganizationApiTokenApi(api_client)
    organization_id = 'organization_id_example' # str | Organization ID
    organization_api_token_create_request = qovery.OrganizationApiTokenCreateRequest() # OrganizationApiTokenCreateRequest |  (optional)

    try:
        # Create an organization api token
        api_response = api_instance.create_organization_api_token(organization_id, organization_api_token_create_request=organization_api_token_create_request)
        print("The response of OrganizationApiTokenApi->create_organization_api_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApiTokenApi->create_organization_api_token: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID | 
 **organization_api_token_create_request** | [**OrganizationApiTokenCreateRequest**](OrganizationApiTokenCreateRequest.md)|  | [optional] 

### Return type

[**OrganizationApiTokenCreate**](OrganizationApiTokenCreate.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Organization api token created |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Organization Api Token name is already taken |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_organization_api_token**
> delete_organization_api_token(organization_id, api_token_id)

Delete organization api token

Delete organization api token

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import qovery
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
    api_instance = qovery.OrganizationApiTokenApi(api_client)
    organization_id = 'organization_id_example' # str | Organization ID
    api_token_id = 'api_token_id_example' # str | Organization Api Token ID

    try:
        # Delete organization api token
        api_instance.delete_organization_api_token(organization_id, api_token_id)
    except Exception as e:
        print("Exception when calling OrganizationApiTokenApi->delete_organization_api_token: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID | 
 **api_token_id** | **str**| Organization Api Token ID | 

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
**204** | no content |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_organization_api_tokens**
> OrganizationApiTokenResponseList list_organization_api_tokens(organization_id)

List organization api tokens

List organization api tokens

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import qovery
from qovery.models.organization_api_token_response_list import OrganizationApiTokenResponseList
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
    api_instance = qovery.OrganizationApiTokenApi(api_client)
    organization_id = 'organization_id_example' # str | Organization ID

    try:
        # List organization api tokens
        api_response = api_instance.list_organization_api_tokens(organization_id)
        print("The response of OrganizationApiTokenApi->list_organization_api_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApiTokenApi->list_organization_api_tokens: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID | 

### Return type

[**OrganizationApiTokenResponseList**](OrganizationApiTokenResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List organization api tokens |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

