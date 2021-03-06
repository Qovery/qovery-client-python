# qovery.ProjectsApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project**](ProjectsApi.md#create_project) | **POST** /organization/{organizationId}/project | Create a project
[**get_organization_project_stats**](ProjectsApi.md#get_organization_project_stats) | **GET** /organization/{organizationId}/project/stats | List total number of services and environments for each project of the organization
[**list_project**](ProjectsApi.md#list_project) | **GET** /organization/{organizationId}/project | List projects


# **create_project**
> Project create_project(organization_id)

Create a project

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import projects_api
from qovery.model.project_request import ProjectRequest
from qovery.model.project import Project
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
    api_instance = projects_api.ProjectsApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    project_request = ProjectRequest(
        name="name_example",
        description="description_example",
    ) # ProjectRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a project
        api_response = api_instance.create_project(organization_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ProjectsApi->create_project: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a project
        api_response = api_instance.create_project(organization_id, project_request=project_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ProjectsApi->create_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **project_request** | [**ProjectRequest**](ProjectRequest.md)|  | [optional]

### Return type

[**Project**](Project.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Create project |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Project name within the organization is already taken |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_project_stats**
> ProjectStatsResponseList get_organization_project_stats(organization_id)

List total number of services and environments for each project of the organization

Returns a list of project ids, and for each its total numberof services and environments

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import projects_api
from qovery.model.project_stats_response_list import ProjectStatsResponseList
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
    api_instance = projects_api.ProjectsApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID

    # example passing only required values which don't have defaults set
    try:
        # List total number of services and environments for each project of the organization
        api_response = api_instance.get_organization_project_stats(organization_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ProjectsApi->get_organization_project_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |

### Return type

[**ProjectStatsResponseList**](ProjectStatsResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get number of services |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_project**
> ProjectResponseList list_project(organization_id)

List projects

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import projects_api
from qovery.model.project_response_list import ProjectResponseList
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
    api_instance = projects_api.ProjectsApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID

    # example passing only required values which don't have defaults set
    try:
        # List projects
        api_response = api_instance.list_project(organization_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ProjectsApi->list_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |

### Return type

[**ProjectResponseList**](ProjectResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List projects |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

