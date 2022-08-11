# qovery.CloudProviderCredentialsApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_aws_credentials**](CloudProviderCredentialsApi.md#create_aws_credentials) | **POST** /organization/{organizationId}/aws/credentials | Create AWS credentials set
[**create_do_credentials**](CloudProviderCredentialsApi.md#create_do_credentials) | **POST** /organization/{organizationId}/digitalOcean/credentials | Create Digital Ocean credentials set
[**create_scaleway_credentials**](CloudProviderCredentialsApi.md#create_scaleway_credentials) | **POST** /organization/{organizationId}/scaleway/credentials | Create Scaleway credentials set
[**delete_aws_credentials**](CloudProviderCredentialsApi.md#delete_aws_credentials) | **DELETE** /organization/{organizationId}/aws/credentials/{credentialsId} | Delete a set of AWS credentials
[**delete_do_credentials**](CloudProviderCredentialsApi.md#delete_do_credentials) | **DELETE** /organization/{organizationId}/digitalOcean/credentials/{credentialsId} | Delete a set of Digital Ocean credentials
[**delete_scaleway_credentials**](CloudProviderCredentialsApi.md#delete_scaleway_credentials) | **DELETE** /organization/{organizationId}/scaleway/credentials/{credentialsId} | Delete a set of Scaleway credentials
[**edit_aws_credentials**](CloudProviderCredentialsApi.md#edit_aws_credentials) | **PUT** /organization/{organizationId}/aws/credentials/{credentialsId} | Edit a set of AWS credentials
[**edit_do_credentials**](CloudProviderCredentialsApi.md#edit_do_credentials) | **PUT** /organization/{organizationId}/digitalOcean/credentials/{credentialsId} | Edit a set of Digital Ocean credentials
[**edit_scaleway_credentials**](CloudProviderCredentialsApi.md#edit_scaleway_credentials) | **PUT** /organization/{organizationId}/scaleway/credentials/{credentialsId} | Edit a set of Scaleway credentials
[**get_aws_credentials**](CloudProviderCredentialsApi.md#get_aws_credentials) | **GET** /organization/{organizationId}/aws/credentials/{credentialsId} | Get a set of AWS credentials
[**get_do_credentials**](CloudProviderCredentialsApi.md#get_do_credentials) | **GET** /organization/{organizationId}/digitalOcean/credentials/{credentialsId} | Get a set of Digital Ocean credentials
[**get_scaleway_credentials**](CloudProviderCredentialsApi.md#get_scaleway_credentials) | **GET** /organization/{organizationId}/scaleway/credentials/{credentialsId} | Get a set of Scaleway credentials
[**list_aws_credentials**](CloudProviderCredentialsApi.md#list_aws_credentials) | **GET** /organization/{organizationId}/aws/credentials | List AWS credentials
[**list_do_credentials**](CloudProviderCredentialsApi.md#list_do_credentials) | **GET** /organization/{organizationId}/digitalOcean/credentials | List DO credentials
[**list_scaleway_credentials**](CloudProviderCredentialsApi.md#list_scaleway_credentials) | **GET** /organization/{organizationId}/scaleway/credentials | List Scaleway credentials


# **create_aws_credentials**
> ClusterCredentials create_aws_credentials(organization_id)

Create AWS credentials set

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import cloud_provider_credentials_api
from qovery.model.cluster_credentials import ClusterCredentials
from qovery.model.aws_credentials_request import AwsCredentialsRequest
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
    api_instance = cloud_provider_credentials_api.CloudProviderCredentialsApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    aws_credentials_request = AwsCredentialsRequest(
        name="name_example",
        access_key_id="access_key_id_example",
        secret_access_key="secret_access_key_example",
    ) # AwsCredentialsRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create AWS credentials set
        api_response = api_instance.create_aws_credentials(organization_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling CloudProviderCredentialsApi->create_aws_credentials: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create AWS credentials set
        api_response = api_instance.create_aws_credentials(organization_id, aws_credentials_request=aws_credentials_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling CloudProviderCredentialsApi->create_aws_credentials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **aws_credentials_request** | [**AwsCredentialsRequest**](AwsCredentialsRequest.md)|  | [optional]

### Return type

[**ClusterCredentials**](ClusterCredentials.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Credentials created |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_do_credentials**
> ClusterCredentials create_do_credentials(organization_id)

Create Digital Ocean credentials set

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import cloud_provider_credentials_api
from qovery.model.do_credentials_request import DoCredentialsRequest
from qovery.model.cluster_credentials import ClusterCredentials
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
    api_instance = cloud_provider_credentials_api.CloudProviderCredentialsApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    do_credentials_request = DoCredentialsRequest(
        name="name_example",
        token="token_example",
        spaces_access_id="spaces_access_id_example",
        spaces_secret_key="spaces_secret_key_example",
    ) # DoCredentialsRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Digital Ocean credentials set
        api_response = api_instance.create_do_credentials(organization_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling CloudProviderCredentialsApi->create_do_credentials: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Digital Ocean credentials set
        api_response = api_instance.create_do_credentials(organization_id, do_credentials_request=do_credentials_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling CloudProviderCredentialsApi->create_do_credentials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **do_credentials_request** | [**DoCredentialsRequest**](DoCredentialsRequest.md)|  | [optional]

### Return type

[**ClusterCredentials**](ClusterCredentials.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Credentials created |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_scaleway_credentials**
> ClusterCredentials create_scaleway_credentials(organization_id)

Create Scaleway credentials set

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import cloud_provider_credentials_api
from qovery.model.scaleway_credentials_request import ScalewayCredentialsRequest
from qovery.model.cluster_credentials import ClusterCredentials
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
    api_instance = cloud_provider_credentials_api.CloudProviderCredentialsApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    scaleway_credentials_request = ScalewayCredentialsRequest(
        name="name_example",
        scaleway_access_key="scaleway_access_key_example",
        scaleway_secret_key="scaleway_secret_key_example",
        scaleway_project_id="scaleway_project_id_example",
    ) # ScalewayCredentialsRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Scaleway credentials set
        api_response = api_instance.create_scaleway_credentials(organization_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling CloudProviderCredentialsApi->create_scaleway_credentials: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Scaleway credentials set
        api_response = api_instance.create_scaleway_credentials(organization_id, scaleway_credentials_request=scaleway_credentials_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling CloudProviderCredentialsApi->create_scaleway_credentials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **scaleway_credentials_request** | [**ScalewayCredentialsRequest**](ScalewayCredentialsRequest.md)|  | [optional]

### Return type

[**ClusterCredentials**](ClusterCredentials.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Credentials created |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_aws_credentials**
> delete_aws_credentials(credentials_id, organization_id)

Delete a set of AWS credentials

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import cloud_provider_credentials_api
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
    api_instance = cloud_provider_credentials_api.CloudProviderCredentialsApi(api_client)
    credentials_id = "credentialsId_example" # str | Credentials ID
    organization_id = "organizationId_example" # str | Organization ID

    # example passing only required values which don't have defaults set
    try:
        # Delete a set of AWS credentials
        api_instance.delete_aws_credentials(credentials_id, organization_id)
    except qovery.ApiException as e:
        print("Exception when calling CloudProviderCredentialsApi->delete_aws_credentials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **str**| Credentials ID |
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

# **delete_do_credentials**
> delete_do_credentials(credentials_id, organization_id)

Delete a set of Digital Ocean credentials

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import cloud_provider_credentials_api
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
    api_instance = cloud_provider_credentials_api.CloudProviderCredentialsApi(api_client)
    credentials_id = "credentialsId_example" # str | Credentials ID
    organization_id = "organizationId_example" # str | Organization ID

    # example passing only required values which don't have defaults set
    try:
        # Delete a set of Digital Ocean credentials
        api_instance.delete_do_credentials(credentials_id, organization_id)
    except qovery.ApiException as e:
        print("Exception when calling CloudProviderCredentialsApi->delete_do_credentials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **str**| Credentials ID |
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

# **delete_scaleway_credentials**
> delete_scaleway_credentials(credentials_id, organization_id)

Delete a set of Scaleway credentials

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import cloud_provider_credentials_api
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
    api_instance = cloud_provider_credentials_api.CloudProviderCredentialsApi(api_client)
    credentials_id = "credentialsId_example" # str | Credentials ID
    organization_id = "organizationId_example" # str | Organization ID

    # example passing only required values which don't have defaults set
    try:
        # Delete a set of Scaleway credentials
        api_instance.delete_scaleway_credentials(credentials_id, organization_id)
    except qovery.ApiException as e:
        print("Exception when calling CloudProviderCredentialsApi->delete_scaleway_credentials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **str**| Credentials ID |
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

# **edit_aws_credentials**
> ClusterCredentials edit_aws_credentials(organization_id, credentials_id)

Edit a set of AWS credentials

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import cloud_provider_credentials_api
from qovery.model.cluster_credentials import ClusterCredentials
from qovery.model.aws_credentials_request import AwsCredentialsRequest
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
    api_instance = cloud_provider_credentials_api.CloudProviderCredentialsApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    credentials_id = "credentialsId_example" # str | Credentials ID
    aws_credentials_request = AwsCredentialsRequest(
        name="name_example",
        access_key_id="access_key_id_example",
        secret_access_key="secret_access_key_example",
    ) # AwsCredentialsRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Edit a set of AWS credentials
        api_response = api_instance.edit_aws_credentials(organization_id, credentials_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling CloudProviderCredentialsApi->edit_aws_credentials: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit a set of AWS credentials
        api_response = api_instance.edit_aws_credentials(organization_id, credentials_id, aws_credentials_request=aws_credentials_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling CloudProviderCredentialsApi->edit_aws_credentials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **credentials_id** | **str**| Credentials ID |
 **aws_credentials_request** | [**AwsCredentialsRequest**](AwsCredentialsRequest.md)|  | [optional]

### Return type

[**ClusterCredentials**](ClusterCredentials.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Edit a set of AWS credentials |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_do_credentials**
> ClusterCredentials edit_do_credentials(organization_id, credentials_id)

Edit a set of Digital Ocean credentials

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import cloud_provider_credentials_api
from qovery.model.do_credentials_request import DoCredentialsRequest
from qovery.model.cluster_credentials import ClusterCredentials
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
    api_instance = cloud_provider_credentials_api.CloudProviderCredentialsApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    credentials_id = "credentialsId_example" # str | Credentials ID
    do_credentials_request = DoCredentialsRequest(
        name="name_example",
        token="token_example",
        spaces_access_id="spaces_access_id_example",
        spaces_secret_key="spaces_secret_key_example",
    ) # DoCredentialsRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Edit a set of Digital Ocean credentials
        api_response = api_instance.edit_do_credentials(organization_id, credentials_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling CloudProviderCredentialsApi->edit_do_credentials: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit a set of Digital Ocean credentials
        api_response = api_instance.edit_do_credentials(organization_id, credentials_id, do_credentials_request=do_credentials_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling CloudProviderCredentialsApi->edit_do_credentials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **credentials_id** | **str**| Credentials ID |
 **do_credentials_request** | [**DoCredentialsRequest**](DoCredentialsRequest.md)|  | [optional]

### Return type

[**ClusterCredentials**](ClusterCredentials.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Edit a set of Digital Ocean credentials |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_scaleway_credentials**
> ClusterCredentials edit_scaleway_credentials(organization_id, credentials_id)

Edit a set of Scaleway credentials

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import cloud_provider_credentials_api
from qovery.model.scaleway_credentials_request import ScalewayCredentialsRequest
from qovery.model.cluster_credentials import ClusterCredentials
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
    api_instance = cloud_provider_credentials_api.CloudProviderCredentialsApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    credentials_id = "credentialsId_example" # str | Credentials ID
    scaleway_credentials_request = ScalewayCredentialsRequest(
        name="name_example",
        scaleway_access_key="scaleway_access_key_example",
        scaleway_secret_key="scaleway_secret_key_example",
        scaleway_project_id="scaleway_project_id_example",
    ) # ScalewayCredentialsRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Edit a set of Scaleway credentials
        api_response = api_instance.edit_scaleway_credentials(organization_id, credentials_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling CloudProviderCredentialsApi->edit_scaleway_credentials: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit a set of Scaleway credentials
        api_response = api_instance.edit_scaleway_credentials(organization_id, credentials_id, scaleway_credentials_request=scaleway_credentials_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling CloudProviderCredentialsApi->edit_scaleway_credentials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **credentials_id** | **str**| Credentials ID |
 **scaleway_credentials_request** | [**ScalewayCredentialsRequest**](ScalewayCredentialsRequest.md)|  | [optional]

### Return type

[**ClusterCredentials**](ClusterCredentials.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Edit a set of Scaleway credentials |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aws_credentials**
> ClusterCredentials get_aws_credentials(organization_id, credentials_id)

Get a set of AWS credentials

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import cloud_provider_credentials_api
from qovery.model.cluster_credentials import ClusterCredentials
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
    api_instance = cloud_provider_credentials_api.CloudProviderCredentialsApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    credentials_id = "credentialsId_example" # str | Credentials ID

    # example passing only required values which don't have defaults set
    try:
        # Get a set of AWS credentials
        api_response = api_instance.get_aws_credentials(organization_id, credentials_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling CloudProviderCredentialsApi->get_aws_credentials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **credentials_id** | **str**| Credentials ID |

### Return type

[**ClusterCredentials**](ClusterCredentials.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a set of AWS credentials |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_do_credentials**
> ClusterCredentials get_do_credentials(organization_id, credentials_id)

Get a set of Digital Ocean credentials

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import cloud_provider_credentials_api
from qovery.model.cluster_credentials import ClusterCredentials
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
    api_instance = cloud_provider_credentials_api.CloudProviderCredentialsApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    credentials_id = "credentialsId_example" # str | Credentials ID

    # example passing only required values which don't have defaults set
    try:
        # Get a set of Digital Ocean credentials
        api_response = api_instance.get_do_credentials(organization_id, credentials_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling CloudProviderCredentialsApi->get_do_credentials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **credentials_id** | **str**| Credentials ID |

### Return type

[**ClusterCredentials**](ClusterCredentials.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a set of Digital Ocean credentials |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scaleway_credentials**
> ClusterCredentials get_scaleway_credentials(organization_id, credentials_id)

Get a set of Scaleway credentials

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import cloud_provider_credentials_api
from qovery.model.cluster_credentials import ClusterCredentials
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
    api_instance = cloud_provider_credentials_api.CloudProviderCredentialsApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    credentials_id = "credentialsId_example" # str | Credentials ID

    # example passing only required values which don't have defaults set
    try:
        # Get a set of Scaleway credentials
        api_response = api_instance.get_scaleway_credentials(organization_id, credentials_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling CloudProviderCredentialsApi->get_scaleway_credentials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **credentials_id** | **str**| Credentials ID |

### Return type

[**ClusterCredentials**](ClusterCredentials.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get a set of Scaleway credentials |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_aws_credentials**
> ClusterCredentialsResponseList list_aws_credentials(organization_id)

List AWS credentials

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import cloud_provider_credentials_api
from qovery.model.cluster_credentials_response_list import ClusterCredentialsResponseList
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
    api_instance = cloud_provider_credentials_api.CloudProviderCredentialsApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID

    # example passing only required values which don't have defaults set
    try:
        # List AWS credentials
        api_response = api_instance.list_aws_credentials(organization_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling CloudProviderCredentialsApi->list_aws_credentials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |

### Return type

[**ClusterCredentialsResponseList**](ClusterCredentialsResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list credentials |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_do_credentials**
> ClusterCredentialsResponseList list_do_credentials(organization_id)

List DO credentials

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import cloud_provider_credentials_api
from qovery.model.cluster_credentials_response_list import ClusterCredentialsResponseList
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
    api_instance = cloud_provider_credentials_api.CloudProviderCredentialsApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID

    # example passing only required values which don't have defaults set
    try:
        # List DO credentials
        api_response = api_instance.list_do_credentials(organization_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling CloudProviderCredentialsApi->list_do_credentials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |

### Return type

[**ClusterCredentialsResponseList**](ClusterCredentialsResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list credentials |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_scaleway_credentials**
> ClusterCredentialsResponseList list_scaleway_credentials(organization_id)

List Scaleway credentials

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import cloud_provider_credentials_api
from qovery.model.cluster_credentials_response_list import ClusterCredentialsResponseList
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
    api_instance = cloud_provider_credentials_api.CloudProviderCredentialsApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID

    # example passing only required values which don't have defaults set
    try:
        # List Scaleway credentials
        api_response = api_instance.list_scaleway_credentials(organization_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling CloudProviderCredentialsApi->list_scaleway_credentials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |

### Return type

[**ClusterCredentialsResponseList**](ClusterCredentialsResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list credentials |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

