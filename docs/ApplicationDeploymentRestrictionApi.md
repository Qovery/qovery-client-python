# qovery.ApplicationDeploymentRestrictionApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_application_deployment_restriction**](ApplicationDeploymentRestrictionApi.md#create_application_deployment_restriction) | **POST** /application/{applicationId}/deploymentRestriction | Create an application deployment restriction
[**delete_application_deployment_restriction**](ApplicationDeploymentRestrictionApi.md#delete_application_deployment_restriction) | **DELETE** /application/{applicationId}/deploymentRestriction/{deploymentRestrictionId} | Delete an application deployment restriction
[**edit_application_deployment_restriction**](ApplicationDeploymentRestrictionApi.md#edit_application_deployment_restriction) | **PUT** /application/{applicationId}/deploymentRestriction/{deploymentRestrictionId} | Edit an application deployment restriction
[**get_application_deployment_restrictions**](ApplicationDeploymentRestrictionApi.md#get_application_deployment_restrictions) | **GET** /application/{applicationId}/deploymentRestriction | Get application deployment restrictions


# **create_application_deployment_restriction**
> ApplicationDeploymentRestriction create_application_deployment_restriction(application_id, application_deployment_restriction_request=application_deployment_restriction_request)

Create an application deployment restriction

Create an application deployment restriction

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import qovery
from qovery.models.application_deployment_restriction import ApplicationDeploymentRestriction
from qovery.models.application_deployment_restriction_request import ApplicationDeploymentRestrictionRequest
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
    api_instance = qovery.ApplicationDeploymentRestrictionApi(api_client)
    application_id = 'application_id_example' # str | Application ID
    application_deployment_restriction_request = qovery.ApplicationDeploymentRestrictionRequest() # ApplicationDeploymentRestrictionRequest |  (optional)

    try:
        # Create an application deployment restriction
        api_response = api_instance.create_application_deployment_restriction(application_id, application_deployment_restriction_request=application_deployment_restriction_request)
        print("The response of ApplicationDeploymentRestrictionApi->create_application_deployment_restriction:\n")
        pprint(api_response)
    except Exception as e:
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

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

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
> delete_application_deployment_restriction(application_id, deployment_restriction_id)

Delete an application deployment restriction

Delete an application deployment restriction

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import qovery
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
    api_instance = qovery.ApplicationDeploymentRestrictionApi(api_client)
    application_id = 'application_id_example' # str | Application ID
    deployment_restriction_id = 'deployment_restriction_id_example' # str | Deployment Restriction ID

    try:
        # Delete an application deployment restriction
        api_instance.delete_application_deployment_restriction(application_id, deployment_restriction_id)
    except Exception as e:
        print("Exception when calling ApplicationDeploymentRestrictionApi->delete_application_deployment_restriction: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID | 
 **deployment_restriction_id** | **str**| Deployment Restriction ID | 

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

# **edit_application_deployment_restriction**
> ApplicationDeploymentRestriction edit_application_deployment_restriction(application_id, deployment_restriction_id, application_deployment_restriction_request=application_deployment_restriction_request)

Edit an application deployment restriction

Edit an application deployment restriction

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import qovery
from qovery.models.application_deployment_restriction import ApplicationDeploymentRestriction
from qovery.models.application_deployment_restriction_request import ApplicationDeploymentRestrictionRequest
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
    api_instance = qovery.ApplicationDeploymentRestrictionApi(api_client)
    application_id = 'application_id_example' # str | Application ID
    deployment_restriction_id = 'deployment_restriction_id_example' # str | Deployment Restriction ID
    application_deployment_restriction_request = qovery.ApplicationDeploymentRestrictionRequest() # ApplicationDeploymentRestrictionRequest |  (optional)

    try:
        # Edit an application deployment restriction
        api_response = api_instance.edit_application_deployment_restriction(application_id, deployment_restriction_id, application_deployment_restriction_request=application_deployment_restriction_request)
        print("The response of ApplicationDeploymentRestrictionApi->edit_application_deployment_restriction:\n")
        pprint(api_response)
    except Exception as e:
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

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

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

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import qovery
from qovery.models.application_deployment_restriction_response_list import ApplicationDeploymentRestrictionResponseList
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
    api_instance = qovery.ApplicationDeploymentRestrictionApi(api_client)
    application_id = 'application_id_example' # str | Application ID

    try:
        # Get application deployment restrictions
        api_response = api_instance.get_application_deployment_restrictions(application_id)
        print("The response of ApplicationDeploymentRestrictionApi->get_application_deployment_restrictions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationDeploymentRestrictionApi->get_application_deployment_restrictions: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID | 

### Return type

[**ApplicationDeploymentRestrictionResponseList**](ApplicationDeploymentRestrictionResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

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

