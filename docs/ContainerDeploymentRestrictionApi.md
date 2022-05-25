# qovery.ContainerDeploymentRestrictionApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_container_deployment_restriction**](ContainerDeploymentRestrictionApi.md#create_container_deployment_restriction) | **POST** /container/{containerId}/deploymentRestriction | Create an container deployment restriction
[**delete_container_deployment_restriction**](ContainerDeploymentRestrictionApi.md#delete_container_deployment_restriction) | **DELETE** /container/{containerId}/deploymentRestriction/{deploymentRestrictionId} | Delete a container deployment restriction
[**edit_container_deployment_restriction**](ContainerDeploymentRestrictionApi.md#edit_container_deployment_restriction) | **PUT** /container/{containerId}/deploymentRestriction/{deploymentRestrictionId} | Edit a container deployment restriction
[**get_container_deployment_restrictions**](ContainerDeploymentRestrictionApi.md#get_container_deployment_restrictions) | **GET** /container/{containerId}/deploymentRestriction | Get container deployment restrictions


# **create_container_deployment_restriction**
> ContainerDeploymentRestriction create_container_deployment_restriction(container_id)

Create an container deployment restriction

Create an container deployment restriction

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import container_deployment_restriction_api
from qovery.model.container_deployment_restriction import ContainerDeploymentRestriction
from qovery.model.container_deployment_restriction_request import ContainerDeploymentRestrictionRequest
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
    api_instance = container_deployment_restriction_api.ContainerDeploymentRestrictionApi(api_client)
    container_id = "containerId_example" # str | Container ID
    container_deployment_restriction_request = ContainerDeploymentRestrictionRequest(
        mode=DeploymentRestrictionModeEnum("MATCH"),
        type=DeploymentRestrictionTypeEnum("PATH"),
        value="application1/src/",
    ) # ContainerDeploymentRestrictionRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create an container deployment restriction
        api_response = api_instance.create_container_deployment_restriction(container_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainerDeploymentRestrictionApi->create_container_deployment_restriction: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an container deployment restriction
        api_response = api_instance.create_container_deployment_restriction(container_id, container_deployment_restriction_request=container_deployment_restriction_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainerDeploymentRestrictionApi->create_container_deployment_restriction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Container ID |
 **container_deployment_restriction_request** | [**ContainerDeploymentRestrictionRequest**](ContainerDeploymentRestrictionRequest.md)|  | [optional]

### Return type

[**ContainerDeploymentRestriction**](ContainerDeploymentRestriction.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Added an environment variable |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**409** | An Container deployment restriction with same properties already exists for this Container |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_container_deployment_restriction**
> delete_container_deployment_restriction(container_id)

Delete a container deployment restriction

Delete a container deployment restriction

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import container_deployment_restriction_api
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
    api_instance = container_deployment_restriction_api.ContainerDeploymentRestrictionApi(api_client)
    container_id = "containerId_example" # str | Container ID

    # example passing only required values which don't have defaults set
    try:
        # Delete a container deployment restriction
        api_instance.delete_container_deployment_restriction(container_id)
    except qovery.ApiException as e:
        print("Exception when calling ContainerDeploymentRestrictionApi->delete_container_deployment_restriction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Container ID |

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

# **edit_container_deployment_restriction**
> ContainerDeploymentRestriction edit_container_deployment_restriction(container_id, deployment_restriction_id)

Edit a container deployment restriction

Edit a container deployment restriction

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import container_deployment_restriction_api
from qovery.model.container_deployment_restriction import ContainerDeploymentRestriction
from qovery.model.container_deployment_restriction_request import ContainerDeploymentRestrictionRequest
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
    api_instance = container_deployment_restriction_api.ContainerDeploymentRestrictionApi(api_client)
    container_id = "containerId_example" # str | Container ID
    deployment_restriction_id = "deploymentRestrictionId_example" # str | Deployment Restriction ID
    container_deployment_restriction_request = ContainerDeploymentRestrictionRequest(
        mode=DeploymentRestrictionModeEnum("MATCH"),
        type=DeploymentRestrictionTypeEnum("PATH"),
        value="application1/src/",
    ) # ContainerDeploymentRestrictionRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Edit a container deployment restriction
        api_response = api_instance.edit_container_deployment_restriction(container_id, deployment_restriction_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainerDeploymentRestrictionApi->edit_container_deployment_restriction: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit a container deployment restriction
        api_response = api_instance.edit_container_deployment_restriction(container_id, deployment_restriction_id, container_deployment_restriction_request=container_deployment_restriction_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainerDeploymentRestrictionApi->edit_container_deployment_restriction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Container ID |
 **deployment_restriction_id** | **str**| Deployment Restriction ID |
 **container_deployment_restriction_request** | [**ContainerDeploymentRestrictionRequest**](ContainerDeploymentRestrictionRequest.md)|  | [optional]

### Return type

[**ContainerDeploymentRestriction**](ContainerDeploymentRestriction.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Edit a container deployment restriction |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_container_deployment_restrictions**
> ContainerDeploymentRestrictionResponseList get_container_deployment_restrictions(container_id)

Get container deployment restrictions

Get container deployment restrictions

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import container_deployment_restriction_api
from qovery.model.container_deployment_restriction_response_list import ContainerDeploymentRestrictionResponseList
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
    api_instance = container_deployment_restriction_api.ContainerDeploymentRestrictionApi(api_client)
    container_id = "containerId_example" # str | Container ID

    # example passing only required values which don't have defaults set
    try:
        # Get container deployment restrictions
        api_response = api_instance.get_container_deployment_restrictions(container_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainerDeploymentRestrictionApi->get_container_deployment_restrictions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **container_id** | **str**| Container ID |

### Return type

[**ContainerDeploymentRestrictionResponseList**](ContainerDeploymentRestrictionResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get container deployment restrictions |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

