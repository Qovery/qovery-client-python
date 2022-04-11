# qovery.ProjectMainCallsApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_project**](ProjectMainCallsApi.md#delete_project) | **DELETE** /project/{projectId} | Delete a project
[**edit_project**](ProjectMainCallsApi.md#edit_project) | **PUT** /project/{projectId} | Edit a project
[**get_project**](ProjectMainCallsApi.md#get_project) | **GET** /project/{projectId} | Get project by ID


# **delete_project**
> delete_project(project_id)

Delete a project

To delete a project you must have the admin permission

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import project_main_calls_api
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
    api_instance = project_main_calls_api.ProjectMainCallsApi(api_client)
    project_id = "projectId_example" # str | Project ID

    # example passing only required values which don't have defaults set
    try:
        # Delete a project
        api_instance.delete_project(project_id)
    except qovery.ApiException as e:
        print("Exception when calling ProjectMainCallsApi->delete_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID |

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

# **edit_project**
> Project edit_project(project_id)

Edit a project

To edit a project you must have the admin permission

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import project_main_calls_api
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
    api_instance = project_main_calls_api.ProjectMainCallsApi(api_client)
    project_id = "projectId_example" # str | Project ID
    project_request = ProjectRequest(
        name="name_example",
        description="description_example",
    ) # ProjectRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Edit a project
        api_response = api_instance.edit_project(project_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ProjectMainCallsApi->edit_project: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit a project
        api_response = api_instance.edit_project(project_id, project_request=project_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ProjectMainCallsApi->edit_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID |
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
**200** | Edit a project |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Project name within the organization is already taken |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> Project get_project(project_id)

Get project by ID

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import project_main_calls_api
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
    api_instance = project_main_calls_api.ProjectMainCallsApi(api_client)
    project_id = "projectId_example" # str | Project ID

    # example passing only required values which don't have defaults set
    try:
        # Get project by ID
        api_response = api_instance.get_project(project_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ProjectMainCallsApi->get_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID |

### Return type

[**Project**](Project.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get project by ID |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

