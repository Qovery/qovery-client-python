# qovery.ApplicationMetricsApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_application_current_instance**](ApplicationMetricsApi.md#get_application_current_instance) | **GET** /application/{applicationId}/instance | List currently running instances of the application with their CPU and RAM metrics
[**get_application_current_scale**](ApplicationMetricsApi.md#get_application_current_scale) | **GET** /application/{applicationId}/currentScale | Get current scaling of the application
[**get_application_current_storage_disk**](ApplicationMetricsApi.md#get_application_current_storage_disk) | **GET** /application/{applicationId}/currentStorage | List current storage disk usage
[**get_application_metric_cpu**](ApplicationMetricsApi.md#get_application_metric_cpu) | **GET** /application/{applicationId}/metric/cpu | Get CPU consumption metric over time for the application
[**get_application_metric_health_check**](ApplicationMetricsApi.md#get_application_metric_health_check) | **GET** /application/{applicationId}/metric/healthCheck | Get Health Check latency  metric over time for the application
[**get_application_metric_memory**](ApplicationMetricsApi.md#get_application_metric_memory) | **GET** /application/{applicationId}/metric/memory | Get Memory consumption metric over time for the application
[**get_application_metric_storage**](ApplicationMetricsApi.md#get_application_metric_storage) | **GET** /application/{applicationId}/metric/storage | Get Storage consumption metric over time for the application


# **get_application_current_instance**
> InstanceResponseList get_application_current_instance(application_id)

List currently running instances of the application with their CPU and RAM metrics

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import application_metrics_api
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
    api_instance = application_metrics_api.ApplicationMetricsApi(api_client)
    application_id = "applicationId_example" # str | Application ID

    # example passing only required values which don't have defaults set
    try:
        # List currently running instances of the application with their CPU and RAM metrics
        api_response = api_instance.get_application_current_instance(application_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationMetricsApi->get_application_current_instance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID |

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
**200** | Know current resource consumption of the application for each running instance |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_current_scale**
> ApplicationCurrentScale get_application_current_scale(application_id)

Get current scaling of the application

Returns min, max, and running number of instances of the application

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import application_metrics_api
from qovery.model.application_current_scale import ApplicationCurrentScale
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
    api_instance = application_metrics_api.ApplicationMetricsApi(api_client)
    application_id = "applicationId_example" # str | Application ID

    # example passing only required values which don't have defaults set
    try:
        # Get current scaling of the application
        api_response = api_instance.get_application_current_scale(application_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationMetricsApi->get_application_current_scale: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID |

### Return type

[**ApplicationCurrentScale**](ApplicationCurrentScale.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get current scaling of the application |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_current_storage_disk**
> StorageDiskResponseList get_application_current_storage_disk(application_id)

List current storage disk usage

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import application_metrics_api
from qovery.model.storage_disk_response_list import StorageDiskResponseList
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
    api_instance = application_metrics_api.ApplicationMetricsApi(api_client)
    application_id = "applicationId_example" # str | Application ID

    # example passing only required values which don't have defaults set
    try:
        # List current storage disk usage
        api_response = api_instance.get_application_current_storage_disk(application_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationMetricsApi->get_application_current_storage_disk: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID |

### Return type

[**StorageDiskResponseList**](StorageDiskResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Know current storage disk |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_metric_cpu**
> MetricCPUResponseList get_application_metric_cpu(application_id, last_seconds)

Get CPU consumption metric over time for the application

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import application_metrics_api
from qovery.model.metric_cpu_response_list import MetricCPUResponseList
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
    api_instance = application_metrics_api.ApplicationMetricsApi(api_client)
    application_id = "applicationId_example" # str | Application ID
    last_seconds = 3.14 # float | Up to how many seconds in the past to ask analytics results

    # example passing only required values which don't have defaults set
    try:
        # Get CPU consumption metric over time for the application
        api_response = api_instance.get_application_metric_cpu(application_id, last_seconds)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationMetricsApi->get_application_metric_cpu: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID |
 **last_seconds** | **float**| Up to how many seconds in the past to ask analytics results |

### Return type

[**MetricCPUResponseList**](MetricCPUResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | CPU consumption |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_metric_health_check**
> MetricGenericResponseList get_application_metric_health_check(application_id, last_seconds)

Get Health Check latency  metric over time for the application

The value returned corresponds to the 95th centile

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import application_metrics_api
from qovery.model.metric_generic_response_list import MetricGenericResponseList
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
    api_instance = application_metrics_api.ApplicationMetricsApi(api_client)
    application_id = "applicationId_example" # str | Application ID
    last_seconds = 3.14 # float | Up to how many seconds in the past to ask analytics results

    # example passing only required values which don't have defaults set
    try:
        # Get Health Check latency  metric over time for the application
        api_response = api_instance.get_application_metric_health_check(application_id, last_seconds)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationMetricsApi->get_application_metric_health_check: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID |
 **last_seconds** | **float**| Up to how many seconds in the past to ask analytics results |

### Return type

[**MetricGenericResponseList**](MetricGenericResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Health Check Latency |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_metric_memory**
> MetricMemoryResponseList get_application_metric_memory(application_id, last_seconds)

Get Memory consumption metric over time for the application

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import application_metrics_api
from qovery.model.metric_memory_response_list import MetricMemoryResponseList
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
    api_instance = application_metrics_api.ApplicationMetricsApi(api_client)
    application_id = "applicationId_example" # str | Application ID
    last_seconds = 3.14 # float | Up to how many seconds in the past to ask analytics results

    # example passing only required values which don't have defaults set
    try:
        # Get Memory consumption metric over time for the application
        api_response = api_instance.get_application_metric_memory(application_id, last_seconds)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationMetricsApi->get_application_metric_memory: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID |
 **last_seconds** | **float**| Up to how many seconds in the past to ask analytics results |

### Return type

[**MetricMemoryResponseList**](MetricMemoryResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Memory consumption |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_metric_storage**
> MetricStorageResponseList get_application_metric_storage(application_id, last_seconds)

Get Storage consumption metric over time for the application

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import application_metrics_api
from qovery.model.metric_storage_response_list import MetricStorageResponseList
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
    api_instance = application_metrics_api.ApplicationMetricsApi(api_client)
    application_id = "applicationId_example" # str | Application ID
    last_seconds = 3.14 # float | Up to how many seconds in the past to ask analytics results

    # example passing only required values which don't have defaults set
    try:
        # Get Storage consumption metric over time for the application
        api_response = api_instance.get_application_metric_storage(application_id, last_seconds)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationMetricsApi->get_application_metric_storage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID |
 **last_seconds** | **float**| Up to how many seconds in the past to ask analytics results |

### Return type

[**MetricStorageResponseList**](MetricStorageResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Storage consumption |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

