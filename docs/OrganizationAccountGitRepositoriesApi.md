# qovery.OrganizationAccountGitRepositoriesApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_organization_bitbucket_repositories**](OrganizationAccountGitRepositoriesApi.md#get_organization_bitbucket_repositories) | **GET** /organization/{organizationId}/account/bitbucket/repository | Get bitbucket repositories of the connected user
[**get_organization_bitbucket_repository_branches**](OrganizationAccountGitRepositoriesApi.md#get_organization_bitbucket_repository_branches) | **GET** /organization/{organizationId}/account/bitbucket/repository/branch | Get bitbucket branches of the specified repository
[**get_organization_git_provider_account**](OrganizationAccountGitRepositoriesApi.md#get_organization_git_provider_account) | **GET** /organization/{organizationId}/account/gitAuthProvider | Get git provider accounts
[**get_organization_github_repositories**](OrganizationAccountGitRepositoriesApi.md#get_organization_github_repositories) | **GET** /organization/{organizationId}/account/github/repository | Get github repositories of the connected user
[**get_organization_github_repository_branches**](OrganizationAccountGitRepositoriesApi.md#get_organization_github_repository_branches) | **GET** /organization/{organizationId}/account/github/repository/branch | Get github branches of the specified repository
[**get_organization_gitlab_repositories**](OrganizationAccountGitRepositoriesApi.md#get_organization_gitlab_repositories) | **GET** /organization/{organizationId}/account/gitlab/repository | Get gitlab repositories of the connected user
[**get_organization_gitlab_repository_branches**](OrganizationAccountGitRepositoriesApi.md#get_organization_gitlab_repository_branches) | **GET** /organization/{organizationId}/account/gitlab/repository/branch | Get gitlab branches of the specified repository


# **get_organization_bitbucket_repositories**
> GitRepositoryResponseList get_organization_bitbucket_repositories(organization_id, git_token_id=git_token_id)

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
    api_instance = qovery.OrganizationAccountGitRepositoriesApi(api_client)
    organization_id = 'organization_id_example' # str | Organization ID
    git_token_id = 'git_token_id_example' # str | The git token id that must be used for the application (optional)

    try:
        # Get bitbucket repositories of the connected user
        api_response = api_instance.get_organization_bitbucket_repositories(organization_id, git_token_id=git_token_id)
        print("The response of OrganizationAccountGitRepositoriesApi->get_organization_bitbucket_repositories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationAccountGitRepositoriesApi->get_organization_bitbucket_repositories: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID | 
 **git_token_id** | **str**| The git token id that must be used for the application | [optional] 

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

# **get_organization_bitbucket_repository_branches**
> GitRepositoryBranchResponseList get_organization_bitbucket_repository_branches(organization_id, name=name, git_token_id=git_token_id)

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
    api_instance = qovery.OrganizationAccountGitRepositoriesApi(api_client)
    organization_id = 'organization_id_example' # str | Organization ID
    name = 'name_example' # str | The name of the repository where to retrieve the branches (optional)
    git_token_id = 'git_token_id_example' # str | The git token id that must be used for the application (optional)

    try:
        # Get bitbucket branches of the specified repository
        api_response = api_instance.get_organization_bitbucket_repository_branches(organization_id, name=name, git_token_id=git_token_id)
        print("The response of OrganizationAccountGitRepositoriesApi->get_organization_bitbucket_repository_branches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationAccountGitRepositoriesApi->get_organization_bitbucket_repository_branches: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID | 
 **name** | **str**| The name of the repository where to retrieve the branches | [optional] 
 **git_token_id** | **str**| The git token id that must be used for the application | [optional] 

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

# **get_organization_git_provider_account**
> GitAuthProviderResponseList get_organization_git_provider_account(organization_id)

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
    api_instance = qovery.OrganizationAccountGitRepositoriesApi(api_client)
    organization_id = 'organization_id_example' # str | Organization ID

    try:
        # Get git provider accounts
        api_response = api_instance.get_organization_git_provider_account(organization_id)
        print("The response of OrganizationAccountGitRepositoriesApi->get_organization_git_provider_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationAccountGitRepositoriesApi->get_organization_git_provider_account: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID | 

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

# **get_organization_github_repositories**
> GitRepositoryResponseList get_organization_github_repositories(organization_id, git_token_id=git_token_id)

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
    api_instance = qovery.OrganizationAccountGitRepositoriesApi(api_client)
    organization_id = 'organization_id_example' # str | Organization ID
    git_token_id = 'git_token_id_example' # str | The git token id that must be used for the application (optional)

    try:
        # Get github repositories of the connected user
        api_response = api_instance.get_organization_github_repositories(organization_id, git_token_id=git_token_id)
        print("The response of OrganizationAccountGitRepositoriesApi->get_organization_github_repositories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationAccountGitRepositoriesApi->get_organization_github_repositories: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID | 
 **git_token_id** | **str**| The git token id that must be used for the application | [optional] 

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

# **get_organization_github_repository_branches**
> GitRepositoryBranchResponseList get_organization_github_repository_branches(organization_id, name=name, git_token_id=git_token_id)

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
    api_instance = qovery.OrganizationAccountGitRepositoriesApi(api_client)
    organization_id = 'organization_id_example' # str | Organization ID
    name = 'name_example' # str | The name of the repository where to retrieve the branches (optional)
    git_token_id = 'git_token_id_example' # str | The git token id that must be used for the application (optional)

    try:
        # Get github branches of the specified repository
        api_response = api_instance.get_organization_github_repository_branches(organization_id, name=name, git_token_id=git_token_id)
        print("The response of OrganizationAccountGitRepositoriesApi->get_organization_github_repository_branches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationAccountGitRepositoriesApi->get_organization_github_repository_branches: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID | 
 **name** | **str**| The name of the repository where to retrieve the branches | [optional] 
 **git_token_id** | **str**| The git token id that must be used for the application | [optional] 

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

# **get_organization_gitlab_repositories**
> GitRepositoryResponseList get_organization_gitlab_repositories(organization_id, git_token_id=git_token_id)

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
    api_instance = qovery.OrganizationAccountGitRepositoriesApi(api_client)
    organization_id = 'organization_id_example' # str | Organization ID
    git_token_id = 'git_token_id_example' # str | The git token id that must be used for the application (optional)

    try:
        # Get gitlab repositories of the connected user
        api_response = api_instance.get_organization_gitlab_repositories(organization_id, git_token_id=git_token_id)
        print("The response of OrganizationAccountGitRepositoriesApi->get_organization_gitlab_repositories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationAccountGitRepositoriesApi->get_organization_gitlab_repositories: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID | 
 **git_token_id** | **str**| The git token id that must be used for the application | [optional] 

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

# **get_organization_gitlab_repository_branches**
> GitRepositoryBranchResponseList get_organization_gitlab_repository_branches(organization_id, name=name, git_token_id=git_token_id)

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
    api_instance = qovery.OrganizationAccountGitRepositoriesApi(api_client)
    organization_id = 'organization_id_example' # str | Organization ID
    name = 'name_example' # str | The name of the repository to retrieve the branches (optional)
    git_token_id = 'git_token_id_example' # str | The git token id that must be used for the application (optional)

    try:
        # Get gitlab branches of the specified repository
        api_response = api_instance.get_organization_gitlab_repository_branches(organization_id, name=name, git_token_id=git_token_id)
        print("The response of OrganizationAccountGitRepositoriesApi->get_organization_gitlab_repository_branches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationAccountGitRepositoriesApi->get_organization_gitlab_repository_branches: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID | 
 **name** | **str**| The name of the repository to retrieve the branches | [optional] 
 **git_token_id** | **str**| The git token id that must be used for the application | [optional] 

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

