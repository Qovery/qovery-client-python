# qovery.JobConfigurationApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edit_job_advanced_settings**](JobConfigurationApi.md#edit_job_advanced_settings) | **PUT** /job/{jobId}/advancedSettings | Edit advanced settings
[**get_job_advanced_settings**](JobConfigurationApi.md#get_job_advanced_settings) | **GET** /job/{jobId}/advancedSettings | Get advanced settings


# **edit_job_advanced_settings**
> JobAdvancedSettings edit_job_advanced_settings(job_id)

Edit advanced settings

Edit advanced settings by returning table of advanced settings.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import job_configuration_api
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = qovery.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with qovery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_configuration_api.JobConfigurationApi(api_client)
    job_id = "jobId_example" # str | Job ID
    job_advanced_settings = JobAdvancedSettings(
        deployment_termination_grace_period_seconds=60,
        job_delete_ttl_seconds_after_finished=1,
        cronjob_concurrency_policy="Forbid",
        cronjob_failed_jobs_history_limit=1,
        cronjob_success_jobs_history_limit=1,
        readiness_probe_type="NONE",
        readiness_probe_http_get_path="",
        readiness_probe_initial_delay_seconds=0,
        readiness_probe_period_seconds=0,
        readiness_probe_timeout_seconds=0,
        readiness_probe_success_threshold=0,
        readiness_probe_failure_threshold=0,
        liveness_probe_type="NONE",
        liveness_probe_http_get_path="",
        liveness_probe_initial_delay_seconds=0,
        liveness_probe_period_seconds=0,
        liveness_probe_timeout_seconds=0,
        liveness_probe_success_threshold=0,
        liveness_probe_failure_threshold=0,
    ) # JobAdvancedSettings |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Edit advanced settings
        api_response = api_instance.edit_job_advanced_settings(job_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling JobConfigurationApi->edit_job_advanced_settings: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit advanced settings
        api_response = api_instance.edit_job_advanced_settings(job_id, job_advanced_settings=job_advanced_settings)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling JobConfigurationApi->edit_job_advanced_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job ID |
 **job_advanced_settings** | [**JobAdvancedSettings**](JobAdvancedSettings.md)|  | [optional]

### Return type

[**JobAdvancedSettings**](JobAdvancedSettings.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Updated advanced settings |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_advanced_settings**
> JobAdvancedSettings get_job_advanced_settings(job_id)

Get advanced settings

Get list and values of the advanced settings of the job.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import job_configuration_api
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = qovery.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with qovery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = job_configuration_api.JobConfigurationApi(api_client)
    job_id = "jobId_example" # str | Job ID

    # example passing only required values which don't have defaults set
    try:
        # Get advanced settings
        api_response = api_instance.get_job_advanced_settings(job_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling JobConfigurationApi->get_job_advanced_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Job ID |

### Return type

[**JobAdvancedSettings**](JobAdvancedSettings.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Advanced settings list |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

