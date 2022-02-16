# qovery.ApplicationMainCallsApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_application_tag**](ApplicationMainCallsApi.md#create_application_tag) | **POST** /application/{applicationId}/tag | Add application tag
[**delete_application**](ApplicationMainCallsApi.md#delete_application) | **DELETE** /application/{applicationId} | Delete application
[**delete_application_tag**](ApplicationMainCallsApi.md#delete_application_tag) | **DELETE** /application/{applicationId}/tag/{tagId} | Delete application tag
[**edit_application**](ApplicationMainCallsApi.md#edit_application) | **PUT** /application/{applicationId} | Edit application
[**get_application**](ApplicationMainCallsApi.md#get_application) | **GET** /application/{applicationId} | Get application by ID
[**get_application_status**](ApplicationMainCallsApi.md#get_application_status) | **GET** /application/{applicationId}/status | Get application status
[**list_application_commit**](ApplicationMainCallsApi.md#list_application_commit) | **GET** /application/{applicationId}/commit | List last commits
[**list_application_contributor**](ApplicationMainCallsApi.md#list_application_contributor) | **GET** /application/{applicationId}/contributor | List contributors
[**list_application_links**](ApplicationMainCallsApi.md#list_application_links) | **GET** /application/{applicationId}/link | List all URLs of the application
[**list_application_tag**](ApplicationMainCallsApi.md#list_application_tag) | **GET** /application/{applicationId}/tag | List tags


# **create_application_tag**
> TagResponseList create_application_tag(application_id)

Add application tag

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from api import application_main_calls_api
from qovery.model.tag_request import TagRequest
from qovery.model.tag_response_list import TagResponseList
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
    api_instance = application_main_calls_api.ApplicationMainCallsApi(api_client)
    application_id = "applicationId_example" # str | Application ID
    tag_request = TagRequest(
        name="name_example",
    ) # TagRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add application tag
        api_response = api_instance.create_application_tag(application_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationMainCallsApi->create_application_tag: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add application tag
        api_response = api_instance.create_application_tag(application_id, tag_request=tag_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationMainCallsApi->create_application_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID |
 **tag_request** | [**TagRequest**](TagRequest.md)|  | [optional]

### Return type

[**TagResponseList**](TagResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create application |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_application**
> delete_application(application_id)

Delete application

To delete the application you must have the admin permission

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from api import application_main_calls_api
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
    api_instance = application_main_calls_api.ApplicationMainCallsApi(api_client)
    application_id = "applicationId_example" # str | Application ID

    # example passing only required values which don't have defaults set
    try:
        # Delete application
        api_instance.delete_application(application_id)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationMainCallsApi->delete_application: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID |

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

# **delete_application_tag**
> delete_application_tag(application_id, tag_id)

Delete application tag

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from api import application_main_calls_api
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
    api_instance = application_main_calls_api.ApplicationMainCallsApi(api_client)
    application_id = "applicationId_example" # str | Application ID
    tag_id = "tagId_example" # str | Tag ID

    # example passing only required values which don't have defaults set
    try:
        # Delete application tag
        api_instance.delete_application_tag(application_id, tag_id)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationMainCallsApi->delete_application_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID |
 **tag_id** | **str**| Tag ID |

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

# **edit_application**
> ApplicationResponse edit_application(application_id)

Edit application

- To edit the application you must have the admin permission. - For port edition, if you provide a port id, we will update the corresponding port. If you don't we will create a new one. If you remove a port from the payload, we will delete it. - For storage edition, if you provide a storage id, we will update the corresponding storage. If you don't we will create a new one. If you remove a storage from the payload, we will delete it. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from api import application_main_calls_api
from qovery.model.application_edit_request import ApplicationEditRequest
from qovery.model.application_response import ApplicationResponse
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
    api_instance = application_main_calls_api.ApplicationMainCallsApi(api_client)
    application_id = "applicationId_example" # str | Application ID
    application_edit_request = ApplicationEditRequest(
        name="name_example",
        description="description_example",
        git_repository=ApplicationGitRepositoryRequest(
            url="https://github.com/Qovery/simple-node-app",
            branch="feat/text_xxx",
            root_path="/",
        ),
        build_mode="DOCKER",
        dockerfile_path="dockerfile_path_example",
        buildpack_language="GO",
        cpu=1250,
        memory=1024,
        min_running_instances=1,
        max_running_instances=1,
        healthcheck=Healthcheck(
            protocol="TCP",
            value="value_example",
        ),
        auto_preview=True,
        sticky_session=False,
    ) # ApplicationEditRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Edit application
        api_response = api_instance.edit_application(application_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationMainCallsApi->edit_application: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit application
        api_response = api_instance.edit_application(application_id, application_edit_request=application_edit_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationMainCallsApi->edit_application: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID |
 **application_edit_request** | [**ApplicationEditRequest**](ApplicationEditRequest.md)|  | [optional]

### Return type

[**ApplicationResponse**](ApplicationResponse.md)

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
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Application name within the environment is already taken |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application**
> ApplicationResponse get_application(application_id)

Get application by ID

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from api import application_main_calls_api
from qovery.model.application_response import ApplicationResponse
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
    api_instance = application_main_calls_api.ApplicationMainCallsApi(api_client)
    application_id = "applicationId_example" # str | Application ID

    # example passing only required values which don't have defaults set
    try:
        # Get application by ID
        api_response = api_instance.get_application(application_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationMainCallsApi->get_application: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID |

### Return type

[**ApplicationResponse**](ApplicationResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get application by ID |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_status**
> Status get_application_status(application_id)

Get application status

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from api import application_main_calls_api
from qovery.model.status import Status
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
    api_instance = application_main_calls_api.ApplicationMainCallsApi(api_client)
    application_id = "applicationId_example" # str | Application ID

    # example passing only required values which don't have defaults set
    try:
        # Get application status
        api_response = api_instance.get_application_status(application_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationMainCallsApi->get_application_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID |

### Return type

[**Status**](Status.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get status |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_application_commit**
> CommitResponseList list_application_commit(application_id)

List last commits

Returns list of the last 100 commits made on the repository linked to the application

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from api import application_main_calls_api
from qovery.model.commit_response_list import CommitResponseList
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
    api_instance = application_main_calls_api.ApplicationMainCallsApi(api_client)
    application_id = "applicationId_example" # str | Application ID
    start_id = "startId_example" # str | Starting point after which to return results (optional)
    git_commit_id = "gitCommitId_example" # str | Git Commit ID (optional)

    # example passing only required values which don't have defaults set
    try:
        # List last commits
        api_response = api_instance.list_application_commit(application_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationMainCallsApi->list_application_commit: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List last commits
        api_response = api_instance.list_application_commit(application_id, start_id=start_id, git_commit_id=git_commit_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationMainCallsApi->list_application_commit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID |
 **start_id** | **str**| Starting point after which to return results | [optional]
 **git_commit_id** | **str**| Git Commit ID | [optional]

### Return type

[**CommitResponseList**](CommitResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List commits |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_application_contributor**
> UserResponseList list_application_contributor(application_id)

List contributors

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from api import application_main_calls_api
from qovery.model.user_response_list import UserResponseList
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
    api_instance = application_main_calls_api.ApplicationMainCallsApi(api_client)
    application_id = "applicationId_example" # str | Application ID

    # example passing only required values which don't have defaults set
    try:
        # List contributors
        api_response = api_instance.list_application_contributor(application_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationMainCallsApi->list_application_contributor: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID |

### Return type

[**UserResponseList**](UserResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List application contributors |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_application_links**
> LinkResponseList list_application_links(application_id)

List all URLs of the application

This will return all the custom domains and Qovery autogenerated domain for the given application

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from api import application_main_calls_api
from qovery.model.link_response_list import LinkResponseList
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
    api_instance = application_main_calls_api.ApplicationMainCallsApi(api_client)
    application_id = "applicationId_example" # str | Application ID

    # example passing only required values which don't have defaults set
    try:
        # List all URLs of the application
        api_response = api_instance.list_application_links(application_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationMainCallsApi->list_application_links: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID |

### Return type

[**LinkResponseList**](LinkResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List links |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_application_tag**
> TagResponseList list_application_tag(application_id)

List tags

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from api import application_main_calls_api
from qovery.model.tag_response_list import TagResponseList
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
    api_instance = application_main_calls_api.ApplicationMainCallsApi(api_client)
    application_id = "applicationId_example" # str | Application ID

    # example passing only required values which don't have defaults set
    try:
        # List tags
        api_response = api_instance.list_application_tag(application_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationMainCallsApi->list_application_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID |

### Return type

[**TagResponseList**](TagResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List application tags |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

