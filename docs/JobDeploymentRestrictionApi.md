# qovery.JobDeploymentRestrictionApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_job_deployment_restriction**](JobDeploymentRestrictionApi.md#create_job_deployment_restriction) | **POST** /job/{jobId}/deploymentRestriction | Create a job deployment restriction
[**delete_job_deployment_restriction**](JobDeploymentRestrictionApi.md#delete_job_deployment_restriction) | **DELETE** /job/{jobId}/deploymentRestriction/{deploymentRestrictionId} | Delete a job deployment restriction
[**edit_job_deployment_restriction**](JobDeploymentRestrictionApi.md#edit_job_deployment_restriction) | **PUT** /job/{jobId}/deploymentRestriction/{deploymentRestrictionId} | Edit a job deployment restriction
[**get_job_deployment_restrictions**](JobDeploymentRestrictionApi.md#get_job_deployment_restrictions) | **GET** /job/{jobId}/deploymentRestriction | Get job deployment restrictions


# **create_job_deployment_restriction**
> JobDeploymentRestrictionResponse create_job_deployment_restriction(job_id)

Create a job deployment restriction

Create a job deployment restriction

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import job_deployment_restriction_api
from qovery.model.job_deployment_restriction_request import JobDeploymentRestrictionRequest
from qovery.model.job_deployment_restriction_response import JobDeploymentRestrictionResponse
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
    api_instance = job_deployment_restriction_api.JobDeploymentRestrictionApi(api_client)
    job_id = "jobId_example" # str | Job ID
    job_deployment_restriction_request = JobDeploymentRestrictionRequest(
        mode=DeploymentRestrictionModeEnum("MATCH"),
        type=DeploymentRestrictionTypeEnum("PATH"),
        value="job1/src/",
    ) # JobDeploymentRestrictionRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a job deployment restriction
        api_response = api_instance.create_job_deployment_restriction(job_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling JobDeploymentRestrictionApi->create_job_deployment_restriction: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a job deployment restriction
        api_response = api_instance.create_job_deployment_restriction(job_id, job_deployment_restriction_request=job_deployment_restriction_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling JobDeploymentRestrictionApi->create_job_deployment_restriction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job ID |
 **job_deployment_restriction_request** | [**JobDeploymentRestrictionRequest**](JobDeploymentRestrictionRequest.md)|  | [optional]

### Return type

[**JobDeploymentRestrictionResponse**](JobDeploymentRestrictionResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Added an environment variable |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**409** | A Job deployment restriction with same properties already exists for this job |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_job_deployment_restriction**
> delete_job_deployment_restriction(job_id, deployment_restriction_id)

Delete a job deployment restriction

Delete a job deployment restriction

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import job_deployment_restriction_api
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
    api_instance = job_deployment_restriction_api.JobDeploymentRestrictionApi(api_client)
    job_id = "jobId_example" # str | Job ID
    deployment_restriction_id = "deploymentRestrictionId_example" # str | Deployment Restriction ID

    # example passing only required values which don't have defaults set
    try:
        # Delete a job deployment restriction
        api_instance.delete_job_deployment_restriction(job_id, deployment_restriction_id)
    except qovery.ApiException as e:
        print("Exception when calling JobDeploymentRestrictionApi->delete_job_deployment_restriction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job ID |
 **deployment_restriction_id** | **str**| Deployment Restriction ID |

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

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

# **edit_job_deployment_restriction**
> JobDeploymentRestrictionResponse edit_job_deployment_restriction(job_id, deployment_restriction_id)

Edit a job deployment restriction

Edit a job deployment restriction

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import job_deployment_restriction_api
from qovery.model.job_deployment_restriction_request import JobDeploymentRestrictionRequest
from qovery.model.job_deployment_restriction_response import JobDeploymentRestrictionResponse
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
    api_instance = job_deployment_restriction_api.JobDeploymentRestrictionApi(api_client)
    job_id = "jobId_example" # str | Job ID
    deployment_restriction_id = "deploymentRestrictionId_example" # str | Deployment Restriction ID
    job_deployment_restriction_request = JobDeploymentRestrictionRequest(
        mode=DeploymentRestrictionModeEnum("MATCH"),
        type=DeploymentRestrictionTypeEnum("PATH"),
        value="job1/src/",
    ) # JobDeploymentRestrictionRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Edit a job deployment restriction
        api_response = api_instance.edit_job_deployment_restriction(job_id, deployment_restriction_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling JobDeploymentRestrictionApi->edit_job_deployment_restriction: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit a job deployment restriction
        api_response = api_instance.edit_job_deployment_restriction(job_id, deployment_restriction_id, job_deployment_restriction_request=job_deployment_restriction_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling JobDeploymentRestrictionApi->edit_job_deployment_restriction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job ID |
 **deployment_restriction_id** | **str**| Deployment Restriction ID |
 **job_deployment_restriction_request** | [**JobDeploymentRestrictionRequest**](JobDeploymentRestrictionRequest.md)|  | [optional]

### Return type

[**JobDeploymentRestrictionResponse**](JobDeploymentRestrictionResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Edit a job deployment restriction |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_deployment_restrictions**
> JobDeploymentRestrictionResponseList get_job_deployment_restrictions(job_id)

Get job deployment restrictions

Get job deployment restrictions

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import job_deployment_restriction_api
from qovery.model.job_deployment_restriction_response_list import JobDeploymentRestrictionResponseList
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
    api_instance = job_deployment_restriction_api.JobDeploymentRestrictionApi(api_client)
    job_id = "jobId_example" # str | Job ID

    # example passing only required values which don't have defaults set
    try:
        # Get job deployment restrictions
        api_response = api_instance.get_job_deployment_restrictions(job_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling JobDeploymentRestrictionApi->get_job_deployment_restrictions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job ID |

### Return type

[**JobDeploymentRestrictionResponseList**](JobDeploymentRestrictionResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get job deployment restrictions |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

