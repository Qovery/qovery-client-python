# qovery.EnvironmentDeploymentRuleApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edit_environment_deployment_rule**](EnvironmentDeploymentRuleApi.md#edit_environment_deployment_rule) | **PUT** /environment/{environmentId}/deploymentRule/{deploymentRuleId} | Edit an environment deployment rule
[**get_environment_deployment_rule**](EnvironmentDeploymentRuleApi.md#get_environment_deployment_rule) | **GET** /environment/{environmentId}/deploymentRule | Get environment deployment rule


# **edit_environment_deployment_rule**
> EnvironmentDeploymentRule edit_environment_deployment_rule(environment_id, deployment_rule_id, environment_deployment_rule_edit_request=environment_deployment_rule_edit_request)

Edit an environment deployment rule

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import qovery
from qovery.models.environment_deployment_rule import EnvironmentDeploymentRule
from qovery.models.environment_deployment_rule_edit_request import EnvironmentDeploymentRuleEditRequest
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
    api_instance = qovery.EnvironmentDeploymentRuleApi(api_client)
    environment_id = 'environment_id_example' # str | Environment ID
    deployment_rule_id = 'deployment_rule_id_example' # str | Deployment Rule ID
    environment_deployment_rule_edit_request = qovery.EnvironmentDeploymentRuleEditRequest() # EnvironmentDeploymentRuleEditRequest |  (optional)

    try:
        # Edit an environment deployment rule
        api_response = api_instance.edit_environment_deployment_rule(environment_id, deployment_rule_id, environment_deployment_rule_edit_request=environment_deployment_rule_edit_request)
        print("The response of EnvironmentDeploymentRuleApi->edit_environment_deployment_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentDeploymentRuleApi->edit_environment_deployment_rule: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID | 
 **deployment_rule_id** | **str**| Deployment Rule ID | 
 **environment_deployment_rule_edit_request** | [**EnvironmentDeploymentRuleEditRequest**](EnvironmentDeploymentRuleEditRequest.md)|  | [optional] 

### Return type

[**EnvironmentDeploymentRule**](EnvironmentDeploymentRule.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Edit environment deployment rule |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_environment_deployment_rule**
> EnvironmentDeploymentRule get_environment_deployment_rule(environment_id)

Get environment deployment rule

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import os
import qovery
from qovery.models.environment_deployment_rule import EnvironmentDeploymentRule
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
    api_instance = qovery.EnvironmentDeploymentRuleApi(api_client)
    environment_id = 'environment_id_example' # str | Environment ID

    try:
        # Get environment deployment rule
        api_response = api_instance.get_environment_deployment_rule(environment_id)
        print("The response of EnvironmentDeploymentRuleApi->get_environment_deployment_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EnvironmentDeploymentRuleApi->get_environment_deployment_rule: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID | 

### Return type

[**EnvironmentDeploymentRule**](EnvironmentDeploymentRule.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get deployment rule |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

