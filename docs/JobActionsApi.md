# qovery.JobActionsApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deploy_job**](JobActionsApi.md#deploy_job) | **POST** /job/{jobId}/deploy | Deploy job
[**restart_job**](JobActionsApi.md#restart_job) | **POST** /job/{jobId}/restart | Deprecated - Restart job
[**stop_job**](JobActionsApi.md#stop_job) | **POST** /job/{jobId}/stop | Stop job


# **deploy_job**
> Status deploy_job(job_id)

Deploy job

You must provide a git commit id or an image tag depending on the source location of your code (git vs image repository).

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import job_actions_api
from qovery.model.job_force_event import JobForceEvent
from qovery.model.job_deploy_request import JobDeployRequest
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
    api_instance = job_actions_api.JobActionsApi(api_client)
    job_id = "jobId_example" # str | Job ID
    force_event = JobForceEvent("START") # JobForceEvent | When filled, it indicates the target event to be deployed.   If the concerned job hasn't the target event provided, the job won't be deployed.  (optional)
    job_deploy_request = JobDeployRequest(
        image_tag="image_tag_example",
        git_commit_id="git_commit_id_example",
    ) # JobDeployRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Deploy job
        api_response = api_instance.deploy_job(job_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling JobActionsApi->deploy_job: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Deploy job
        api_response = api_instance.deploy_job(job_id, force_event=force_event, job_deploy_request=job_deploy_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling JobActionsApi->deploy_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job ID |
 **force_event** | **JobForceEvent**| When filled, it indicates the target event to be deployed.   If the concerned job hasn&#39;t the target event provided, the job won&#39;t be deployed.  | [optional]
 **job_deploy_request** | [**JobDeployRequest**](JobDeployRequest.md)|  | [optional]

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
**202** | Deploy job |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Operation is in progress |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restart_job**
> Status restart_job(job_id)

Deprecated - Restart job

**Deprecated** - Please use the \"Redeploy job\" endpoint now

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import job_actions_api
from qovery.model.job_force_event import JobForceEvent
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
    api_instance = job_actions_api.JobActionsApi(api_client)
    job_id = "jobId_example" # str | Job ID
    force_event = JobForceEvent("START") # JobForceEvent | When filled, it indicates the target event to be deployed.   If the concerned job hasn't the target event provided, the job won't be deployed.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Deprecated - Restart job
        api_response = api_instance.restart_job(job_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling JobActionsApi->restart_job: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Deprecated - Restart job
        api_response = api_instance.restart_job(job_id, force_event=force_event)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling JobActionsApi->restart_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job ID |
 **force_event** | **JobForceEvent**| When filled, it indicates the target event to be deployed.   If the concerned job hasn&#39;t the target event provided, the job won&#39;t be deployed.  | [optional]

### Return type

[**Status**](Status.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Job restart has been requested |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Operation is in progress |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_job**
> Status stop_job(job_id)

Stop job

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import job_actions_api
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
    api_instance = job_actions_api.JobActionsApi(api_client)
    job_id = "jobId_example" # str | Job ID

    # example passing only required values which don't have defaults set
    try:
        # Stop job
        api_response = api_instance.stop_job(job_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling JobActionsApi->stop_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job ID |

### Return type

[**Status**](Status.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Job stop has been requested |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Job is already stopped or an operation is in progress |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

