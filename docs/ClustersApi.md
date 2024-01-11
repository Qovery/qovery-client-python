# qovery.ClustersApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cluster**](ClustersApi.md#create_cluster) | **POST** /organization/{organizationId}/cluster | Create a cluster
[**delete_cluster**](ClustersApi.md#delete_cluster) | **DELETE** /organization/{organizationId}/cluster/{clusterId} | Delete a cluster
[**deploy_cluster**](ClustersApi.md#deploy_cluster) | **POST** /organization/{organizationId}/cluster/{clusterId}/deploy | Deploy a cluster
[**edit_cluster**](ClustersApi.md#edit_cluster) | **PUT** /organization/{organizationId}/cluster/{clusterId} | Edit a cluster
[**edit_cluster_advanced_settings**](ClustersApi.md#edit_cluster_advanced_settings) | **PUT** /organization/{organizationId}/cluster/{clusterId}/advancedSettings | Edit advanced settings
[**edit_routing_table**](ClustersApi.md#edit_routing_table) | **PUT** /organization/{organizationId}/cluster/{clusterId}/routingTable | Edit routing table
[**get_cluster_advanced_settings**](ClustersApi.md#get_cluster_advanced_settings) | **GET** /organization/{organizationId}/cluster/{clusterId}/advancedSettings | Get advanced settings
[**get_cluster_kubeconfig**](ClustersApi.md#get_cluster_kubeconfig) | **GET** /organization/{organizationId}/cluster/{clusterId}/kubeconfig | Get cluster kubeconfig
[**get_cluster_readiness_status**](ClustersApi.md#get_cluster_readiness_status) | **GET** /organization/{organizationId}/cluster/{clusterId}/isReady | Know if a cluster is ready to be deployed or not
[**get_cluster_status**](ClustersApi.md#get_cluster_status) | **GET** /organization/{organizationId}/cluster/{clusterId}/status | Get cluster status
[**get_default_cluster_advanced_settings**](ClustersApi.md#get_default_cluster_advanced_settings) | **GET** /defaultClusterAdvancedSettings | List default cluster advanced settings
[**get_installation_helm_values**](ClustersApi.md#get_installation_helm_values) | **GET** /organization/{organizationId}/cluster/{clusterId}/installationHelmValues | Get cluster helm values for self managed installation
[**get_organization_cloud_provider_info**](ClustersApi.md#get_organization_cloud_provider_info) | **GET** /organization/{organizationId}/cluster/{clusterId}/cloudProviderInfo | Get cluster cloud provider info and credentials
[**get_organization_cluster_status**](ClustersApi.md#get_organization_cluster_status) | **GET** /organization/{organizationId}/cluster/status | List all clusters statuses
[**get_routing_table**](ClustersApi.md#get_routing_table) | **GET** /organization/{organizationId}/cluster/{clusterId}/routingTable | Get routing table
[**list_cluster_logs**](ClustersApi.md#list_cluster_logs) | **GET** /organization/{organizationId}/cluster/{clusterId}/logs | List Cluster Logs
[**list_organization_cluster**](ClustersApi.md#list_organization_cluster) | **GET** /organization/{organizationId}/cluster | List organization clusters
[**specify_cluster_cloud_provider_info**](ClustersApi.md#specify_cluster_cloud_provider_info) | **POST** /organization/{organizationId}/cluster/{clusterId}/cloudProviderInfo | Specify cluster cloud provider info and credentials
[**stop_cluster**](ClustersApi.md#stop_cluster) | **POST** /organization/{organizationId}/cluster/{clusterId}/stop | Stop cluster


# **create_cluster**
> Cluster create_cluster(organization_id)

Create a cluster

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import clusters_api
from qovery.model.cluster_request import ClusterRequest
from qovery.model.cluster import Cluster
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
    api_instance = clusters_api.ClustersApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    cluster_request = ClusterRequest(
        name="name_example",
        description="description_example",
        region="region_example",
        cloud_provider=CloudProviderEnum("AWS"),
        cloud_provider_credentials=ClusterCloudProviderInfoRequest(
            cloud_provider=CloudProviderEnum("AWS"),
            credentials=ClusterCloudProviderInfoCredentials(
                id="id_example",
                name="name_example",
            ),
            region="region_example",
        ),
        min_running_nodes=1,
        max_running_nodes=1,
        disk_size=50,
        instance_type="T3A_LARGE",
        kubernetes=KubernetesEnum("MANAGED"),
        production=True,
        ssh_keys=[
            "ssh_keys_example",
        ],
        kubeconfig="kubeconfig_example",
        features=[
            ClusterRequestFeaturesInner(
                id="id_example",
                value=ClusterFeatureValue(None),
            ),
        ],
    ) # ClusterRequest |  (optional)

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

[**Cluster**](Cluster.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

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

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import clusters_api
from qovery.model.cluster_delete_mode import ClusterDeleteMode
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
    api_instance = clusters_api.ClustersApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    cluster_id = "clusterId_example" # str | Cluster ID
    delete_mode = ClusterDeleteMode("DEFAULT") # ClusterDeleteMode |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete a cluster
        api_instance.delete_cluster(organization_id, cluster_id)
    except qovery.ApiException as e:
        print("Exception when calling ClustersApi->delete_cluster: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete a cluster
        api_instance.delete_cluster(organization_id, cluster_id, delete_mode=delete_mode)
    except qovery.ApiException as e:
        print("Exception when calling ClustersApi->delete_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **cluster_id** | **str**| Cluster ID |
 **delete_mode** | **ClusterDeleteMode**|  | [optional]

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

# **deploy_cluster**
> ClusterStatus deploy_cluster(organization_id, cluster_id)

Deploy a cluster

allows to deploy a cluster

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import clusters_api
from qovery.model.cluster_status import ClusterStatus
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

[**ClusterStatus**](ClusterStatus.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

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
> Cluster edit_cluster(organization_id, cluster_id)

Edit a cluster

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import clusters_api
from qovery.model.cluster_request import ClusterRequest
from qovery.model.cluster import Cluster
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
    api_instance = clusters_api.ClustersApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    cluster_id = "clusterId_example" # str | Cluster ID
    cluster_request = ClusterRequest(
        name="name_example",
        description="description_example",
        region="region_example",
        cloud_provider=CloudProviderEnum("AWS"),
        cloud_provider_credentials=ClusterCloudProviderInfoRequest(
            cloud_provider=CloudProviderEnum("AWS"),
            credentials=ClusterCloudProviderInfoCredentials(
                id="id_example",
                name="name_example",
            ),
            region="region_example",
        ),
        min_running_nodes=1,
        max_running_nodes=1,
        disk_size=50,
        instance_type="T3A_LARGE",
        kubernetes=KubernetesEnum("MANAGED"),
        production=True,
        ssh_keys=[
            "ssh_keys_example",
        ],
        kubeconfig="kubeconfig_example",
        features=[
            ClusterRequestFeaturesInner(
                id="id_example",
                value=ClusterFeatureValue(None),
            ),
        ],
    ) # ClusterRequest |  (optional)

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

[**Cluster**](Cluster.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

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

# **edit_cluster_advanced_settings**
> ClusterAdvancedSettings edit_cluster_advanced_settings(organization_id, cluster_id)

Edit advanced settings

Edit advanced settings by returning table of advanced settings.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import clusters_api
from qovery.model.cluster_advanced_settings import ClusterAdvancedSettings
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
    api_instance = clusters_api.ClustersApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    cluster_id = "clusterId_example" # str | Cluster ID
    cluster_advanced_settings = ClusterAdvancedSettings(
        aws_cloudwatch_eks_logs_retention_days=1,
        aws_vpc_enable_s3_flow_logs=True,
        aws_vpc_flow_logs_retention_days=1,
        loki_log_retention_in_week=1,
        registry_image_retention_time=1,
        cloud_provider_container_registry_tags={
            "key": "key_example",
        },
        load_balancer_size="load_balancer_size_example",
        database_postgresql_deny_public_access=True,
        database_postgresql_allowed_cidrs=[
            "database_postgresql_allowed_cidrs_example",
        ],
        database_mysql_deny_public_access=True,
        database_mysql_allowed_cidrs=[
            "database_mysql_allowed_cidrs_example",
        ],
        database_mongodb_deny_public_access=True,
        database_mongodb_allowed_cidrs=[
            "database_mongodb_allowed_cidrs_example",
        ],
        database_redis_deny_public_access=True,
        database_redis_allowed_cidrs=[
            "database_redis_allowed_cidrs_example",
        ],
        aws_iam_admin_group="aws_iam_admin_group_example",
        aws_eks_ec2_metadata_imds="optional",
        pleco_resources_ttl=1,
        registry_mirroring_mode=RegistryMirroringModeEnum("SERVICE"),
        nginx_vcpu_request_in_milli_cpu=1,
        nginx_vcpu_limit_in_milli_cpu=1,
        nginx_memory_request_in_mib=1,
        nginx_memory_limit_in_mib=1,
        nginx_hpa_cpu_utilization_percentage_threshold=1,
        nginx_hpa_min_number_instances=1,
        nginx_hpa_max_number_instances=1,
    ) # ClusterAdvancedSettings |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Edit advanced settings
        api_response = api_instance.edit_cluster_advanced_settings(organization_id, cluster_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ClustersApi->edit_cluster_advanced_settings: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit advanced settings
        api_response = api_instance.edit_cluster_advanced_settings(organization_id, cluster_id, cluster_advanced_settings=cluster_advanced_settings)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ClustersApi->edit_cluster_advanced_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **cluster_id** | **str**| Cluster ID |
 **cluster_advanced_settings** | [**ClusterAdvancedSettings**](ClusterAdvancedSettings.md)|  | [optional]

### Return type

[**ClusterAdvancedSettings**](ClusterAdvancedSettings.md)

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

# **edit_routing_table**
> ClusterRoutingTable edit_routing_table(organization_id, cluster_id)

Edit routing table

Edit routing table by returning updated table.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import clusters_api
from qovery.model.cluster_routing_table import ClusterRoutingTable
from qovery.model.cluster_routing_table_request import ClusterRoutingTableRequest
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
    api_instance = clusters_api.ClustersApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    cluster_id = "clusterId_example" # str | Cluster ID
    cluster_routing_table_request = ClusterRoutingTableRequest(
        routes=[
            ClusterRoutingTableResultsInner(
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

[**ClusterRoutingTable**](ClusterRoutingTable.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

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

# **get_cluster_advanced_settings**
> ClusterAdvancedSettings get_cluster_advanced_settings(organization_id, cluster_id)

Get advanced settings

Get the list and values of the advanced settings of the cluster. Default values for each setting are available in [our documentation](https://hub.qovery.com/docs/using-qovery/configuration/cluster-advanced-settings/) 

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import clusters_api
from qovery.model.cluster_advanced_settings import ClusterAdvancedSettings
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
    api_instance = clusters_api.ClustersApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    cluster_id = "clusterId_example" # str | Cluster ID

    # example passing only required values which don't have defaults set
    try:
        # Get advanced settings
        api_response = api_instance.get_cluster_advanced_settings(organization_id, cluster_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ClustersApi->get_cluster_advanced_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **cluster_id** | **str**| Cluster ID |

### Return type

[**ClusterAdvancedSettings**](ClusterAdvancedSettings.md)

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

# **get_cluster_kubeconfig**
> str get_cluster_kubeconfig(organization_id, cluster_id)

Get cluster kubeconfig

### Example

* Api Key Authentication (ApiKeyAuth):
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
    api_instance = clusters_api.ClustersApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    cluster_id = "clusterId_example" # str | Cluster ID

    # example passing only required values which don't have defaults set
    try:
        # Get cluster kubeconfig
        api_response = api_instance.get_cluster_kubeconfig(organization_id, cluster_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ClustersApi->get_cluster_kubeconfig: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **cluster_id** | **str**| Cluster ID |

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get kubeconfig of the cluster |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_readiness_status**
> ClusterReadinessStatus get_cluster_readiness_status(organization_id, cluster_id)

Know if a cluster is ready to be deployed or not

### Example

* Api Key Authentication (ApiKeyAuth):
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

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

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
> ClusterStatusGet get_cluster_status(organization_id, cluster_id)

Get cluster status

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import clusters_api
from qovery.model.cluster_status_get import ClusterStatusGet
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

[**ClusterStatusGet**](ClusterStatusGet.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

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

# **get_default_cluster_advanced_settings**
> ClusterAdvancedSettings get_default_cluster_advanced_settings()

List default cluster advanced settings

Default values for each setting are available in [our documentation](https://hub.qovery.com/docs/using-qovery/configuration/cluster-advanced-settings/)

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import clusters_api
from qovery.model.cluster_advanced_settings import ClusterAdvancedSettings
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
    api_instance = clusters_api.ClustersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List default cluster advanced settings
        api_response = api_instance.get_default_cluster_advanced_settings()
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ClustersApi->get_default_cluster_advanced_settings: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ClusterAdvancedSettings**](ClusterAdvancedSettings.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default cluster advanced settings |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_installation_helm_values**
> str get_installation_helm_values(organization_id, cluster_id)

Get cluster helm values for self managed installation

### Example

* Api Key Authentication (ApiKeyAuth):
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
    api_instance = clusters_api.ClustersApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    cluster_id = "clusterId_example" # str | Cluster ID

    # example passing only required values which don't have defaults set
    try:
        # Get cluster helm values for self managed installation
        api_response = api_instance.get_installation_helm_values(organization_id, cluster_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ClustersApi->get_installation_helm_values: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **cluster_id** | **str**| Cluster ID |

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-yaml


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Helm values |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_cloud_provider_info**
> ClusterCloudProviderInfo get_organization_cloud_provider_info(organization_id, cluster_id)

Get cluster cloud provider info and credentials

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import clusters_api
from qovery.model.cluster_cloud_provider_info import ClusterCloudProviderInfo
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

[**ClusterCloudProviderInfo**](ClusterCloudProviderInfo.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

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

* Api Key Authentication (ApiKeyAuth):
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

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

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
> ClusterRoutingTable get_routing_table(organization_id, cluster_id)

Get routing table

Retrieve network routing table where each line corresponds to a route between a destination and a target.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import clusters_api
from qovery.model.cluster_routing_table import ClusterRoutingTable
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

[**ClusterRoutingTable**](ClusterRoutingTable.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

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

# **list_cluster_logs**
> ClusterLogsResponseList list_cluster_logs(organization_id, cluster_id)

List Cluster Logs

List Cluster Logs

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import clusters_api
from qovery.model.cluster_logs_response_list import ClusterLogsResponseList
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
    api_instance = clusters_api.ClustersApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    cluster_id = "clusterId_example" # str | Cluster ID

    # example passing only required values which don't have defaults set
    try:
        # List Cluster Logs
        api_response = api_instance.list_cluster_logs(organization_id, cluster_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ClustersApi->list_cluster_logs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **cluster_id** | **str**| Cluster ID |

### Return type

[**ClusterLogsResponseList**](ClusterLogsResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | list cluster logs |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_organization_cluster**
> ClusterResponseList list_organization_cluster(organization_id)

List organization clusters

### Example

* Api Key Authentication (ApiKeyAuth):
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

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

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
> ClusterCloudProviderInfo specify_cluster_cloud_provider_info(organization_id, cluster_id)

Specify cluster cloud provider info and credentials

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import clusters_api
from qovery.model.cluster_cloud_provider_info_request import ClusterCloudProviderInfoRequest
from qovery.model.cluster_cloud_provider_info import ClusterCloudProviderInfo
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
    api_instance = clusters_api.ClustersApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    cluster_id = "clusterId_example" # str | Cluster ID
    cluster_cloud_provider_info_request = ClusterCloudProviderInfoRequest(
        cloud_provider=CloudProviderEnum("AWS"),
        credentials=ClusterCloudProviderInfoCredentials(
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

[**ClusterCloudProviderInfo**](ClusterCloudProviderInfo.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

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
> ClusterStatus stop_cluster(organization_id, cluster_id)

Stop cluster

Cluster stop has been requester.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import clusters_api
from qovery.model.cluster_status import ClusterStatus
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

[**ClusterStatus**](ClusterStatus.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

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

