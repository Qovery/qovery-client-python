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

* Api Key Authentication (ApiKeyAuth):
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
    api_instance = job_configuration_api.JobConfigurationApi(api_client)
    job_id = "jobId_example" # str | Job ID
    job_advanced_settings = JobAdvancedSettings(
        build_timeout_max_sec=1,
        build_cpu_max_in_milli=1,
        build_ram_max_in_gib=1,
        deployment_termination_grace_period_seconds=1,
        deployment_affinity_node_required={
            "key": "key_example",
        },
        job_delete_ttl_seconds_after_finished=1,
        cronjob_concurrency_policy="cronjob_concurrency_policy_example",
        cronjob_failed_jobs_history_limit=1,
        cronjob_success_jobs_history_limit=1,
        security_service_account_name="security_service_account_name_example",
        security_read_only_root_filesystem=True,
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

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

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

Get list and values of the advanced settings of the job. Default values for each setting are available in [our documentation](https://hub.qovery.com/docs/using-qovery/configuration/advanced-settings/) 

### Example

* Api Key Authentication (ApiKeyAuth):
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

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

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

