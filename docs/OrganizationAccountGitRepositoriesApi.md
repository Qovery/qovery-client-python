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
> GitRepositoryResponseList get_organization_bitbucket_repositories(organization_id)

Get bitbucket repositories of the connected user

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import organization_account_git_repositories_api
from qovery.model.git_repository_response_list import GitRepositoryResponseList
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
    api_instance = organization_account_git_repositories_api.OrganizationAccountGitRepositoriesApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID

    # example passing only required values which don't have defaults set
    try:
        # Get bitbucket repositories of the connected user
        api_response = api_instance.get_organization_bitbucket_repositories(organization_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling OrganizationAccountGitRepositoriesApi->get_organization_bitbucket_repositories: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |

### Return type

[**GitRepositoryResponseList**](GitRepositoryResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

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
> GitRepositoryBranchResponseList get_organization_bitbucket_repository_branches(organization_id)

Get bitbucket branches of the specified repository

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import organization_account_git_repositories_api
from qovery.model.git_repository_branch_response_list import GitRepositoryBranchResponseList
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
    api_instance = organization_account_git_repositories_api.OrganizationAccountGitRepositoriesApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    name = "name_example" # str | The name of the repository where to retrieve the branches (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get bitbucket branches of the specified repository
        api_response = api_instance.get_organization_bitbucket_repository_branches(organization_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling OrganizationAccountGitRepositoriesApi->get_organization_bitbucket_repository_branches: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get bitbucket branches of the specified repository
        api_response = api_instance.get_organization_bitbucket_repository_branches(organization_id, name=name)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling OrganizationAccountGitRepositoriesApi->get_organization_bitbucket_repository_branches: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **name** | **str**| The name of the repository where to retrieve the branches | [optional]

### Return type

[**GitRepositoryBranchResponseList**](GitRepositoryBranchResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

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

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import organization_account_git_repositories_api
from qovery.model.git_auth_provider_response_list import GitAuthProviderResponseList
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
    api_instance = organization_account_git_repositories_api.OrganizationAccountGitRepositoriesApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID

    # example passing only required values which don't have defaults set
    try:
        # Get git provider accounts
        api_response = api_instance.get_organization_git_provider_account(organization_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling OrganizationAccountGitRepositoriesApi->get_organization_git_provider_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |

### Return type

[**GitAuthProviderResponseList**](GitAuthProviderResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

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
> GitRepositoryResponseList get_organization_github_repositories(organization_id)

Get github repositories of the connected user

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import organization_account_git_repositories_api
from qovery.model.git_repository_response_list import GitRepositoryResponseList
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
    api_instance = organization_account_git_repositories_api.OrganizationAccountGitRepositoriesApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID

    # example passing only required values which don't have defaults set
    try:
        # Get github repositories of the connected user
        api_response = api_instance.get_organization_github_repositories(organization_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling OrganizationAccountGitRepositoriesApi->get_organization_github_repositories: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |

### Return type

[**GitRepositoryResponseList**](GitRepositoryResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

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
> GitRepositoryBranchResponseList get_organization_github_repository_branches(organization_id)

Get github branches of the specified repository

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import organization_account_git_repositories_api
from qovery.model.git_repository_branch_response_list import GitRepositoryBranchResponseList
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
    api_instance = organization_account_git_repositories_api.OrganizationAccountGitRepositoriesApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    name = "name_example" # str | The name of the repository where to retrieve the branches (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get github branches of the specified repository
        api_response = api_instance.get_organization_github_repository_branches(organization_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling OrganizationAccountGitRepositoriesApi->get_organization_github_repository_branches: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get github branches of the specified repository
        api_response = api_instance.get_organization_github_repository_branches(organization_id, name=name)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling OrganizationAccountGitRepositoriesApi->get_organization_github_repository_branches: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **name** | **str**| The name of the repository where to retrieve the branches | [optional]

### Return type

[**GitRepositoryBranchResponseList**](GitRepositoryBranchResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

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
> GitRepositoryResponseList get_organization_gitlab_repositories(organization_id)

Get gitlab repositories of the connected user

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import organization_account_git_repositories_api
from qovery.model.git_repository_response_list import GitRepositoryResponseList
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
    api_instance = organization_account_git_repositories_api.OrganizationAccountGitRepositoriesApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID

    # example passing only required values which don't have defaults set
    try:
        # Get gitlab repositories of the connected user
        api_response = api_instance.get_organization_gitlab_repositories(organization_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling OrganizationAccountGitRepositoriesApi->get_organization_gitlab_repositories: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |

### Return type

[**GitRepositoryResponseList**](GitRepositoryResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

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
> GitRepositoryBranchResponseList get_organization_gitlab_repository_branches(organization_id)

Get gitlab branches of the specified repository

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import organization_account_git_repositories_api
from qovery.model.git_repository_branch_response_list import GitRepositoryBranchResponseList
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
    api_instance = organization_account_git_repositories_api.OrganizationAccountGitRepositoriesApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    name = "name_example" # str | The name of the repository to retrieve the branches (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get gitlab branches of the specified repository
        api_response = api_instance.get_organization_gitlab_repository_branches(organization_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling OrganizationAccountGitRepositoriesApi->get_organization_gitlab_repository_branches: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get gitlab branches of the specified repository
        api_response = api_instance.get_organization_gitlab_repository_branches(organization_id, name=name)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling OrganizationAccountGitRepositoriesApi->get_organization_gitlab_repository_branches: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **name** | **str**| The name of the repository to retrieve the branches | [optional]

### Return type

[**GitRepositoryBranchResponseList**](GitRepositoryBranchResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get gitlab repository branches |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

