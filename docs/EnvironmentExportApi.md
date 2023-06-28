# qovery.EnvironmentExportApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_environment_configuration_into_terraform**](EnvironmentExportApi.md#export_environment_configuration_into_terraform) | **GET** /environment/{environmentId}/terraformExport | Export full environment and its resources into Terraform manifests


# **export_environment_configuration_into_terraform**
> file_type export_environment_configuration_into_terraform(environment_id)

Export full environment and its resources into Terraform manifests

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import environment_export_api
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
    api_instance = environment_export_api.EnvironmentExportApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID
    export_secrets = False # bool | export Secrets from configuration and include them into Terraform export (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Export full environment and its resources into Terraform manifests
        api_response = api_instance.export_environment_configuration_into_terraform(environment_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling EnvironmentExportApi->export_environment_configuration_into_terraform: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export full environment and its resources into Terraform manifests
        api_response = api_instance.export_environment_configuration_into_terraform(environment_id, export_secrets=export_secrets)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling EnvironmentExportApi->export_environment_configuration_into_terraform: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID |
 **export_secrets** | **bool**| export Secrets from configuration and include them into Terraform export | [optional] if omitted the server will use the default value of False

### Return type

**file_type**

### Authorization

[bearerAuth](../README.md#bearerAuth)

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

