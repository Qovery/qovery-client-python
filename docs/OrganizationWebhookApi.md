# qovery.OrganizationWebhookApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_organization_webhook**](OrganizationWebhookApi.md#create_organization_webhook) | **POST** /organization/{organizationId}/webhook | Create an organization webhook
[**delete_organization_webhook**](OrganizationWebhookApi.md#delete_organization_webhook) | **DELETE** /organization/{organizationId}/webhook/{webhookId} | Delete organization webhook
[**edit_organization_webhook**](OrganizationWebhookApi.md#edit_organization_webhook) | **PUT** /organization/{organizationId}/webhook/{webhookId} | Edit an organization webhook
[**get_organization_webhook**](OrganizationWebhookApi.md#get_organization_webhook) | **GET** /organization/{organizationId}/webhook/{webhookId} | Get an Organization webhook
[**list_organization_web_hooks**](OrganizationWebhookApi.md#list_organization_web_hooks) | **GET** /organization/{organizationId}/webhook | List organization webhooks


# **create_organization_webhook**
> OrganizationWebhookCreateResponse create_organization_webhook(organization_id, organization_webhook_create_request=organization_webhook_create_request)

Create an organization webhook

Create an organization webhook.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import qovery
from qovery.models.organization_webhook_create_request import OrganizationWebhookCreateRequest
from qovery.models.organization_webhook_create_response import OrganizationWebhookCreateResponse
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
    api_instance = qovery.OrganizationWebhookApi(api_client)
    organization_id = 'organization_id_example' # str | Organization ID
    organization_webhook_create_request = qovery.OrganizationWebhookCreateRequest() # OrganizationWebhookCreateRequest |  (optional)

    try:
        # Create an organization webhook
        api_response = api_instance.create_organization_webhook(organization_id, organization_webhook_create_request=organization_webhook_create_request)
        print("The response of OrganizationWebhookApi->create_organization_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationWebhookApi->create_organization_webhook: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID | 
 **organization_webhook_create_request** | [**OrganizationWebhookCreateRequest**](OrganizationWebhookCreateRequest.md)|  | [optional] 

### Return type

[**OrganizationWebhookCreateResponse**](OrganizationWebhookCreateResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Organization webhook created |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_organization_webhook**
> delete_organization_webhook(organization_id, webhook_id)

Delete organization webhook

Delete organization webhook

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
    api_instance = qovery.OrganizationWebhookApi(api_client)
    organization_id = 'organization_id_example' # str | Organization ID
    webhook_id = 'webhook_id_example' # str | Webhook ID

    try:
        # Delete organization webhook
        api_instance.delete_organization_webhook(organization_id, webhook_id)
    except Exception as e:
        print("Exception when calling OrganizationWebhookApi->delete_organization_webhook: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID | 
 **webhook_id** | **str**| Webhook ID | 

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
**204** | no content |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_organization_webhook**
> OrganizationWebhookCreateResponse edit_organization_webhook(organization_id, webhook_id, organization_webhook_create_request=organization_webhook_create_request)

Edit an organization webhook

Edit an organization webhook

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import qovery
from qovery.models.organization_webhook_create_request import OrganizationWebhookCreateRequest
from qovery.models.organization_webhook_create_response import OrganizationWebhookCreateResponse
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
    api_instance = qovery.OrganizationWebhookApi(api_client)
    organization_id = 'organization_id_example' # str | Organization ID
    webhook_id = 'webhook_id_example' # str | Webhook ID
    organization_webhook_create_request = qovery.OrganizationWebhookCreateRequest() # OrganizationWebhookCreateRequest |  (optional)

    try:
        # Edit an organization webhook
        api_response = api_instance.edit_organization_webhook(organization_id, webhook_id, organization_webhook_create_request=organization_webhook_create_request)
        print("The response of OrganizationWebhookApi->edit_organization_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationWebhookApi->edit_organization_webhook: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID | 
 **webhook_id** | **str**| Webhook ID | 
 **organization_webhook_create_request** | [**OrganizationWebhookCreateRequest**](OrganizationWebhookCreateRequest.md)|  | [optional] 

### Return type

[**OrganizationWebhookCreateResponse**](OrganizationWebhookCreateResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Edit an organization webhook |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_webhook**
> OrganizationWebhookResponse get_organization_webhook(organization_id, webhook_id)

Get an Organization webhook

Get an Organization webhook

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import qovery
from qovery.models.organization_webhook_response import OrganizationWebhookResponse
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
    api_instance = qovery.OrganizationWebhookApi(api_client)
    organization_id = 'organization_id_example' # str | Organization ID
    webhook_id = 'webhook_id_example' # str | Webhook ID

    try:
        # Get an Organization webhook
        api_response = api_instance.get_organization_webhook(organization_id, webhook_id)
        print("The response of OrganizationWebhookApi->get_organization_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationWebhookApi->get_organization_webhook: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID | 
 **webhook_id** | **str**| Webhook ID | 

### Return type

[**OrganizationWebhookResponse**](OrganizationWebhookResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get organization webhook |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_organization_web_hooks**
> OrganizationWebhookResponseList list_organization_web_hooks(organization_id)

List organization webhooks

List organization webhooks

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import qovery
from qovery.models.organization_webhook_response_list import OrganizationWebhookResponseList
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
    api_instance = qovery.OrganizationWebhookApi(api_client)
    organization_id = 'organization_id_example' # str | Organization ID

    try:
        # List organization webhooks
        api_response = api_instance.list_organization_web_hooks(organization_id)
        print("The response of OrganizationWebhookApi->list_organization_web_hooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationWebhookApi->list_organization_web_hooks: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID | 

### Return type

[**OrganizationWebhookResponseList**](OrganizationWebhookResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List organization webhooks |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

