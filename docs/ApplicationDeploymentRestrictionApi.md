# qovery.ApplicationDeploymentRestrictionApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_application_deployment_restriction**](ApplicationDeploymentRestrictionApi.md#create_application_deployment_restriction) | **POST** /application/{applicationId}/deploymentRestriction | Create an application deployment restriction
[**delete_application_deployment_restriction**](ApplicationDeploymentRestrictionApi.md#delete_application_deployment_restriction) | **DELETE** /application/{applicationId}/deploymentRestriction/{deploymentRestrictionId} | Delete an application deployment restriction
[**edit_application_deployment_restriction**](ApplicationDeploymentRestrictionApi.md#edit_application_deployment_restriction) | **PUT** /application/{applicationId}/deploymentRestriction/{deploymentRestrictionId} | Edit an application deployment restriction
[**get_application_deployment_restrictions**](ApplicationDeploymentRestrictionApi.md#get_application_deployment_restrictions) | **GET** /application/{applicationId}/deploymentRestriction | Get application deployment restrictions


# **create_application_deployment_restriction**
> ApplicationDeploymentRestriction create_application_deployment_restriction(application_id)

Create an application deployment restriction

Create an application deployment restriction

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import application_deployment_restriction_api
from qovery.model.application_deployment_restriction_request import ApplicationDeploymentRestrictionRequest
from qovery.model.application_deployment_restriction import ApplicationDeploymentRestriction
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
    api_instance = application_deployment_restriction_api.ApplicationDeploymentRestrictionApi(api_client)
    application_id = "applicationId_example" # str | Application ID
    application_deployment_restriction_request = ApplicationDeploymentRestrictionRequest(
        mode=DeploymentRestrictionModeEnum("MATCH"),
        type=DeploymentRestrictionTypeEnum("PATH"),
        value="application1/src/",
    ) # ApplicationDeploymentRestrictionRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create an application deployment restriction
        api_response = api_instance.create_application_deployment_restriction(application_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationDeploymentRestrictionApi->create_application_deployment_restriction: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an application deployment restriction
        api_response = api_instance.create_application_deployment_restriction(application_id, application_deployment_restriction_request=application_deployment_restriction_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationDeploymentRestrictionApi->create_application_deployment_restriction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID |
 **application_deployment_restriction_request** | [**ApplicationDeploymentRestrictionRequest**](ApplicationDeploymentRestrictionRequest.md)|  | [optional]

### Return type

[**ApplicationDeploymentRestriction**](ApplicationDeploymentRestriction.md)

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
**409** | An application deployment restriction with same properties already exists for this application |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_application_deployment_restriction**
> delete_application_deployment_restriction(application_id)

Delete an application deployment restriction

Delete an application deployment restriction

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import application_deployment_restriction_api
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
    api_instance = application_deployment_restriction_api.ApplicationDeploymentRestrictionApi(api_client)
    application_id = "applicationId_example" # str | Application ID

    # example passing only required values which don't have defaults set
    try:
        # Delete an application deployment restriction
        api_instance.delete_application_deployment_restriction(application_id)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationDeploymentRestrictionApi->delete_application_deployment_restriction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID |

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

# **edit_application_deployment_restriction**
> ApplicationDeploymentRestriction edit_application_deployment_restriction(application_id, deployment_restriction_id)

Edit an application deployment restriction

Edit an application deployment restriction

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import application_deployment_restriction_api
from qovery.model.application_deployment_restriction_request import ApplicationDeploymentRestrictionRequest
from qovery.model.application_deployment_restriction import ApplicationDeploymentRestriction
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
    api_instance = application_deployment_restriction_api.ApplicationDeploymentRestrictionApi(api_client)
    application_id = "applicationId_example" # str | Application ID
    deployment_restriction_id = "deploymentRestrictionId_example" # str | Deployment Restriction ID
    application_deployment_restriction_request = ApplicationDeploymentRestrictionRequest(
        mode=DeploymentRestrictionModeEnum("MATCH"),
        type=DeploymentRestrictionTypeEnum("PATH"),
        value="application1/src/",
    ) # ApplicationDeploymentRestrictionRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Edit an application deployment restriction
        api_response = api_instance.edit_application_deployment_restriction(application_id, deployment_restriction_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationDeploymentRestrictionApi->edit_application_deployment_restriction: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit an application deployment restriction
        api_response = api_instance.edit_application_deployment_restriction(application_id, deployment_restriction_id, application_deployment_restriction_request=application_deployment_restriction_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationDeploymentRestrictionApi->edit_application_deployment_restriction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID |
 **deployment_restriction_id** | **str**| Deployment Restriction ID |
 **application_deployment_restriction_request** | [**ApplicationDeploymentRestrictionRequest**](ApplicationDeploymentRestrictionRequest.md)|  | [optional]

### Return type

[**ApplicationDeploymentRestriction**](ApplicationDeploymentRestriction.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Edit an application deployment restriction |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_deployment_restrictions**
> ApplicationDeploymentRestrictionResponseList get_application_deployment_restrictions(application_id)

Get application deployment restrictions

Get application deployment restrictions

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import application_deployment_restriction_api
from qovery.model.application_deployment_restriction_response_list import ApplicationDeploymentRestrictionResponseList
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
    api_instance = application_deployment_restriction_api.ApplicationDeploymentRestrictionApi(api_client)
    application_id = "applicationId_example" # str | Application ID

    # example passing only required values which don't have defaults set
    try:
        # Get application deployment restrictions
        api_response = api_instance.get_application_deployment_restrictions(application_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationDeploymentRestrictionApi->get_application_deployment_restrictions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID |

### Return type

[**ApplicationDeploymentRestrictionResponseList**](ApplicationDeploymentRestrictionResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get application deployment restrictions |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

