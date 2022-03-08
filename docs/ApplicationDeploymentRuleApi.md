# qovery.ApplicationDeploymentRuleApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edit_application_deployment_rule**](ApplicationDeploymentRuleApi.md#edit_application_deployment_rule) | **PUT** /application/{applicationId}/deploymentRule/{deploymentRuleId} | Edit an application deployment rule
[**get_application_deployment_rule**](ApplicationDeploymentRuleApi.md#get_application_deployment_rule) | **GET** /application/{applicationId}/deploymentRule | Get application deployment rule


# **edit_application_deployment_rule**
> ApplicationDeploymentRuleResponse edit_application_deployment_rule(application_id, deployment_rule_id)

Edit an application deployment rule

Edit an application deployment rule

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import application_deployment_rule_api
from qovery.model.application_deployment_rule_edit_request import ApplicationDeploymentRuleEditRequest
from qovery.model.application_deployment_rule_response import ApplicationDeploymentRuleResponse
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
    api_instance = application_deployment_rule_api.ApplicationDeploymentRuleApi(api_client)
    application_id = "applicationId_example" # str | Application ID
    deployment_rule_id = "deploymentRuleId_example" # str | Deployment Rule ID
    application_deployment_rule_edit_request = ApplicationDeploymentRuleEditRequest(
        deployment_restrictions=[
            ApplicationDeploymentRestriction(
                mode=DeploymentRestrictionModeEnum("MATCH"),
                type=DeploymentRestrictionTypeEnum("PATH"),
                value="value_example",
            ),
        ],
    ) # ApplicationDeploymentRuleEditRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Edit an application deployment rule
        api_response = api_instance.edit_application_deployment_rule(application_id, deployment_rule_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationDeploymentRuleApi->edit_application_deployment_rule: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit an application deployment rule
        api_response = api_instance.edit_application_deployment_rule(application_id, deployment_rule_id, application_deployment_rule_edit_request=application_deployment_rule_edit_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationDeploymentRuleApi->edit_application_deployment_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID |
 **deployment_rule_id** | **str**| Deployment Rule ID |
 **application_deployment_rule_edit_request** | [**ApplicationDeploymentRuleEditRequest**](ApplicationDeploymentRuleEditRequest.md)|  | [optional]

### Return type

[**ApplicationDeploymentRuleResponse**](ApplicationDeploymentRuleResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Edit application deployment rule |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_deployment_rule**
> ApplicationDeploymentRuleResponse get_application_deployment_rule(application_id)

Get application deployment rule

Get application deployment rule

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import application_deployment_rule_api
from qovery.model.application_deployment_rule_response import ApplicationDeploymentRuleResponse
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
    api_instance = application_deployment_rule_api.ApplicationDeploymentRuleApi(api_client)
    application_id = "applicationId_example" # str | Application ID

    # example passing only required values which don't have defaults set
    try:
        # Get application deployment rule
        api_response = api_instance.get_application_deployment_rule(application_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ApplicationDeploymentRuleApi->get_application_deployment_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_id** | **str**| Application ID |

### Return type

[**ApplicationDeploymentRuleResponse**](ApplicationDeploymentRuleResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get application deployment rule |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

