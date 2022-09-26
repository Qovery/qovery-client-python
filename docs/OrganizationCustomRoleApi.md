# qovery.OrganizationCustomRoleApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_organization_custom_role**](OrganizationCustomRoleApi.md#create_organization_custom_role) | **POST** /organization/{organizationId}/customRole | Create an organization custom role
[**delete_organization_custom_role**](OrganizationCustomRoleApi.md#delete_organization_custom_role) | **DELETE** /organization/{organizationId}/customRole/{customRoleId} | Delete organization custom role
[**edit_organization_custom_role**](OrganizationCustomRoleApi.md#edit_organization_custom_role) | **PUT** /organization/{organizationId}/customRole/{customRoleId} | Edit an organization custom role
[**get_organization_custom_role**](OrganizationCustomRoleApi.md#get_organization_custom_role) | **GET** /organization/{organizationId}/customRole/{customRoleId} | Get an organization custom role 
[**list_organization_custom_roles**](OrganizationCustomRoleApi.md#list_organization_custom_roles) | **GET** /organization/{organizationId}/customRole | List organization custom roles


# **create_organization_custom_role**
> OrganizationCustomRole create_organization_custom_role(organization_id)

Create an organization custom role

Create an organization custom role

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import organization_custom_role_api
from qovery.model.organization_custom_role import OrganizationCustomRole
from qovery.model.organization_custom_role_request import OrganizationCustomRoleRequest
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
    api_instance = organization_custom_role_api.OrganizationCustomRoleApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    organization_custom_role_request = OrganizationCustomRoleRequest(
        name="name_example",
        description="description_example",
        cluster_permissions=[
            OrganizationCustomRoleRequestClusterPermissionsInner(
                cluster_id="cluster_id_example",
                permission=OrganizationCustomRoleClusterPermission("VIEWER"),
            ),
        ],
        project_permissions=[
            OrganizationCustomRoleRequestProjectPermissionsInner(
                project_id="project_id_example",
                is_admin=False,
                permissions=[
                    OrganizationCustomRoleRequestProjectPermissionsInnerPermissionsInner(
                        environment_type=EnvironmentModeEnum("PRODUCTION"),
                        permission=OrganizationCustomRoleProjectPermission("NO_ACCESS"),
                    ),
                ],
            ),
        ],
    ) # OrganizationCustomRoleRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create an organization custom role
        api_response = api_instance.create_organization_custom_role(organization_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling OrganizationCustomRoleApi->create_organization_custom_role: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an organization custom role
        api_response = api_instance.create_organization_custom_role(organization_id, organization_custom_role_request=organization_custom_role_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling OrganizationCustomRoleApi->create_organization_custom_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **organization_custom_role_request** | [**OrganizationCustomRoleRequest**](OrganizationCustomRoleRequest.md)|  | [optional]

### Return type

[**OrganizationCustomRole**](OrganizationCustomRole.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Organization custom role created |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_organization_custom_role**
> delete_organization_custom_role(organization_id)

Delete organization custom role

Delete organization custom role

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import organization_custom_role_api
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
    api_instance = organization_custom_role_api.OrganizationCustomRoleApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID

    # example passing only required values which don't have defaults set
    try:
        # Delete organization custom role
        api_instance.delete_organization_custom_role(organization_id)
    except qovery.ApiException as e:
        print("Exception when calling OrganizationCustomRoleApi->delete_organization_custom_role: %s\n" % e)
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
**204** | no content |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_organization_custom_role**
> OrganizationCustomRole edit_organization_custom_role(organization_id)

Edit an organization custom role

Edit an organization custom role

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import organization_custom_role_api
from qovery.model.organization_custom_role import OrganizationCustomRole
from qovery.model.organization_custom_role_request import OrganizationCustomRoleRequest
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
    api_instance = organization_custom_role_api.OrganizationCustomRoleApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    organization_custom_role_request = OrganizationCustomRoleRequest(
        name="name_example",
        description="description_example",
        cluster_permissions=[
            OrganizationCustomRoleRequestClusterPermissionsInner(
                cluster_id="cluster_id_example",
                permission=OrganizationCustomRoleClusterPermission("VIEWER"),
            ),
        ],
        project_permissions=[
            OrganizationCustomRoleRequestProjectPermissionsInner(
                project_id="project_id_example",
                is_admin=False,
                permissions=[
                    OrganizationCustomRoleRequestProjectPermissionsInnerPermissionsInner(
                        environment_type=EnvironmentModeEnum("PRODUCTION"),
                        permission=OrganizationCustomRoleProjectPermission("NO_ACCESS"),
                    ),
                ],
            ),
        ],
    ) # OrganizationCustomRoleRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Edit an organization custom role
        api_response = api_instance.edit_organization_custom_role(organization_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling OrganizationCustomRoleApi->edit_organization_custom_role: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit an organization custom role
        api_response = api_instance.edit_organization_custom_role(organization_id, organization_custom_role_request=organization_custom_role_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling OrganizationCustomRoleApi->edit_organization_custom_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **organization_custom_role_request** | [**OrganizationCustomRoleRequest**](OrganizationCustomRoleRequest.md)|  | [optional]

### Return type

[**OrganizationCustomRole**](OrganizationCustomRole.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Edit an organization custom role |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_custom_role**
> OrganizationCustomRole get_organization_custom_role(organization_id, custom_role_id)

Get an organization custom role 

Get an organization custom role 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import organization_custom_role_api
from qovery.model.organization_custom_role import OrganizationCustomRole
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
    api_instance = organization_custom_role_api.OrganizationCustomRoleApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    custom_role_id = "customRoleId_example" # str | Custom Role ID

    # example passing only required values which don't have defaults set
    try:
        # Get an organization custom role 
        api_response = api_instance.get_organization_custom_role(organization_id, custom_role_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling OrganizationCustomRoleApi->get_organization_custom_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **custom_role_id** | **str**| Custom Role ID |

### Return type

[**OrganizationCustomRole**](OrganizationCustomRole.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get an organization custom role  |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_organization_custom_roles**
> OrganizationCustomRoleList list_organization_custom_roles(organization_id)

List organization custom roles

List organization custom roles

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import organization_custom_role_api
from qovery.model.organization_custom_role_list import OrganizationCustomRoleList
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
    api_instance = organization_custom_role_api.OrganizationCustomRoleApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID

    # example passing only required values which don't have defaults set
    try:
        # List organization custom roles
        api_response = api_instance.list_organization_custom_roles(organization_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling OrganizationCustomRoleApi->list_organization_custom_roles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |

### Return type

[**OrganizationCustomRoleList**](OrganizationCustomRoleList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List organization custom roles |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

