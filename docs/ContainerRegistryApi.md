# qovery.ContainerRegistryApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edit_container_registry**](ContainerRegistryApi.md#edit_container_registry) | **PUT** /organization/{organizationId}/containerRegistry/{containerRegistryId} | Edit a container registry


# **edit_container_registry**
> ContainerRegistryResponse edit_container_registry(organization_id)

Edit a container registry

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import container_registry_api
from qovery.model.container_registry_request import ContainerRegistryRequest
from qovery.model.container_registry_response import ContainerRegistryResponse
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
    api_instance = container_registry_api.ContainerRegistryApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    container_registry_request = ContainerRegistryRequest(
        name="name_example",
        kind=ContainerRegistryKindEnum("ECR"),
        description="description_example",
        url="url_example",
        config={},
    ) # ContainerRegistryRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Edit a container registry
        api_response = api_instance.edit_container_registry(organization_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainerRegistryApi->edit_container_registry: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit a container registry
        api_response = api_instance.edit_container_registry(organization_id, container_registry_request=container_registry_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ContainerRegistryApi->edit_container_registry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **container_registry_request** | [**ContainerRegistryRequest**](ContainerRegistryRequest.md)|  | [optional]

### Return type

[**ContainerRegistryResponse**](ContainerRegistryResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Edited the container registry |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

