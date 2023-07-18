# qovery.VariableMainCallsApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_variable_alias**](VariableMainCallsApi.md#create_variable_alias) | **POST** /variable/{variableId}/alias | Create a variable alias


# **create_variable_alias**
> VariableResponse create_variable_alias(variable_id)

Create a variable alias

- Allows you to add an alias at the level defined in the request body on an existing variable having a higher scope, in order to customize its key. - You have to specify a key in the request body and the scope and the parent id of the alias - The system will create a new variable at the requested level with the same value as the one corresponding to the variable id in the path - The response body will contain the newly created variable - Information regarding the aliased_variable will be exposed in the \"aliased_variable\" or in the \"aliased_secret\" field of the newly created variable - Only 1 alias level is allowed. You can't create an alias on an alias 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import variable_main_calls_api
from qovery.model.variable_response import VariableResponse
from qovery.model.variable_alias_request import VariableAliasRequest
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
    api_instance = variable_main_calls_api.VariableMainCallsApi(api_client)
    variable_id = "variableId_example" # str | Variable ID
    variable_alias_request = VariableAliasRequest(
        key="key_example",
        alias_scope=APIVariableScopeEnum("APPLICATION"),
        alias_parent_id="alias_parent_id_example",
    ) # VariableAliasRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a variable alias
        api_response = api_instance.create_variable_alias(variable_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling VariableMainCallsApi->create_variable_alias: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a variable alias
        api_response = api_instance.create_variable_alias(variable_id, variable_alias_request=variable_alias_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling VariableMainCallsApi->create_variable_alias: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variable_id** | **str**| Variable ID |
 **variable_alias_request** | [**VariableAliasRequest**](VariableAliasRequest.md)|  | [optional]

### Return type

[**VariableResponse**](VariableResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create variable alias |  -  |
**400** | Can&#39;t create an alias on a higher scope. Aliases can only be created from one scope to a lower scope. Scope hierarchy is ORGANIZATION &gt; PROJECT &gt; ENVIRONMENT &gt; CONTAINER |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

