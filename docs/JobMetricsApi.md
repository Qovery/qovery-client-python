# qovery.JobMetricsApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_job_current_instance**](JobMetricsApi.md#get_job_current_instance) | **GET** /job/{jobId}/instance | List currently running instances of the job with their CPU and RAM metrics


# **get_job_current_instance**
> InstanceResponseList get_job_current_instance()

List currently running instances of the job with their CPU and RAM metrics

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import job_metrics_api
from qovery.model.instance_response_list import InstanceResponseList
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
    api_instance = job_metrics_api.JobMetricsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List currently running instances of the job with their CPU and RAM metrics
        api_response = api_instance.get_job_current_instance()
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling JobMetricsApi->get_job_current_instance: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**InstanceResponseList**](InstanceResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Know current resource consumption of the job for each running instance |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

