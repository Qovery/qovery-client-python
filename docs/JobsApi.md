# qovery.JobsApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auto_deploy_job_environments**](JobsApi.md#auto_deploy_job_environments) | **POST** /organization/{organizationId}/job/deploy | Auto deploy jobs
[**clone_job**](JobsApi.md#clone_job) | **POST** /job/{jobId}/clone | Clone job
[**create_job**](JobsApi.md#create_job) | **POST** /environment/{environmentId}/job | Create a job
[**get_default_job_advanced_settings**](JobsApi.md#get_default_job_advanced_settings) | **GET** /defaultJobAdvancedSettings | List default job advanced settings
[**get_environment_job_status**](JobsApi.md#get_environment_job_status) | **GET** /environment/{environmentId}/job/status | List all environment job statuses
[**list_jobs**](JobsApi.md#list_jobs) | **GET** /environment/{environmentId}/job | List jobs


# **auto_deploy_job_environments**
> Status auto_deploy_job_environments(organization_id)

Auto deploy jobs

Triggers a new job deploy in each environment matching the following conditions - environment should have the auto-deploy enabled - the job should have the same image name and a different tag 

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import jobs_api
from qovery.model.organization_job_auto_deploy_request import OrganizationJobAutoDeployRequest
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

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = qovery.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with qovery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jobs_api.JobsApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    organization_job_auto_deploy_request = OrganizationJobAutoDeployRequest(
        image_name="image_name_example",
        tag="tag_example",
    ) # OrganizationJobAutoDeployRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Auto deploy jobs
        api_response = api_instance.auto_deploy_job_environments(organization_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling JobsApi->auto_deploy_job_environments: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Auto deploy jobs
        api_response = api_instance.auto_deploy_job_environments(organization_id, organization_job_auto_deploy_request=organization_job_auto_deploy_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling JobsApi->auto_deploy_job_environments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **organization_job_auto_deploy_request** | [**OrganizationJobAutoDeployRequest**](OrganizationJobAutoDeployRequest.md)|  | [optional]

### Return type

[**Status**](Status.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Deployed jobs |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Operation is in progress |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clone_job**
> JobResponse clone_job(job_id)

Clone job

This will create a new job with the same configuration on the targeted environment Id.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import jobs_api
from qovery.model.clone_job_request import CloneJobRequest
from qovery.model.job_response import JobResponse
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
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = qovery.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with qovery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jobs_api.JobsApi(api_client)
    job_id = "jobId_example" # str | Job ID
    clone_job_request = CloneJobRequest(
        name="name_example",
        environment_id="environment_id_example",
    ) # CloneJobRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Clone job
        api_response = api_instance.clone_job(job_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling JobsApi->clone_job: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Clone job
        api_response = api_instance.clone_job(job_id, clone_job_request=clone_job_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling JobsApi->clone_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job ID |
 **clone_job_request** | [**CloneJobRequest**](CloneJobRequest.md)|  | [optional]

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Job clone has been requested |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Operation is in progress |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_job**
> JobResponse create_job(environment_id)

Create a job

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import jobs_api
from qovery.model.job_request import JobRequest
from qovery.model.job_response import JobResponse
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
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = qovery.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with qovery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jobs_api.JobsApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID
    job_request = JobRequest(None) # JobRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a job
        api_response = api_instance.create_job(environment_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling JobsApi->create_job: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a job
        api_response = api_instance.create_job(environment_id, job_request=job_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling JobsApi->create_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID |
 **job_request** | [**JobRequest**](JobRequest.md)|  | [optional]

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create job |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Job name within the environment is already taken |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_default_job_advanced_settings**
> JobAdvancedSettings get_default_job_advanced_settings()

List default job advanced settings

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import jobs_api
from qovery.model.job_advanced_settings import JobAdvancedSettings
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
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = qovery.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with qovery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jobs_api.JobsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List default job advanced settings
        api_response = api_instance.get_default_job_advanced_settings()
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling JobsApi->get_default_job_advanced_settings: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**JobAdvancedSettings**](JobAdvancedSettings.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default job advanced settings |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_environment_job_status**
> ReferenceObjectStatusResponseList get_environment_job_status(environment_id)

List all environment job statuses

Returns a list of jobs with only their id and status.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import jobs_api
from qovery.model.reference_object_status_response_list import ReferenceObjectStatusResponseList
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
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = qovery.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with qovery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jobs_api.JobsApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID

    # example passing only required values which don't have defaults set
    try:
        # List all environment job statuses
        api_response = api_instance.get_environment_job_status(environment_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling JobsApi->get_environment_job_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID |

### Return type

[**ReferenceObjectStatusResponseList**](ReferenceObjectStatusResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

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

# **list_jobs**
> JobResponseList list_jobs(environment_id)

List jobs

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import jobs_api
from qovery.model.job_response_list import JobResponseList
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
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = qovery.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with qovery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jobs_api.JobsApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID
    to_update = False # bool | return (or not) results that must be updated (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # List jobs
        api_response = api_instance.list_jobs(environment_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling JobsApi->list_jobs: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List jobs
        api_response = api_instance.list_jobs(environment_id, to_update=to_update)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling JobsApi->list_jobs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID |
 **to_update** | **bool**| return (or not) results that must be updated | [optional] if omitted the server will use the default value of False

### Return type

[**JobResponseList**](JobResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List jobs |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

