# qovery.GitRepositoriesApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_bitbucket_repositories**](GitRepositoriesApi.md#get_bitbucket_repositories) | **GET** /account/bitbucket/repository | Get bitbucket repositories of the connected user
[**get_bitbucket_repository_branches**](GitRepositoriesApi.md#get_bitbucket_repository_branches) | **GET** /account/bitbucket/repository/branch | Get bitbucket branches of the specified repository
[**get_git_provider_account**](GitRepositoriesApi.md#get_git_provider_account) | **GET** /account/gitAuthProvider | Get git provider accounts
[**get_github_repositories**](GitRepositoriesApi.md#get_github_repositories) | **GET** /account/github/repository | Get github repositories of the connected user
[**get_github_repository_branches**](GitRepositoriesApi.md#get_github_repository_branches) | **GET** /account/github/repository/branch | Get github branches of the specified repository
[**get_gitlab_repositories**](GitRepositoriesApi.md#get_gitlab_repositories) | **GET** /account/gitlab/repository | Get gitlab repositories of the connected user
[**get_gitlab_repository_branches**](GitRepositoriesApi.md#get_gitlab_repository_branches) | **GET** /account/gitlab/repository/branch | Get gitlab branches of the specified repository


# **get_bitbucket_repositories**
> GitRepositoryResponseList get_bitbucket_repositories()

Get bitbucket repositories of the connected user

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import qovery
from qovery.models.git_repository_response_list import GitRepositoryResponseList
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
    api_instance = qovery.GitRepositoriesApi(api_client)

    try:
        # Get bitbucket repositories of the connected user
        api_response = api_instance.get_bitbucket_repositories()
        print("The response of GitRepositoriesApi->get_bitbucket_repositories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GitRepositoriesApi->get_bitbucket_repositories: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**GitRepositoryResponseList**](GitRepositoryResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get bitbucket repositories |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bitbucket_repository_branches**
> GitRepositoryBranchResponseList get_bitbucket_repository_branches(name=name)

Get bitbucket branches of the specified repository

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import qovery
from qovery.models.git_repository_branch_response_list import GitRepositoryBranchResponseList
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
    api_instance = qovery.GitRepositoriesApi(api_client)
    name = 'name_example' # str | The name of the repository where to retrieve the branches (optional)

    try:
        # Get bitbucket branches of the specified repository
        api_response = api_instance.get_bitbucket_repository_branches(name=name)
        print("The response of GitRepositoriesApi->get_bitbucket_repository_branches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GitRepositoriesApi->get_bitbucket_repository_branches: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the repository where to retrieve the branches | [optional] 

### Return type

[**GitRepositoryBranchResponseList**](GitRepositoryBranchResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get bitbucket repository branches |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_git_provider_account**
> GitAuthProviderResponseList get_git_provider_account()

Get git provider accounts

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import qovery
from qovery.models.git_auth_provider_response_list import GitAuthProviderResponseList
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
    api_instance = qovery.GitRepositoriesApi(api_client)

    try:
        # Get git provider accounts
        api_response = api_instance.get_git_provider_account()
        print("The response of GitRepositoriesApi->get_git_provider_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GitRepositoriesApi->get_git_provider_account: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**GitAuthProviderResponseList**](GitAuthProviderResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get account |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_github_repositories**
> GitRepositoryResponseList get_github_repositories()

Get github repositories of the connected user

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import qovery
from qovery.models.git_repository_response_list import GitRepositoryResponseList
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
    api_instance = qovery.GitRepositoriesApi(api_client)

    try:
        # Get github repositories of the connected user
        api_response = api_instance.get_github_repositories()
        print("The response of GitRepositoriesApi->get_github_repositories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GitRepositoriesApi->get_github_repositories: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**GitRepositoryResponseList**](GitRepositoryResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get github repositories |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_github_repository_branches**
> GitRepositoryBranchResponseList get_github_repository_branches(name=name)

Get github branches of the specified repository

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import qovery
from qovery.models.git_repository_branch_response_list import GitRepositoryBranchResponseList
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
    api_instance = qovery.GitRepositoriesApi(api_client)
    name = 'name_example' # str | The name of the repository where to retrieve the branches (optional)

    try:
        # Get github branches of the specified repository
        api_response = api_instance.get_github_repository_branches(name=name)
        print("The response of GitRepositoriesApi->get_github_repository_branches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GitRepositoriesApi->get_github_repository_branches: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the repository where to retrieve the branches | [optional] 

### Return type

[**GitRepositoryBranchResponseList**](GitRepositoryBranchResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get github repository branches |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gitlab_repositories**
> GitRepositoryResponseList get_gitlab_repositories()

Get gitlab repositories of the connected user

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import qovery
from qovery.models.git_repository_response_list import GitRepositoryResponseList
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
    api_instance = qovery.GitRepositoriesApi(api_client)

    try:
        # Get gitlab repositories of the connected user
        api_response = api_instance.get_gitlab_repositories()
        print("The response of GitRepositoriesApi->get_gitlab_repositories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GitRepositoriesApi->get_gitlab_repositories: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**GitRepositoryResponseList**](GitRepositoryResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get gitlab repositories |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gitlab_repository_branches**
> GitRepositoryBranchResponseList get_gitlab_repository_branches(name=name)

Get gitlab branches of the specified repository

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import qovery
from qovery.models.git_repository_branch_response_list import GitRepositoryBranchResponseList
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
    api_instance = qovery.GitRepositoriesApi(api_client)
    name = 'name_example' # str | The name of the repository to retrieve the branches (optional)

    try:
        # Get gitlab branches of the specified repository
        api_response = api_instance.get_gitlab_repository_branches(name=name)
        print("The response of GitRepositoriesApi->get_gitlab_repository_branches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GitRepositoriesApi->get_gitlab_repository_branches: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the repository to retrieve the branches | [optional] 

### Return type

[**GitRepositoryBranchResponseList**](GitRepositoryBranchResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get gitlab repository branches |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

