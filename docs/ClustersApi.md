# qovery.ClustersApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cluster**](ClustersApi.md#create_cluster) | **POST** /organization/{organizationId}/cluster | Create a cluster
[**delete_cluster**](ClustersApi.md#delete_cluster) | **DELETE** /organization/{organizationId}/cluster/{clusterId} | Delete a cluster
[**deploy_cluster**](ClustersApi.md#deploy_cluster) | **POST** /organization/{organizationId}/cluster/{clusterId}/deploy | Deploy a cluster
[**edit_cluster**](ClustersApi.md#edit_cluster) | **PUT** /organization/{organizationId}/cluster/{clusterId} | Edit a cluster
[**edit_routing_table**](ClustersApi.md#edit_routing_table) | **PUT** /organization/{organizationId}/cluster/{clusterId}/routingTable | Edit routing table
[**get_cluster_readiness_status**](ClustersApi.md#get_cluster_readiness_status) | **GET** /organization/{organizationId}/cluster/{clusterId}/isReady | Know if a cluster is ready to be deployed or not
[**get_cluster_status**](ClustersApi.md#get_cluster_status) | **GET** /organization/{organizationId}/cluster/{clusterId}/status | Get cluster status
[**get_organization_cloud_provider_info**](ClustersApi.md#get_organization_cloud_provider_info) | **GET** /organization/{organizationId}/cluster/{clusterId}/cloudProviderInfo | Get cluster cloud provider info and credentials
[**get_organization_cluster_status**](ClustersApi.md#get_organization_cluster_status) | **GET** /organization/{organizationId}/cluster/status | List all clusters statuses
[**get_routing_table**](ClustersApi.md#get_routing_table) | **GET** /organization/{organizationId}/cluster/{clusterId}/routingTable | Get routing table
[**list_organization_cluster**](ClustersApi.md#list_organization_cluster) | **GET** /organization/{organizationId}/cluster | List organization clusters
[**specify_cluster_cloud_provider_info**](ClustersApi.md#specify_cluster_cloud_provider_info) | **POST** /organization/{organizationId}/cluster/{clusterId}/cloudProviderInfo | Specify cluster cloud provider info and credentials
[**stop_cluster**](ClustersApi.md#stop_cluster) | **POST** /organization/{organizationId}/cluster/{clusterId}/stop | Stop cluster
[**update_cluster**](ClustersApi.md#update_cluster) | **POST** /organization/{organizationId}/cluster/{clusterId}/update | Update a cluster Version


# **create_cluster**
> ClusterResponse create_cluster(organization_id)

Create a cluster

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import clusters_api
from qovery.model.cluster_request import ClusterRequest
from qovery.model.cluster_response import ClusterResponse
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
    api_instance = clusters_api.ClustersApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    cluster_request = ClusterRequest(None) # ClusterRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a cluster
        api_response = api_instance.create_cluster(organization_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ClustersApi->create_cluster: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a cluster
        api_response = api_instance.create_cluster(organization_id, cluster_request=cluster_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ClustersApi->create_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **cluster_request** | [**ClusterRequest**](ClusterRequest.md)|  | [optional]

### Return type

[**ClusterResponse**](ClusterResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create cluster |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cluster**
> delete_cluster(organization_id, cluster_id)

Delete a cluster

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import clusters_api
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
    api_instance = clusters_api.ClustersApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    cluster_id = "clusterId_example" # str | Cluster ID

    # example passing only required values which don't have defaults set
    try:
        # Delete a cluster
        api_instance.delete_cluster(organization_id, cluster_id)
    except qovery.ApiException as e:
        print("Exception when calling ClustersApi->delete_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **cluster_id** | **str**| Cluster ID |

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

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

# **deploy_cluster**
> ClusterStatusResponse deploy_cluster(organization_id, cluster_id)

Deploy a cluster

allows to deploy a cluster

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import clusters_api
from qovery.model.cluster_status_response import ClusterStatusResponse
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
    api_instance = clusters_api.ClustersApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    cluster_id = "clusterId_example" # str | Cluster ID

    # example passing only required values which don't have defaults set
    try:
        # Deploy a cluster
        api_response = api_instance.deploy_cluster(organization_id, cluster_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ClustersApi->deploy_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **cluster_id** | **str**| Cluster ID |

### Return type

[**ClusterStatusResponse**](ClusterStatusResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Deploy cluster |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_cluster**
> ClusterResponse edit_cluster(organization_id, cluster_id)

Edit a cluster

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import clusters_api
from qovery.model.cluster_request import ClusterRequest
from qovery.model.cluster_response import ClusterResponse
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
    api_instance = clusters_api.ClustersApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    cluster_id = "clusterId_example" # str | Cluster ID
    cluster_request = ClusterRequest(None) # ClusterRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Edit a cluster
        api_response = api_instance.edit_cluster(organization_id, cluster_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ClustersApi->edit_cluster: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit a cluster
        api_response = api_instance.edit_cluster(organization_id, cluster_id, cluster_request=cluster_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ClustersApi->edit_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **cluster_id** | **str**| Cluster ID |
 **cluster_request** | [**ClusterRequest**](ClusterRequest.md)|  | [optional]

### Return type

[**ClusterResponse**](ClusterResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Edited the cluster |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_routing_table**
> ClusterRoutingTableResponse edit_routing_table(organization_id, cluster_id)

Edit routing table

Edit routing table by returning updated table.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import clusters_api
from qovery.model.cluster_routing_table_request import ClusterRoutingTableRequest
from qovery.model.cluster_routing_table_response import ClusterRoutingTableResponse
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
    api_instance = clusters_api.ClustersApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    cluster_id = "clusterId_example" # str | Cluster ID
    cluster_routing_table_request = ClusterRoutingTableRequest(
        routes=[
            ClusterRoutingTableRequestRoutes(
                destination="destination_example",
                target="target_example",
                description="description_example",
            ),
        ],
    ) # ClusterRoutingTableRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Edit routing table
        api_response = api_instance.edit_routing_table(organization_id, cluster_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ClustersApi->edit_routing_table: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit routing table
        api_response = api_instance.edit_routing_table(organization_id, cluster_id, cluster_routing_table_request=cluster_routing_table_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ClustersApi->edit_routing_table: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **cluster_id** | **str**| Cluster ID |
 **cluster_routing_table_request** | [**ClusterRoutingTableRequest**](ClusterRoutingTableRequest.md)|  | [optional]

### Return type

[**ClusterRoutingTableResponse**](ClusterRoutingTableResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Updated routing table |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_readiness_status**
> ClusterReadinessStatus get_cluster_readiness_status(organization_id, cluster_id)

Know if a cluster is ready to be deployed or not

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import clusters_api
from qovery.model.cluster_readiness_status import ClusterReadinessStatus
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
    api_instance = clusters_api.ClustersApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    cluster_id = "clusterId_example" # str | Cluster ID

    # example passing only required values which don't have defaults set
    try:
        # Know if a cluster is ready to be deployed or not
        api_response = api_instance.get_cluster_readiness_status(organization_id, cluster_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ClustersApi->get_cluster_readiness_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **cluster_id** | **str**| Cluster ID |

### Return type

[**ClusterReadinessStatus**](ClusterReadinessStatus.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Cluster Readiness Status |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_status**
> ClusterStatusResponse get_cluster_status(organization_id, cluster_id)

Get cluster status

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import clusters_api
from qovery.model.cluster_status_response import ClusterStatusResponse
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
    api_instance = clusters_api.ClustersApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    cluster_id = "clusterId_example" # str | Cluster ID

    # example passing only required values which don't have defaults set
    try:
        # Get cluster status
        api_response = api_instance.get_cluster_status(organization_id, cluster_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ClustersApi->get_cluster_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **cluster_id** | **str**| Cluster ID |

### Return type

[**ClusterStatusResponse**](ClusterStatusResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get status |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_cloud_provider_info**
> ClusterCloudProviderInfoResponse get_organization_cloud_provider_info(organization_id, cluster_id)

Get cluster cloud provider info and credentials

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import clusters_api
from qovery.model.cluster_cloud_provider_info_response import ClusterCloudProviderInfoResponse
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
    api_instance = clusters_api.ClustersApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    cluster_id = "clusterId_example" # str | Cluster ID

    # example passing only required values which don't have defaults set
    try:
        # Get cluster cloud provider info and credentials
        api_response = api_instance.get_organization_cloud_provider_info(organization_id, cluster_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ClustersApi->get_organization_cloud_provider_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **cluster_id** | **str**| Cluster ID |

### Return type

[**ClusterCloudProviderInfoResponse**](ClusterCloudProviderInfoResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | get cloud provider info and credentials |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_cluster_status**
> ClusterStatusResponseList get_organization_cluster_status(organization_id)

List all clusters statuses

Returns a list of clusters with only their id and status.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import clusters_api
from qovery.model.cluster_status_response_list import ClusterStatusResponseList
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
    api_instance = clusters_api.ClustersApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID

    # example passing only required values which don't have defaults set
    try:
        # List all clusters statuses
        api_response = api_instance.get_organization_cluster_status(organization_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ClustersApi->get_organization_cluster_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |

### Return type

[**ClusterStatusResponseList**](ClusterStatusResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get statuses |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_routing_table**
> ClusterRoutingTableResponse get_routing_table(organization_id, cluster_id)

Get routing table

Retrieve network routing table where each line corresponds to a route between a destination and a target.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import clusters_api
from qovery.model.cluster_routing_table_response import ClusterRoutingTableResponse
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
    api_instance = clusters_api.ClustersApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    cluster_id = "clusterId_example" # str | Cluster ID

    # example passing only required values which don't have defaults set
    try:
        # Get routing table
        api_response = api_instance.get_routing_table(organization_id, cluster_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ClustersApi->get_routing_table: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **cluster_id** | **str**| Cluster ID |

### Return type

[**ClusterRoutingTableResponse**](ClusterRoutingTableResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Routing table |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_organization_cluster**
> ClusterResponseList list_organization_cluster(organization_id)

List organization clusters

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import clusters_api
from qovery.model.cluster_response_list import ClusterResponseList
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
    api_instance = clusters_api.ClustersApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID

    # example passing only required values which don't have defaults set
    try:
        # List organization clusters
        api_response = api_instance.list_organization_cluster(organization_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ClustersApi->list_organization_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |

### Return type

[**ClusterResponseList**](ClusterResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List clusters |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **specify_cluster_cloud_provider_info**
> ClusterCloudProviderInfoResponse specify_cluster_cloud_provider_info(organization_id, cluster_id)

Specify cluster cloud provider info and credentials

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import clusters_api
from qovery.model.cluster_cloud_provider_info_response import ClusterCloudProviderInfoResponse
from qovery.model.cluster_cloud_provider_info_request import ClusterCloudProviderInfoRequest
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
    api_instance = clusters_api.ClustersApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    cluster_id = "clusterId_example" # str | Cluster ID
    cluster_cloud_provider_info_request = ClusterCloudProviderInfoRequest(
        cloud_provider=CloudProviderEnum("AWS"),
        credentials=ClusterCloudProviderInfoRequestCredentials(
            id="id_example",
            name="name_example",
        ),
        region="region_example",
    ) # ClusterCloudProviderInfoRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Specify cluster cloud provider info and credentials
        api_response = api_instance.specify_cluster_cloud_provider_info(organization_id, cluster_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ClustersApi->specify_cluster_cloud_provider_info: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Specify cluster cloud provider info and credentials
        api_response = api_instance.specify_cluster_cloud_provider_info(organization_id, cluster_id, cluster_cloud_provider_info_request=cluster_cloud_provider_info_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ClustersApi->specify_cluster_cloud_provider_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **cluster_id** | **str**| Cluster ID |
 **cluster_cloud_provider_info_request** | [**ClusterCloudProviderInfoRequest**](ClusterCloudProviderInfoRequest.md)|  | [optional]

### Return type

[**ClusterCloudProviderInfoResponse**](ClusterCloudProviderInfoResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create cluster |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_cluster**
> ClusterStatusResponse stop_cluster(organization_id, cluster_id)

Stop cluster

Cluster stop has been requester.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import clusters_api
from qovery.model.cluster_status_response import ClusterStatusResponse
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
    api_instance = clusters_api.ClustersApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    cluster_id = "clusterId_example" # str | Cluster ID

    # example passing only required values which don't have defaults set
    try:
        # Stop cluster
        api_response = api_instance.stop_cluster(organization_id, cluster_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ClustersApi->stop_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **cluster_id** | **str**| Cluster ID |

### Return type

[**ClusterStatusResponse**](ClusterStatusResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Update cluster |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Cluster is already stopped or an operation is in progress |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster**
> ClusterStatusResponse update_cluster(organization_id, cluster_id)

Update a cluster Version

allows to update cluster version

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import clusters_api
from qovery.model.cluster_status_response import ClusterStatusResponse
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
    api_instance = clusters_api.ClustersApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    cluster_id = "clusterId_example" # str | Cluster ID

    # example passing only required values which don't have defaults set
    try:
        # Update a cluster Version
        api_response = api_instance.update_cluster(organization_id, cluster_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ClustersApi->update_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **cluster_id** | **str**| Cluster ID |

### Return type

[**ClusterStatusResponse**](ClusterStatusResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Update cluster |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

