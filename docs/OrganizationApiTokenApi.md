# qovery.OrganizationApiTokenApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_organization_api_token**](OrganizationApiTokenApi.md#create_organization_api_token) | **POST** /organization/{organizationId}/apiToken | Create an organization api token
[**delete_organization_api_token**](OrganizationApiTokenApi.md#delete_organization_api_token) | **DELETE** /organization/{organizationId}/apiToken/{apiTokenId} | Delete organization api token
[**list_organization_api_tokens**](OrganizationApiTokenApi.md#list_organization_api_tokens) | **GET** /organization/{organizationId}/apiToken | List organization api tokens


# **create_organization_api_token**
> OrganizationApiTokenCreate create_organization_api_token(organization_id)

Create an organization api token

Create an organization api token. You can use the generated token to interact in a programmatic way with our API.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import organization_api_token_api
from qovery.model.organization_api_token_create import OrganizationApiTokenCreate
from qovery.model.organization_api_token_create_request import OrganizationApiTokenCreateRequest
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
    api_instance = organization_api_token_api.OrganizationApiTokenApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    organization_api_token_create_request = OrganizationApiTokenCreateRequest(
        name="name_example",
        description="description_example",
        scope=OrganizationApiTokenScope("ADMIN"),
    ) # OrganizationApiTokenCreateRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create an organization api token
        api_response = api_instance.create_organization_api_token(organization_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling OrganizationApiTokenApi->create_organization_api_token: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an organization api token
        api_response = api_instance.create_organization_api_token(organization_id, organization_api_token_create_request=organization_api_token_create_request)
        pprint(api_response)
    except qovery.ApiException as e:
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

[bearerAuth](../README.md#bearerAuth)

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

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import organization_api_token_api
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
    api_instance = organization_api_token_api.OrganizationApiTokenApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    api_token_id = "apiTokenId_example" # str | Organization Api Token ID

    # example passing only required values which don't have defaults set
    try:
        # Delete organization api token
        api_instance.delete_organization_api_token(organization_id, api_token_id)
    except qovery.ApiException as e:
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

[bearerAuth](../README.md#bearerAuth)

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

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import organization_api_token_api
from qovery.model.organization_api_token_response_list import OrganizationApiTokenResponseList
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
    api_instance = organization_api_token_api.OrganizationApiTokenApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID

    # example passing only required values which don't have defaults set
    try:
        # List organization api tokens
        api_response = api_instance.list_organization_api_tokens(organization_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling OrganizationApiTokenApi->list_organization_api_tokens: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |

### Return type

[**OrganizationApiTokenResponseList**](OrganizationApiTokenResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

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

