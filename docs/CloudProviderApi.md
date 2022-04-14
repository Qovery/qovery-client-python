# qovery.CloudProviderApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_aws_features**](CloudProviderApi.md#list_aws_features) | **GET** /aws/clusterFeature | List AWS features available
[**list_aws_instance_type**](CloudProviderApi.md#list_aws_instance_type) | **GET** /aws/instanceType | List AWS available instance types
[**list_aws_regions**](CloudProviderApi.md#list_aws_regions) | **GET** /aws/region | List AWS regions
[**list_cloud_provider**](CloudProviderApi.md#list_cloud_provider) | **GET** /cloudProvider | List Cloud providers available
[**list_do_features**](CloudProviderApi.md#list_do_features) | **GET** /digitalOcean/clusterFeature | List DO features available
[**list_do_instance_type**](CloudProviderApi.md#list_do_instance_type) | **GET** /digitalOcean/instanceType | List DO available instance types
[**list_do_regions**](CloudProviderApi.md#list_do_regions) | **GET** /digitalOcean/region | List DO regions
[**list_scaleway_features**](CloudProviderApi.md#list_scaleway_features) | **GET** /scaleway/clusterFeature | List Scaleway features available
[**list_scaleway_instance_type**](CloudProviderApi.md#list_scaleway_instance_type) | **GET** /scaleway/instanceType | List Scaleway available instance types
[**list_scaleway_regions**](CloudProviderApi.md#list_scaleway_regions) | **GET** /scaleway/region | List Scaleway regions


# **list_aws_features**
> ClusterFeatureResponseList list_aws_features()

List AWS features available

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import cloud_provider_api
from qovery.model.cluster_feature_response_list import ClusterFeatureResponseList
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
    api_instance = cloud_provider_api.CloudProviderApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List AWS features available
        api_response = api_instance.list_aws_features()
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling CloudProviderApi->list_aws_features: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterFeatureResponseList**](ClusterFeatureResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list features available for AWS cloud provider |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_aws_instance_type**
> InlineResponse200 list_aws_instance_type()

List AWS available instance types

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import cloud_provider_api
from qovery.model.inline_response200 import InlineResponse200
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
    api_instance = cloud_provider_api.CloudProviderApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List AWS available instance types
        api_response = api_instance.list_aws_instance_type()
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling CloudProviderApi->list_aws_instance_type: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list the instance types available for AWS cloud provider |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_aws_regions**
> ClusterRegionResponseList list_aws_regions()

List AWS regions

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import cloud_provider_api
from qovery.model.cluster_region_response_list import ClusterRegionResponseList
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
    api_instance = cloud_provider_api.CloudProviderApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List AWS regions
        api_response = api_instance.list_aws_regions()
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling CloudProviderApi->list_aws_regions: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterRegionResponseList**](ClusterRegionResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list regions |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cloud_provider**
> CloudProviderResponseList list_cloud_provider()

List Cloud providers available

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import cloud_provider_api
from qovery.model.cloud_provider_response_list import CloudProviderResponseList
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
    api_instance = cloud_provider_api.CloudProviderApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List Cloud providers available
        api_response = api_instance.list_cloud_provider()
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling CloudProviderApi->list_cloud_provider: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CloudProviderResponseList**](CloudProviderResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list cloud providers |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_do_features**
> ClusterFeatureResponseList list_do_features()

List DO features available

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import cloud_provider_api
from qovery.model.cluster_feature_response_list import ClusterFeatureResponseList
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
    api_instance = cloud_provider_api.CloudProviderApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List DO features available
        api_response = api_instance.list_do_features()
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling CloudProviderApi->list_do_features: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterFeatureResponseList**](ClusterFeatureResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list features available for Digital Ocean cloud provider |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_do_instance_type**
> ERRORUNKNOWN list_do_instance_type()

List DO available instance types

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import cloud_provider_api
from qovery.model.errorunknown import ERRORUNKNOWN
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
    api_instance = cloud_provider_api.CloudProviderApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List DO available instance types
        api_response = api_instance.list_do_instance_type()
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling CloudProviderApi->list_do_instance_type: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ERRORUNKNOWN**](ERRORUNKNOWN.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list the instance types available for Digital Ocean cloud provider |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_do_regions**
> ClusterRegionResponseList list_do_regions()

List DO regions

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import cloud_provider_api
from qovery.model.cluster_region_response_list import ClusterRegionResponseList
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
    api_instance = cloud_provider_api.CloudProviderApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List DO regions
        api_response = api_instance.list_do_regions()
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling CloudProviderApi->list_do_regions: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterRegionResponseList**](ClusterRegionResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list regions |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_scaleway_features**
> ClusterFeatureResponseList list_scaleway_features()

List Scaleway features available

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import cloud_provider_api
from qovery.model.cluster_feature_response_list import ClusterFeatureResponseList
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
    api_instance = cloud_provider_api.CloudProviderApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List Scaleway features available
        api_response = api_instance.list_scaleway_features()
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling CloudProviderApi->list_scaleway_features: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterFeatureResponseList**](ClusterFeatureResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list features available for Scaleway cloud provider |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_scaleway_instance_type**
> ERRORUNKNOWN list_scaleway_instance_type()

List Scaleway available instance types

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import cloud_provider_api
from qovery.model.errorunknown import ERRORUNKNOWN
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
    api_instance = cloud_provider_api.CloudProviderApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List Scaleway available instance types
        api_response = api_instance.list_scaleway_instance_type()
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling CloudProviderApi->list_scaleway_instance_type: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ERRORUNKNOWN**](ERRORUNKNOWN.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list the instance types available for Scaleway cloud provider |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_scaleway_regions**
> ClusterRegionResponseList list_scaleway_regions()

List Scaleway regions

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import cloud_provider_api
from qovery.model.cluster_region_response_list import ClusterRegionResponseList
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
    api_instance = cloud_provider_api.CloudProviderApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List Scaleway regions
        api_response = api_instance.list_scaleway_regions()
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling CloudProviderApi->list_scaleway_regions: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterRegionResponseList**](ClusterRegionResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list regions |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

