# qovery.ContainerMetricsApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_container_current_instance**](ContainerMetricsApi.md#get_container_current_instance) | **GET** /container/{containerId}/instance | NOT YET IMPLEMENTED - List currently running instances of the container with their CPU and RAM metrics
[**get_container_current_scale**](ContainerMetricsApi.md#get_container_current_scale) | **GET** /container/{containerId}/currentScale | NOT YET IMPLEMENTED - Get current scaling of the container
[**get_container_current_storage_disk**](ContainerMetricsApi.md#get_container_current_storage_disk) | **GET** /container/{containerId}/currentStorage | NOT YET IMPLEMENTED - List current storage disk usage
[**get_container_metric_cpu**](ContainerMetricsApi.md#get_container_metric_cpu) | **GET** /container/{containerId}/metric/cpu | NOT YET IMPLEMENTED - Get CPU consumption metric over time for the container
[**get_container_metric_health_check**](ContainerMetricsApi.md#get_container_metric_health_check) | **GET** /container/{containerId}/metric/healthCheck | NOT YET IMPLEMENTED - Get Health Check latency  metric over time for the container
[**get_container_metric_memory**](ContainerMetricsApi.md#get_container_metric_memory) | **GET** /container/{containerId}/metric/memory | NOT YET IMPLEMENTED - Get Memory consumption metric over time for the container
[**get_container_metric_restart**](ContainerMetricsApi.md#get_container_metric_restart) | **GET** /container/{containerId}/metric/restart | NOT YET IMPLEMENTED - List container restarts
[**get_container_metric_storage**](ContainerMetricsApi.md#get_container_metric_storage) | **GET** /container/{containerId}/metric/storage | NOT YET IMPLEMENTED - Get Storage consumption metric over time for the container 


# **get_container_current_instance**
> InstanceResponseList get_container_current_instance(container_id)

NOT YET IMPLEMENTED - List currently running instances of the container with their CPU and RAM metrics

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import container_metrics_api
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
    api_instance = container_metrics_api.ContainerMetricsApi(api_client)
    container_id = "containerId_example" # str | Container ID

    # example passing only required values which don't have defaults set
    try:
        # NOT YET IMPLEMENTED - List currently running instances of the container with their CPU and RAM metrics
        api_response = api_instance.get_container_current_instance(container_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainerMetricsApi->get_container_current_instance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Container ID |

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
**200** | Know current resource consumption of the container for each running instance |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_container_current_scale**
> ContainerCurrentScale get_container_current_scale(container_id)

NOT YET IMPLEMENTED - Get current scaling of the container

Returns min, max, and running number of instances of the application

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import container_metrics_api
from qovery.model.container_current_scale import ContainerCurrentScale
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
    api_instance = container_metrics_api.ContainerMetricsApi(api_client)
    container_id = "containerId_example" # str | Container ID

    # example passing only required values which don't have defaults set
    try:
        # NOT YET IMPLEMENTED - Get current scaling of the container
        api_response = api_instance.get_container_current_scale(container_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainerMetricsApi->get_container_current_scale: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Container ID |

### Return type

[**ContainerCurrentScale**](ContainerCurrentScale.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get current scaling of the container |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_container_current_storage_disk**
> StorageDiskResponseList get_container_current_storage_disk(container_id)

NOT YET IMPLEMENTED - List current storage disk usage

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import container_metrics_api
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
    api_instance = container_metrics_api.ContainerMetricsApi(api_client)
    container_id = "containerId_example" # str | Container ID

    # example passing only required values which don't have defaults set
    try:
        # NOT YET IMPLEMENTED - List current storage disk usage
        api_response = api_instance.get_container_current_storage_disk(container_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainerMetricsApi->get_container_current_storage_disk: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Container ID |

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

# **get_container_metric_cpu**
> MetricCPUResponseList get_container_metric_cpu(container_id, last_seconds)

NOT YET IMPLEMENTED - Get CPU consumption metric over time for the container

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import container_metrics_api
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
    api_instance = container_metrics_api.ContainerMetricsApi(api_client)
    container_id = "containerId_example" # str | Container ID
    last_seconds = 3.14 # float | Up to how many seconds in the past to ask analytics results

    # example passing only required values which don't have defaults set
    try:
        # NOT YET IMPLEMENTED - Get CPU consumption metric over time for the container
        api_response = api_instance.get_container_metric_cpu(container_id, last_seconds)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainerMetricsApi->get_container_metric_cpu: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Container ID |
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

# **get_container_metric_health_check**
> MetricGenericResponseList get_container_metric_health_check(container_id, last_seconds)

NOT YET IMPLEMENTED - Get Health Check latency  metric over time for the container

The value returned corresponds to the 95th centile

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import container_metrics_api
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
    api_instance = container_metrics_api.ContainerMetricsApi(api_client)
    container_id = "containerId_example" # str | Container ID
    last_seconds = 3.14 # float | Up to how many seconds in the past to ask analytics results

    # example passing only required values which don't have defaults set
    try:
        # NOT YET IMPLEMENTED - Get Health Check latency  metric over time for the container
        api_response = api_instance.get_container_metric_health_check(container_id, last_seconds)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainerMetricsApi->get_container_metric_health_check: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Container ID |
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

# **get_container_metric_memory**
> MetricMemoryResponseList get_container_metric_memory(container_id, last_seconds)

NOT YET IMPLEMENTED - Get Memory consumption metric over time for the container

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import container_metrics_api
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
    api_instance = container_metrics_api.ContainerMetricsApi(api_client)
    container_id = "containerId_example" # str | Container ID
    last_seconds = 3.14 # float | Up to how many seconds in the past to ask analytics results

    # example passing only required values which don't have defaults set
    try:
        # NOT YET IMPLEMENTED - Get Memory consumption metric over time for the container
        api_response = api_instance.get_container_metric_memory(container_id, last_seconds)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainerMetricsApi->get_container_metric_memory: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Container ID |
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

# **get_container_metric_restart**
> MetricRestart get_container_metric_restart(container_id, last_seconds)

NOT YET IMPLEMENTED - List container restarts

Get container restart message and timestamp.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import container_metrics_api
from qovery.model.metric_restart import MetricRestart
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
    api_instance = container_metrics_api.ContainerMetricsApi(api_client)
    container_id = "containerId_example" # str | Container ID
    last_seconds = 3.14 # float | Up to how many seconds in the past to ask analytics results

    # example passing only required values which don't have defaults set
    try:
        # NOT YET IMPLEMENTED - List container restarts
        api_response = api_instance.get_container_metric_restart(container_id, last_seconds)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainerMetricsApi->get_container_metric_restart: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Container ID |
 **last_seconds** | **float**| Up to how many seconds in the past to ask analytics results |

### Return type

[**MetricRestart**](MetricRestart.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Restarts |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_container_metric_storage**
> MetricStorageResponseList get_container_metric_storage(container_id, last_seconds)

NOT YET IMPLEMENTED - Get Storage consumption metric over time for the container 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import container_metrics_api
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
    api_instance = container_metrics_api.ContainerMetricsApi(api_client)
    container_id = "containerId_example" # str | Container ID
    last_seconds = 3.14 # float | Up to how many seconds in the past to ask analytics results

    # example passing only required values which don't have defaults set
    try:
        # NOT YET IMPLEMENTED - Get Storage consumption metric over time for the container 
        api_response = api_instance.get_container_metric_storage(container_id, last_seconds)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainerMetricsApi->get_container_metric_storage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Container ID |
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

