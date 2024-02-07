# qovery.EnvironmentExportApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_environment_configuration_into_terraform**](EnvironmentExportApi.md#export_environment_configuration_into_terraform) | **GET** /environment/{environmentId}/terraformExport | Export full environment and its resources into Terraform manifests


# **export_environment_configuration_into_terraform**
> bytearray export_environment_configuration_into_terraform(environment_id, export_secrets=export_secrets)

Export full environment and its resources into Terraform manifests

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
    api_instance = qovery.EnvironmentExportApi(api_client)
    environment_id = 'environment_id_example' # str | Environment ID
    export_secrets = False # bool | export Secrets from configuration and include them into Terraform export (optional) (default to False)

    try:
        # Export full environment and its resources into Terraform manifests
        api_response = api_instance.export_environment_configuration_into_terraform(environment_id, export_secrets=export_secrets)
        print("The response of EnvironmentExportApi->export_environment_configuration_into_terraform:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentExportApi->export_environment_configuration_into_terraform: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID | 
 **export_secrets** | **bool**| export Secrets from configuration and include them into Terraform export | [optional] [default to False]

### Return type

**bytearray**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/zip

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Export full environment and its resources into Terraform manifests |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

