# qovery.DatabaseMetricsApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_database_current_metric**](DatabaseMetricsApi.md#get_database_current_metric) | **GET** /database/{databaseId}/currentMetric | Get current metric consumption of the database 
[**get_database_metric_cpu**](DatabaseMetricsApi.md#get_database_metric_cpu) | **GET** /database/{databaseId}/metric/cpu | Get CPU consumption metric over time for the database
[**get_database_metric_health_check**](DatabaseMetricsApi.md#get_database_metric_health_check) | **GET** /database/{databaseId}/metric/healthCheck | Get Health Check latency  metric over time for the database
[**get_database_metric_memory**](DatabaseMetricsApi.md#get_database_metric_memory) | **GET** /database/{databaseId}/metric/memory | Get Memory consumption metric over time for the database
[**get_database_metric_restart**](DatabaseMetricsApi.md#get_database_metric_restart) | **GET** /database/{databaseId}/metric/restart | List database restarts
[**get_database_metric_storage**](DatabaseMetricsApi.md#get_database_metric_storage) | **GET** /database/{databaseId}/metric/storage | Get Storage consumption metric over time for the database


# **get_database_current_metric**
> DatabaseCurrentMetric get_database_current_metric(database_id)

Get current metric consumption of the database 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import database_metrics_api
from qovery.model.database_current_metric import DatabaseCurrentMetric
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
    api_instance = database_metrics_api.DatabaseMetricsApi(api_client)
    database_id = "databaseId_example" # str | Database ID

    # example passing only required values which don't have defaults set
    try:
        # Get current metric consumption of the database 
        api_response = api_instance.get_database_current_metric(database_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling DatabaseMetricsApi->get_database_current_metric: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_id** | **str**| Database ID |

### Return type

[**DatabaseCurrentMetric**](DatabaseCurrentMetric.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get database  current metric |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_database_metric_cpu**
> MetricCPUDatapointResponseList get_database_metric_cpu(database_id, last_seconds)

Get CPU consumption metric over time for the database

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import database_metrics_api
from qovery.model.metric_cpu_datapoint_response_list import MetricCPUDatapointResponseList
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
    api_instance = database_metrics_api.DatabaseMetricsApi(api_client)
    database_id = "databaseId_example" # str | Database ID
    last_seconds = 3.14 # float | Up to how many seconds in the past to ask analytics results

    # example passing only required values which don't have defaults set
    try:
        # Get CPU consumption metric over time for the database
        api_response = api_instance.get_database_metric_cpu(database_id, last_seconds)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling DatabaseMetricsApi->get_database_metric_cpu: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_id** | **str**| Database ID |
 **last_seconds** | **float**| Up to how many seconds in the past to ask analytics results |

### Return type

[**MetricCPUDatapointResponseList**](MetricCPUDatapointResponseList.md)

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

# **get_database_metric_health_check**
> MetricGenericResponseList get_database_metric_health_check(database_id, last_seconds)

Get Health Check latency  metric over time for the database

The value returned corresponds to the 95th centile

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import database_metrics_api
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
    api_instance = database_metrics_api.DatabaseMetricsApi(api_client)
    database_id = "databaseId_example" # str | Database ID
    last_seconds = 3.14 # float | Up to how many seconds in the past to ask analytics results

    # example passing only required values which don't have defaults set
    try:
        # Get Health Check latency  metric over time for the database
        api_response = api_instance.get_database_metric_health_check(database_id, last_seconds)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling DatabaseMetricsApi->get_database_metric_health_check: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_id** | **str**| Database ID |
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

# **get_database_metric_memory**
> MetricMemoryDatapointResponseList get_database_metric_memory(database_id, last_seconds)

Get Memory consumption metric over time for the database

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import database_metrics_api
from qovery.model.metric_memory_datapoint_response_list import MetricMemoryDatapointResponseList
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
    api_instance = database_metrics_api.DatabaseMetricsApi(api_client)
    database_id = "databaseId_example" # str | Database ID
    last_seconds = 3.14 # float | Up to how many seconds in the past to ask analytics results

    # example passing only required values which don't have defaults set
    try:
        # Get Memory consumption metric over time for the database
        api_response = api_instance.get_database_metric_memory(database_id, last_seconds)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling DatabaseMetricsApi->get_database_metric_memory: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_id** | **str**| Database ID |
 **last_seconds** | **float**| Up to how many seconds in the past to ask analytics results |

### Return type

[**MetricMemoryDatapointResponseList**](MetricMemoryDatapointResponseList.md)

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

# **get_database_metric_restart**
> MetricRestart get_database_metric_restart(database_id, last_seconds)

List database restarts

Get database restart message and timestamp.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import database_metrics_api
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
    api_instance = database_metrics_api.DatabaseMetricsApi(api_client)
    database_id = "databaseId_example" # str | Database ID
    last_seconds = 3.14 # float | Up to how many seconds in the past to ask analytics results

    # example passing only required values which don't have defaults set
    try:
        # List database restarts
        api_response = api_instance.get_database_metric_restart(database_id, last_seconds)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling DatabaseMetricsApi->get_database_metric_restart: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_id** | **str**| Database ID |
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

# **get_database_metric_storage**
> MetricStorageDatapointResponseList get_database_metric_storage(database_id, last_seconds)

Get Storage consumption metric over time for the database

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import database_metrics_api
from qovery.model.metric_storage_datapoint_response_list import MetricStorageDatapointResponseList
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
    api_instance = database_metrics_api.DatabaseMetricsApi(api_client)
    database_id = "databaseId_example" # str | Database ID
    last_seconds = 3.14 # float | Up to how many seconds in the past to ask analytics results

    # example passing only required values which don't have defaults set
    try:
        # Get Storage consumption metric over time for the database
        api_response = api_instance.get_database_metric_storage(database_id, last_seconds)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling DatabaseMetricsApi->get_database_metric_storage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_id** | **str**| Database ID |
 **last_seconds** | **float**| Up to how many seconds in the past to ask analytics results |

### Return type

[**MetricStorageDatapointResponseList**](MetricStorageDatapointResponseList.md)

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

