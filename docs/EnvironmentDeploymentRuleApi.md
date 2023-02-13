# qovery.EnvironmentDeploymentRuleApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edit_environment_deployment_rule**](EnvironmentDeploymentRuleApi.md#edit_environment_deployment_rule) | **PUT** /environment/{environmentId}/deploymentRule/{deploymentRuleId} | Edit an environment deployment rule
[**get_environment_deployment_rule**](EnvironmentDeploymentRuleApi.md#get_environment_deployment_rule) | **GET** /environment/{environmentId}/deploymentRule | Get environment deployment rule


# **edit_environment_deployment_rule**
> EnvironmentDeploymentRule edit_environment_deployment_rule(environment_id, deployment_rule_id)

Edit an environment deployment rule

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import environment_deployment_rule_api
from qovery.model.environment_deployment_rule import EnvironmentDeploymentRule
from qovery.model.environment_deployment_rule_edit_request import EnvironmentDeploymentRuleEditRequest
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
    api_instance = environment_deployment_rule_api.EnvironmentDeploymentRuleApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID
    deployment_rule_id = "deploymentRuleId_example" # str | Deployment Rule ID
    environment_deployment_rule_edit_request = EnvironmentDeploymentRuleEditRequest(
        auto_deploy=True,
        auto_delete=False,
        auto_stop=False,
        timezone="UTC",
        start_time=dateutil_parser('1970-01-01T08:00:00Z'),
        stop_time=dateutil_parser('1970-01-01T19:00:00Z'),
        weekdays=[
            WeekdayEnum("MONDAY"),
        ],
    ) # EnvironmentDeploymentRuleEditRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Edit an environment deployment rule
        api_response = api_instance.edit_environment_deployment_rule(environment_id, deployment_rule_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling EnvironmentDeploymentRuleApi->edit_environment_deployment_rule: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit an environment deployment rule
        api_response = api_instance.edit_environment_deployment_rule(environment_id, deployment_rule_id, environment_deployment_rule_edit_request=environment_deployment_rule_edit_request)
        pprint(api_response)
    except qovery.ApiException as e:
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

[bearerAuth](../README.md#bearerAuth)

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

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import environment_deployment_rule_api
from qovery.model.environment_deployment_rule import EnvironmentDeploymentRule
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
    api_instance = environment_deployment_rule_api.EnvironmentDeploymentRuleApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID

    # example passing only required values which don't have defaults set
    try:
        # Get environment deployment rule
        api_response = api_instance.get_environment_deployment_rule(environment_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling EnvironmentDeploymentRuleApi->get_environment_deployment_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID |

### Return type

[**EnvironmentDeploymentRule**](EnvironmentDeploymentRule.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

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

