# qovery.DeploymentStageMainCallsApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_service_to_deployment_stage**](DeploymentStageMainCallsApi.md#attach_service_to_deployment_stage) | **PUT** /deploymentStage/{deploymentStageId}/service/{serviceId} | Attach service to deployment stage
[**create_environment_deployment_stage**](DeploymentStageMainCallsApi.md#create_environment_deployment_stage) | **POST** /environment/{environmentId}/deploymentStage | Create environment deployment stage
[**delete_deployment_stage**](DeploymentStageMainCallsApi.md#delete_deployment_stage) | **DELETE** /deploymentStage/{deploymentStageId} | Delete deployment stage
[**edit_deployment_stage**](DeploymentStageMainCallsApi.md#edit_deployment_stage) | **PUT** /deploymentStage/{deploymentStageId} | Edit deployment stage
[**get_deployment_stage**](DeploymentStageMainCallsApi.md#get_deployment_stage) | **GET** /deploymentStage/{deploymentStageId} | Get Deployment Stage
[**get_service_deployment_stage**](DeploymentStageMainCallsApi.md#get_service_deployment_stage) | **GET** /service/{serviceId}/deploymentStage | Get Service Deployment Stage
[**list_environment_deployment_stage**](DeploymentStageMainCallsApi.md#list_environment_deployment_stage) | **GET** /environment/{environmentId}/deploymentStage | List environment deployment stage
[**move_deployment_stage**](DeploymentStageMainCallsApi.md#move_deployment_stage) | **PUT** /deploymentStage/{deploymentStageId}/moveBefore/{stageId} | Move deployment stage before requested stage


# **attach_service_to_deployment_stage**
> DeploymentStageResponseList attach_service_to_deployment_stage(deployment_stage_id)

Attach service to deployment stage

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import deployment_stage_main_calls_api
from qovery.model.deployment_stage_response_list import DeploymentStageResponseList
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
    api_instance = deployment_stage_main_calls_api.DeploymentStageMainCallsApi(api_client)
    deployment_stage_id = "deploymentStageId_example" # str | Deployment Stage ID

    # example passing only required values which don't have defaults set
    try:
        # Attach service to deployment stage
        api_response = api_instance.attach_service_to_deployment_stage(deployment_stage_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling DeploymentStageMainCallsApi->attach_service_to_deployment_stage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_stage_id** | **str**| Deployment Stage ID |

### Return type

[**DeploymentStageResponseList**](DeploymentStageResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of deployment stages for the env |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_environment_deployment_stage**
> DeploymentStageResponse create_environment_deployment_stage(environment_id)

Create environment deployment stage

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import deployment_stage_main_calls_api
from qovery.model.deployment_stage_response import DeploymentStageResponse
from qovery.model.deployment_stage_request import DeploymentStageRequest
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
    api_instance = deployment_stage_main_calls_api.DeploymentStageMainCallsApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID
    deployment_stage_request = DeploymentStageRequest(
        name="name_example",
        description="description_example",
    ) # DeploymentStageRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create environment deployment stage
        api_response = api_instance.create_environment_deployment_stage(environment_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling DeploymentStageMainCallsApi->create_environment_deployment_stage: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create environment deployment stage
        api_response = api_instance.create_environment_deployment_stage(environment_id, deployment_stage_request=deployment_stage_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling DeploymentStageMainCallsApi->create_environment_deployment_stage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID |
 **deployment_stage_request** | [**DeploymentStageRequest**](DeploymentStageRequest.md)|  | [optional]

### Return type

[**DeploymentStageResponse**](DeploymentStageResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | created deployment stage |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_deployment_stage**
> delete_deployment_stage(deployment_stage_id)

Delete deployment stage

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import deployment_stage_main_calls_api
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
    api_instance = deployment_stage_main_calls_api.DeploymentStageMainCallsApi(api_client)
    deployment_stage_id = "deploymentStageId_example" # str | Deployment Stage ID

    # example passing only required values which don't have defaults set
    try:
        # Delete deployment stage
        api_instance.delete_deployment_stage(deployment_stage_id)
    except qovery.ApiException as e:
        print("Exception when calling DeploymentStageMainCallsApi->delete_deployment_stage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_stage_id** | **str**| Deployment Stage ID |

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
**204** | no content |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_deployment_stage**
> DeploymentStageResponse edit_deployment_stage(deployment_stage_id)

Edit deployment stage

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import deployment_stage_main_calls_api
from qovery.model.deployment_stage_response import DeploymentStageResponse
from qovery.model.deployment_stage_request import DeploymentStageRequest
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
    api_instance = deployment_stage_main_calls_api.DeploymentStageMainCallsApi(api_client)
    deployment_stage_id = "deploymentStageId_example" # str | Deployment Stage ID
    deployment_stage_request = DeploymentStageRequest(
        name="name_example",
        description="description_example",
    ) # DeploymentStageRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Edit deployment stage
        api_response = api_instance.edit_deployment_stage(deployment_stage_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling DeploymentStageMainCallsApi->edit_deployment_stage: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit deployment stage
        api_response = api_instance.edit_deployment_stage(deployment_stage_id, deployment_stage_request=deployment_stage_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling DeploymentStageMainCallsApi->edit_deployment_stage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_stage_id** | **str**| Deployment Stage ID |
 **deployment_stage_request** | [**DeploymentStageRequest**](DeploymentStageRequest.md)|  | [optional]

### Return type

[**DeploymentStageResponse**](DeploymentStageResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | created deployment stage |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deployment_stage**
> DeploymentStageResponse get_deployment_stage(deployment_stage_id)

Get Deployment Stage

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import deployment_stage_main_calls_api
from qovery.model.deployment_stage_response import DeploymentStageResponse
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
    api_instance = deployment_stage_main_calls_api.DeploymentStageMainCallsApi(api_client)
    deployment_stage_id = "deploymentStageId_example" # str | Deployment Stage ID

    # example passing only required values which don't have defaults set
    try:
        # Get Deployment Stage
        api_response = api_instance.get_deployment_stage(deployment_stage_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling DeploymentStageMainCallsApi->get_deployment_stage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_stage_id** | **str**| Deployment Stage ID |

### Return type

[**DeploymentStageResponse**](DeploymentStageResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Deployment Stage |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_deployment_stage**
> DeploymentStageResponse get_service_deployment_stage(service_id)

Get Service Deployment Stage

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import deployment_stage_main_calls_api
from qovery.model.deployment_stage_response import DeploymentStageResponse
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
    api_instance = deployment_stage_main_calls_api.DeploymentStageMainCallsApi(api_client)
    service_id = "serviceId_example" # str | Service ID of an application/job/container/database

    # example passing only required values which don't have defaults set
    try:
        # Get Service Deployment Stage
        api_response = api_instance.get_service_deployment_stage(service_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling DeploymentStageMainCallsApi->get_service_deployment_stage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Service ID of an application/job/container/database |

### Return type

[**DeploymentStageResponse**](DeploymentStageResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Service Deployment Stage |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_environment_deployment_stage**
> DeploymentStageResponseList list_environment_deployment_stage(environment_id)

List environment deployment stage

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import deployment_stage_main_calls_api
from qovery.model.deployment_stage_response_list import DeploymentStageResponseList
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
    api_instance = deployment_stage_main_calls_api.DeploymentStageMainCallsApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID

    # example passing only required values which don't have defaults set
    try:
        # List environment deployment stage
        api_response = api_instance.list_environment_deployment_stage(environment_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling DeploymentStageMainCallsApi->list_environment_deployment_stage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID |

### Return type

[**DeploymentStageResponseList**](DeploymentStageResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List deployment stage |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_deployment_stage**
> DeploymentStageResponseList move_deployment_stage(deployment_stage_id, stage_id)

Move deployment stage before requested stage

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import deployment_stage_main_calls_api
from qovery.model.deployment_stage_response_list import DeploymentStageResponseList
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
    api_instance = deployment_stage_main_calls_api.DeploymentStageMainCallsApi(api_client)
    deployment_stage_id = "deploymentStageId_example" # str | Deployment Stage ID
    stage_id = "stageId_example" # str | Deployment Stage ID

    # example passing only required values which don't have defaults set
    try:
        # Move deployment stage before requested stage
        api_response = api_instance.move_deployment_stage(deployment_stage_id, stage_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling DeploymentStageMainCallsApi->move_deployment_stage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_stage_id** | **str**| Deployment Stage ID |
 **stage_id** | **str**| Deployment Stage ID |

### Return type

[**DeploymentStageResponseList**](DeploymentStageResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List deployment stage |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

