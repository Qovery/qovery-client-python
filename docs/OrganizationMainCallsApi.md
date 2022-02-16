# qovery.OrganizationMainCallsApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_organization**](OrganizationMainCallsApi.md#create_organization) | **POST** /organization | Create an organization
[**delete_organization**](OrganizationMainCallsApi.md#delete_organization) | **DELETE** /organization/{organizationId} | Delete an organization
[**edit_organization**](OrganizationMainCallsApi.md#edit_organization) | **PUT** /organization/{organizationId} | Edit an organization
[**get_organization**](OrganizationMainCallsApi.md#get_organization) | **GET** /organization/{organizationId} | Get organization by ID
[**list_organization**](OrganizationMainCallsApi.md#list_organization) | **GET** /organization | List user organizations


# **create_organization**
> OrganizationResponse create_organization()

Create an organization

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from api import organization_main_calls_api
from qovery.model.organization_request import OrganizationRequest
from qovery.model.organization_response import OrganizationResponse
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
    api_instance = organization_main_calls_api.OrganizationMainCallsApi(api_client)
    organization_request = OrganizationRequest(
        name="name_example",
        description="description_example",
        plan="COMMUNITY",
        website_url="website_url_example",
        repository="repository_example",
        logo_url="logo_url_example",
        icon_url="icon_url_example",
    ) # OrganizationRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an organization
        api_response = api_instance.create_organization(organization_request=organization_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling OrganizationMainCallsApi->create_organization: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_request** | [**OrganizationRequest**](OrganizationRequest.md)|  | [optional]

### Return type

[**OrganizationResponse**](OrganizationResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create organization |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Organization name is already taken |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_organization**
> delete_organization(organization_id)

Delete an organization

To delete an organization you must have the admin permission

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from api import organization_main_calls_api
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
    api_instance = organization_main_calls_api.OrganizationMainCallsApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID

    # example passing only required values which don't have defaults set
    try:
        # Delete an organization
        api_instance.delete_organization(organization_id)
    except qovery.ApiException as e:
        print("Exception when calling OrganizationMainCallsApi->delete_organization: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |

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
**204** | The resource was deleted successfully |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_organization**
> OrganizationResponse edit_organization(organization_id)

Edit an organization

To edit an organization you must have the admin permission

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from api import organization_main_calls_api
from qovery.model.organization_response import OrganizationResponse
from qovery.model.organization_edit_request import OrganizationEditRequest
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
    api_instance = organization_main_calls_api.OrganizationMainCallsApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    organization_edit_request = OrganizationEditRequest(
        name="name_example",
        description="description_example",
        website_url="website_url_example",
        repository="repository_example",
        logo_url="logo_url_example",
        icon_url="icon_url_example",
    ) # OrganizationEditRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Edit an organization
        api_response = api_instance.edit_organization(organization_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling OrganizationMainCallsApi->edit_organization: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit an organization
        api_response = api_instance.edit_organization(organization_id, organization_edit_request=organization_edit_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling OrganizationMainCallsApi->edit_organization: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **organization_edit_request** | [**OrganizationEditRequest**](OrganizationEditRequest.md)|  | [optional]

### Return type

[**OrganizationResponse**](OrganizationResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Edit an organization |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Organization name is already taken |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization**
> OrganizationResponse get_organization(organization_id)

Get organization by ID

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from api import organization_main_calls_api
from qovery.model.organization_response import OrganizationResponse
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
    api_instance = organization_main_calls_api.OrganizationMainCallsApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID

    # example passing only required values which don't have defaults set
    try:
        # Get organization by ID
        api_response = api_instance.get_organization(organization_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling OrganizationMainCallsApi->get_organization: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |

### Return type

[**OrganizationResponse**](OrganizationResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get organization by ID |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_organization**
> OrganizationResponseList list_organization()

List user organizations

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from api import organization_main_calls_api
from qovery.model.organization_response_list import OrganizationResponseList
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
    api_instance = organization_main_calls_api.OrganizationMainCallsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List user organizations
        api_response = api_instance.list_organization()
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling OrganizationMainCallsApi->list_organization: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**OrganizationResponseList**](OrganizationResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List organizations |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

