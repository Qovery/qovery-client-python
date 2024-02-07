# qovery.CloudProviderApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_aws_features**](CloudProviderApi.md#list_aws_features) | **GET** /aws/clusterFeature | List AWS features available
[**list_aws_instance_type**](CloudProviderApi.md#list_aws_instance_type) | **GET** /aws/instanceType | List AWS available instance types
[**list_aws_managed_database_instance_type**](CloudProviderApi.md#list_aws_managed_database_instance_type) | **GET** /aws/managedDatabase/instanceType/{region}/{databaseType} | List AWS available managed database instance types
[**list_aws_managed_database_type**](CloudProviderApi.md#list_aws_managed_database_type) | **GET** /aws/managedDatabase/type | List AWS available managed database types
[**list_aws_regions**](CloudProviderApi.md#list_aws_regions) | **GET** /aws/region | List AWS regions
[**list_awsec2_instance_type**](CloudProviderApi.md#list_awsec2_instance_type) | **GET** /aws/ec2/instanceType/{region} | List AWS EC2 available instance types
[**list_awseks_instance_type**](CloudProviderApi.md#list_awseks_instance_type) | **GET** /aws/eks/instanceType/{region} | List AWS EKS available instance types
[**list_cloud_provider**](CloudProviderApi.md#list_cloud_provider) | **GET** /cloudProvider | List Cloud providers available
[**list_gcp_features**](CloudProviderApi.md#list_gcp_features) | **GET** /gcp/clusterFeature | List GCP features available
[**list_gcp_gke_instance_type**](CloudProviderApi.md#list_gcp_gke_instance_type) | **GET** /gcp/instanceType/{region} | List GCP GKE available instance types
[**list_gcp_regions**](CloudProviderApi.md#list_gcp_regions) | **GET** /gcp/region | List GCP regions
[**list_scaleway_features**](CloudProviderApi.md#list_scaleway_features) | **GET** /scaleway/clusterFeature | List Scaleway features available
[**list_scaleway_instance_type**](CloudProviderApi.md#list_scaleway_instance_type) | **GET** /scaleway/instanceType | List Scaleway available instance types
[**list_scaleway_kapsule_instance_type**](CloudProviderApi.md#list_scaleway_kapsule_instance_type) | **GET** /scaleway/instanceType/{zone} | List Scaleway Kapsule available instance types
[**list_scaleway_regions**](CloudProviderApi.md#list_scaleway_regions) | **GET** /scaleway/region | List Scaleway regions
[**list_scw_managed_database_instance_type**](CloudProviderApi.md#list_scw_managed_database_instance_type) | **GET** /scaleway/managedDatabase/instanceType/{zone}/{databaseType} | List Scaleway available managed database instance types
[**list_scw_managed_database_type**](CloudProviderApi.md#list_scw_managed_database_type) | **GET** /scaleway/managedDatabase/type | List Scaleway available managed database types


# **list_aws_features**
> ClusterFeatureResponseList list_aws_features()

List AWS features available

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import os
import qovery
from qovery.models.cluster_feature_response_list import ClusterFeatureResponseList
from qovery.rest import ApiException
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
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = qovery.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qovery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qovery.CloudProviderApi(api_client)

    try:
        # List AWS features available
        api_response = api_instance.list_aws_features()
        print("The response of CloudProviderApi->list_aws_features:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudProviderApi->list_aws_features: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ClusterFeatureResponseList**](ClusterFeatureResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

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
> ClusterInstanceTypeResponseList list_aws_instance_type()

List AWS available instance types

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import os
import qovery
from qovery.models.cluster_instance_type_response_list import ClusterInstanceTypeResponseList
from qovery.rest import ApiException
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
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = qovery.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qovery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qovery.CloudProviderApi(api_client)

    try:
        # List AWS available instance types
        api_response = api_instance.list_aws_instance_type()
        print("The response of CloudProviderApi->list_aws_instance_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudProviderApi->list_aws_instance_type: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ClusterInstanceTypeResponseList**](ClusterInstanceTypeResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

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

# **list_aws_managed_database_instance_type**
> ManagedDatabaseInstanceTypeResponseList list_aws_managed_database_instance_type(region, database_type)

List AWS available managed database instance types

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import os
import qovery
from qovery.models.managed_database_instance_type_response_list import ManagedDatabaseInstanceTypeResponseList
from qovery.rest import ApiException
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
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = qovery.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qovery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qovery.CloudProviderApi(api_client)
    region = 'us-east-2' # str | region name
    database_type = 'MYSQL' # str | Database type

    try:
        # List AWS available managed database instance types
        api_response = api_instance.list_aws_managed_database_instance_type(region, database_type)
        print("The response of CloudProviderApi->list_aws_managed_database_instance_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudProviderApi->list_aws_managed_database_instance_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region** | **str**| region name | 
 **database_type** | **str**| Database type | 

### Return type

[**ManagedDatabaseInstanceTypeResponseList**](ManagedDatabaseInstanceTypeResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list AWS available managed database instance types |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_aws_managed_database_type**
> ManagedDatabaseTypeResponseList list_aws_managed_database_type()

List AWS available managed database types

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import os
import qovery
from qovery.models.managed_database_type_response_list import ManagedDatabaseTypeResponseList
from qovery.rest import ApiException
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
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = qovery.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qovery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qovery.CloudProviderApi(api_client)

    try:
        # List AWS available managed database types
        api_response = api_instance.list_aws_managed_database_type()
        print("The response of CloudProviderApi->list_aws_managed_database_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudProviderApi->list_aws_managed_database_type: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ManagedDatabaseTypeResponseList**](ManagedDatabaseTypeResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list AWS available managed database types |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_aws_regions**
> ClusterRegionResponseList list_aws_regions()

List AWS regions

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import os
import qovery
from qovery.models.cluster_region_response_list import ClusterRegionResponseList
from qovery.rest import ApiException
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
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = qovery.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qovery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qovery.CloudProviderApi(api_client)

    try:
        # List AWS regions
        api_response = api_instance.list_aws_regions()
        print("The response of CloudProviderApi->list_aws_regions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudProviderApi->list_aws_regions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ClusterRegionResponseList**](ClusterRegionResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

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

# **list_awsec2_instance_type**
> ClusterInstanceTypeResponseList list_awsec2_instance_type(region)

List AWS EC2 available instance types

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import os
import qovery
from qovery.models.cluster_instance_type_response_list import ClusterInstanceTypeResponseList
from qovery.rest import ApiException
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
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = qovery.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qovery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qovery.CloudProviderApi(api_client)
    region = 'us-east-2' # str | region name

    try:
        # List AWS EC2 available instance types
        api_response = api_instance.list_awsec2_instance_type(region)
        print("The response of CloudProviderApi->list_awsec2_instance_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudProviderApi->list_awsec2_instance_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region** | **str**| region name | 

### Return type

[**ClusterInstanceTypeResponseList**](ClusterInstanceTypeResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list the instance types available for AWS Ec2 by region |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_awseks_instance_type**
> ClusterInstanceTypeResponseList list_awseks_instance_type(region)

List AWS EKS available instance types

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import os
import qovery
from qovery.models.cluster_instance_type_response_list import ClusterInstanceTypeResponseList
from qovery.rest import ApiException
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
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = qovery.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qovery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qovery.CloudProviderApi(api_client)
    region = 'us-east-2' # str | region name

    try:
        # List AWS EKS available instance types
        api_response = api_instance.list_awseks_instance_type(region)
        print("The response of CloudProviderApi->list_awseks_instance_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudProviderApi->list_awseks_instance_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region** | **str**| region name | 

### Return type

[**ClusterInstanceTypeResponseList**](ClusterInstanceTypeResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list the instance types available for AWS EKS by region |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cloud_provider**
> CloudProviderResponseList list_cloud_provider()

List Cloud providers available

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import os
import qovery
from qovery.models.cloud_provider_response_list import CloudProviderResponseList
from qovery.rest import ApiException
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
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = qovery.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qovery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qovery.CloudProviderApi(api_client)

    try:
        # List Cloud providers available
        api_response = api_instance.list_cloud_provider()
        print("The response of CloudProviderApi->list_cloud_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudProviderApi->list_cloud_provider: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CloudProviderResponseList**](CloudProviderResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

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

# **list_gcp_features**
> ClusterFeatureResponseList list_gcp_features()

List GCP features available

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import os
import qovery
from qovery.models.cluster_feature_response_list import ClusterFeatureResponseList
from qovery.rest import ApiException
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
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = qovery.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qovery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qovery.CloudProviderApi(api_client)

    try:
        # List GCP features available
        api_response = api_instance.list_gcp_features()
        print("The response of CloudProviderApi->list_gcp_features:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudProviderApi->list_gcp_features: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ClusterFeatureResponseList**](ClusterFeatureResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list features available for GCP cloud provider |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_gcp_gke_instance_type**
> ClusterInstanceTypeResponseList list_gcp_gke_instance_type(region)

List GCP GKE available instance types

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import os
import qovery
from qovery.models.cluster_instance_type_response_list import ClusterInstanceTypeResponseList
from qovery.rest import ApiException
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
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = qovery.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qovery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qovery.CloudProviderApi(api_client)
    region = 'us-east-2' # str | region name

    try:
        # List GCP GKE available instance types
        api_response = api_instance.list_gcp_gke_instance_type(region)
        print("The response of CloudProviderApi->list_gcp_gke_instance_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudProviderApi->list_gcp_gke_instance_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region** | **str**| region name | 

### Return type

[**ClusterInstanceTypeResponseList**](ClusterInstanceTypeResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list the instance types available for GCP GKE by region |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_gcp_regions**
> ClusterRegionResponseList list_gcp_regions()

List GCP regions

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import os
import qovery
from qovery.models.cluster_region_response_list import ClusterRegionResponseList
from qovery.rest import ApiException
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
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = qovery.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qovery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qovery.CloudProviderApi(api_client)

    try:
        # List GCP regions
        api_response = api_instance.list_gcp_regions()
        print("The response of CloudProviderApi->list_gcp_regions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudProviderApi->list_gcp_regions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ClusterRegionResponseList**](ClusterRegionResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

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

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import os
import qovery
from qovery.models.cluster_feature_response_list import ClusterFeatureResponseList
from qovery.rest import ApiException
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
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = qovery.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qovery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qovery.CloudProviderApi(api_client)

    try:
        # List Scaleway features available
        api_response = api_instance.list_scaleway_features()
        print("The response of CloudProviderApi->list_scaleway_features:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudProviderApi->list_scaleway_features: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ClusterFeatureResponseList**](ClusterFeatureResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

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
> ClusterInstanceTypeResponseList list_scaleway_instance_type()

List Scaleway available instance types

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import os
import qovery
from qovery.models.cluster_instance_type_response_list import ClusterInstanceTypeResponseList
from qovery.rest import ApiException
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
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = qovery.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qovery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qovery.CloudProviderApi(api_client)

    try:
        # List Scaleway available instance types
        api_response = api_instance.list_scaleway_instance_type()
        print("The response of CloudProviderApi->list_scaleway_instance_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudProviderApi->list_scaleway_instance_type: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ClusterInstanceTypeResponseList**](ClusterInstanceTypeResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

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

# **list_scaleway_kapsule_instance_type**
> ClusterInstanceTypeResponseList list_scaleway_kapsule_instance_type(zone)

List Scaleway Kapsule available instance types

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import os
import qovery
from qovery.models.cluster_instance_type_response_list import ClusterInstanceTypeResponseList
from qovery.rest import ApiException
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
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = qovery.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qovery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qovery.CloudProviderApi(api_client)
    zone = 'fr-par-1' # str | zone name

    try:
        # List Scaleway Kapsule available instance types
        api_response = api_instance.list_scaleway_kapsule_instance_type(zone)
        print("The response of CloudProviderApi->list_scaleway_kapsule_instance_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudProviderApi->list_scaleway_kapsule_instance_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **zone** | **str**| zone name | 

### Return type

[**ClusterInstanceTypeResponseList**](ClusterInstanceTypeResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list the instance types available for Scaleway Kapsule by region |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_scaleway_regions**
> ClusterRegionResponseList list_scaleway_regions()

List Scaleway regions

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import os
import qovery
from qovery.models.cluster_region_response_list import ClusterRegionResponseList
from qovery.rest import ApiException
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
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = qovery.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qovery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qovery.CloudProviderApi(api_client)

    try:
        # List Scaleway regions
        api_response = api_instance.list_scaleway_regions()
        print("The response of CloudProviderApi->list_scaleway_regions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudProviderApi->list_scaleway_regions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ClusterRegionResponseList**](ClusterRegionResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

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

# **list_scw_managed_database_instance_type**
> ManagedDatabaseInstanceTypeResponseList list_scw_managed_database_instance_type(database_type)

List Scaleway available managed database instance types

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import os
import qovery
from qovery.models.managed_database_instance_type_response_list import ManagedDatabaseInstanceTypeResponseList
from qovery.rest import ApiException
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
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = qovery.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qovery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qovery.CloudProviderApi(api_client)
    database_type = 'MYSQL' # str | Database type

    try:
        # List Scaleway available managed database instance types
        api_response = api_instance.list_scw_managed_database_instance_type(database_type)
        print("The response of CloudProviderApi->list_scw_managed_database_instance_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudProviderApi->list_scw_managed_database_instance_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_type** | **str**| Database type | 

### Return type

[**ManagedDatabaseInstanceTypeResponseList**](ManagedDatabaseInstanceTypeResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list Scaleway available managed database instance types |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_scw_managed_database_type**
> ManagedDatabaseTypeResponseList list_scw_managed_database_type()

List Scaleway available managed database types

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import os
import qovery
from qovery.models.managed_database_type_response_list import ManagedDatabaseTypeResponseList
from qovery.rest import ApiException
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
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = qovery.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with qovery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = qovery.CloudProviderApi(api_client)

    try:
        # List Scaleway available managed database types
        api_response = api_instance.list_scw_managed_database_type()
        print("The response of CloudProviderApi->list_scw_managed_database_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CloudProviderApi->list_scw_managed_database_type: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ManagedDatabaseTypeResponseList**](ManagedDatabaseTypeResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list Scaleway available managed database types |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

