# qovery.GithubAppApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**organization_github_app_connect**](GithubAppApi.md#organization_github_app_connect) | **POST** /organization/{organizationId}/github/connect | Connect a github account to an organization
[**organization_github_app_disconnect**](GithubAppApi.md#organization_github_app_disconnect) | **DELETE** /organization/{organizationId}/github/disconnect | Disconnect a github account from an organization


# **organization_github_app_connect**
> organization_github_app_connect(organization_id)

Connect a github account to an organization

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import github_app_api
from qovery.model.organization_github_app_connect_request import OrganizationGithubAppConnectRequest
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
    api_instance = github_app_api.GithubAppApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    organization_github_app_connect_request = OrganizationGithubAppConnectRequest(
        installation_id="installation_id_example",
        code="code_example",
    ) # OrganizationGithubAppConnectRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Connect a github account to an organization
        api_instance.organization_github_app_connect(organization_id)
    except qovery.ApiException as e:
        print("Exception when calling GithubAppApi->organization_github_app_connect: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Connect a github account to an organization
        api_instance.organization_github_app_connect(organization_id, organization_github_app_connect_request=organization_github_app_connect_request)
    except qovery.ApiException as e:
        print("Exception when calling GithubAppApi->organization_github_app_connect: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **organization_github_app_connect_request** | [**OrganizationGithubAppConnectRequest**](OrganizationGithubAppConnectRequest.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Github App connected |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_github_app_disconnect**
> organization_github_app_disconnect(organization_id)

Disconnect a github account from an organization

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import github_app_api
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
    api_instance = github_app_api.GithubAppApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    force = True # bool | Indicates if the github app should be disconnected despite github applications linked to organization (optional)

    # example passing only required values which don't have defaults set
    try:
        # Disconnect a github account from an organization
        api_instance.organization_github_app_disconnect(organization_id)
    except qovery.ApiException as e:
        print("Exception when calling GithubAppApi->organization_github_app_disconnect: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Disconnect a github account from an organization
        api_instance.organization_github_app_disconnect(organization_id, force=force)
    except qovery.ApiException as e:
        print("Exception when calling GithubAppApi->organization_github_app_disconnect: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **force** | **bool**| Indicates if the github app should be disconnected despite github applications linked to organization | [optional]

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
**204** | Github App disconnected |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

