# qovery.ProjectDeploymentRuleApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_deployment_rule**](ProjectDeploymentRuleApi.md#create_deployment_rule) | **POST** /project/{projectId}/deploymentRule | Create a deployment rule
[**delete_project_deployment_rule**](ProjectDeploymentRuleApi.md#delete_project_deployment_rule) | **DELETE** /project/{projectId}/deploymentRule/{deploymentRuleId} | Delete a project deployment rule
[**edit_project_deployemtn_rule**](ProjectDeploymentRuleApi.md#edit_project_deployemtn_rule) | **PUT** /project/{projectId}/deploymentRule/{deploymentRuleId} | Edit a project deployment rule
[**get_project_deployment_rule**](ProjectDeploymentRuleApi.md#get_project_deployment_rule) | **GET** /project/{projectId}/deploymentRule/{deploymentRuleId} | Get a project deployment rule
[**list_project_deployment_rules**](ProjectDeploymentRuleApi.md#list_project_deployment_rules) | **GET** /project/{projectId}/deploymentRule | List project deployment rules
[**update_deployment_rules_priority_order**](ProjectDeploymentRuleApi.md#update_deployment_rules_priority_order) | **PUT** /project/{projectId}/deploymentRule/order | Update deployment rules priority order


# **create_deployment_rule**
> ProjectDeploymentRule create_deployment_rule(project_id)

Create a deployment rule

Create a deployment rule

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import project_deployment_rule_api
from qovery.model.project_deployment_rule_request import ProjectDeploymentRuleRequest
from qovery.model.project_deployment_rule import ProjectDeploymentRule
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
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = qovery.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with qovery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_deployment_rule_api.ProjectDeploymentRuleApi(api_client)
    project_id = "projectId_example" # str | Project ID
    project_deployment_rule_request = ProjectDeploymentRuleRequest(
        name="project-rule",
        description="description project rule",
        mode=EnvironmentModeEnum("PRODUCTION"),
        cluster_id="cluster_id_example",
        auto_deploy=False,
        auto_stop=False,
        timezone="UTC",
        start_time=dateutil_parser('1970-01-01T08:00:00Z'),
        stop_time=dateutil_parser('1970-01-01T19:00:00Z'),
        weekdays=[
            WeekdayEnum("MONDAY"),
        ],
        wildcard="",
    ) # ProjectDeploymentRuleRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a deployment rule
        api_response = api_instance.create_deployment_rule(project_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ProjectDeploymentRuleApi->create_deployment_rule: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a deployment rule
        api_response = api_instance.create_deployment_rule(project_id, project_deployment_rule_request=project_deployment_rule_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ProjectDeploymentRuleApi->create_deployment_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID |
 **project_deployment_rule_request** | [**ProjectDeploymentRuleRequest**](ProjectDeploymentRuleRequest.md)|  | [optional]

### Return type

[**ProjectDeploymentRule**](ProjectDeploymentRule.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Create deployment rule |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_deployment_rule**
> delete_project_deployment_rule(project_id, deployment_rule_id)

Delete a project deployment rule

Delete a project deployment rule

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import project_deployment_rule_api
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
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = qovery.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with qovery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_deployment_rule_api.ProjectDeploymentRuleApi(api_client)
    project_id = "projectId_example" # str | Project ID
    deployment_rule_id = "deploymentRuleId_example" # str | Deployment Rule ID

    # example passing only required values which don't have defaults set
    try:
        # Delete a project deployment rule
        api_instance.delete_project_deployment_rule(project_id, deployment_rule_id)
    except qovery.ApiException as e:
        print("Exception when calling ProjectDeploymentRuleApi->delete_project_deployment_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID |
 **deployment_rule_id** | **str**| Deployment Rule ID |

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

# **edit_project_deployemtn_rule**
> ProjectDeploymentRule edit_project_deployemtn_rule(project_id, deployment_rule_id)

Edit a project deployment rule

Edit a project deployment rule

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import project_deployment_rule_api
from qovery.model.project_deployment_rule_request import ProjectDeploymentRuleRequest
from qovery.model.project_deployment_rule import ProjectDeploymentRule
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
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = qovery.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with qovery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_deployment_rule_api.ProjectDeploymentRuleApi(api_client)
    project_id = "projectId_example" # str | Project ID
    deployment_rule_id = "deploymentRuleId_example" # str | Deployment Rule ID
    project_deployment_rule_request = ProjectDeploymentRuleRequest(
        name="project-rule",
        description="description project rule",
        mode=EnvironmentModeEnum("PRODUCTION"),
        cluster_id="cluster_id_example",
        auto_deploy=False,
        auto_stop=False,
        timezone="UTC",
        start_time=dateutil_parser('1970-01-01T08:00:00Z'),
        stop_time=dateutil_parser('1970-01-01T19:00:00Z'),
        weekdays=[
            WeekdayEnum("MONDAY"),
        ],
        wildcard="",
    ) # ProjectDeploymentRuleRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Edit a project deployment rule
        api_response = api_instance.edit_project_deployemtn_rule(project_id, deployment_rule_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ProjectDeploymentRuleApi->edit_project_deployemtn_rule: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit a project deployment rule
        api_response = api_instance.edit_project_deployemtn_rule(project_id, deployment_rule_id, project_deployment_rule_request=project_deployment_rule_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ProjectDeploymentRuleApi->edit_project_deployemtn_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID |
 **deployment_rule_id** | **str**| Deployment Rule ID |
 **project_deployment_rule_request** | [**ProjectDeploymentRuleRequest**](ProjectDeploymentRuleRequest.md)|  | [optional]

### Return type

[**ProjectDeploymentRule**](ProjectDeploymentRule.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Edit a project deployment rule |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_deployment_rule**
> ProjectDeploymentRule get_project_deployment_rule(project_id, deployment_rule_id)

Get a project deployment rule

Get a project deployment rule

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import project_deployment_rule_api
from qovery.model.project_deployment_rule import ProjectDeploymentRule
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
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = qovery.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with qovery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_deployment_rule_api.ProjectDeploymentRuleApi(api_client)
    project_id = "projectId_example" # str | Project ID
    deployment_rule_id = "deploymentRuleId_example" # str | Deployment Rule ID

    # example passing only required values which don't have defaults set
    try:
        # Get a project deployment rule
        api_response = api_instance.get_project_deployment_rule(project_id, deployment_rule_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ProjectDeploymentRuleApi->get_project_deployment_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID |
 **deployment_rule_id** | **str**| Deployment Rule ID |

### Return type

[**ProjectDeploymentRule**](ProjectDeploymentRule.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get project deployment rule |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_project_deployment_rules**
> ProjectDeploymentRuleResponseList list_project_deployment_rules(project_id)

List project deployment rules

List project deployment rules

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import project_deployment_rule_api
from qovery.model.project_deployment_rule_response_list import ProjectDeploymentRuleResponseList
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
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = qovery.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with qovery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_deployment_rule_api.ProjectDeploymentRuleApi(api_client)
    project_id = "projectId_example" # str | Project ID

    # example passing only required values which don't have defaults set
    try:
        # List project deployment rules
        api_response = api_instance.list_project_deployment_rules(project_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ProjectDeploymentRuleApi->list_project_deployment_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID |

### Return type

[**ProjectDeploymentRuleResponseList**](ProjectDeploymentRuleResponseList.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get project deployment rules |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_deployment_rules_priority_order**
> update_deployment_rules_priority_order(project_id)

Update deployment rules priority order

Update deployment rules priority order

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import project_deployment_rule_api
from qovery.model.project_deployment_rules_priority_order_request import ProjectDeploymentRulesPriorityOrderRequest
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
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): bearerAuth
configuration = qovery.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with qovery.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = project_deployment_rule_api.ProjectDeploymentRuleApi(api_client)
    project_id = "projectId_example" # str | Project ID
    project_deployment_rules_priority_order_request = ProjectDeploymentRulesPriorityOrderRequest(
        project_deployment_rule_ids_in_order=[
            "project_deployment_rule_ids_in_order_example",
        ],
    ) # ProjectDeploymentRulesPriorityOrderRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update deployment rules priority order
        api_instance.update_deployment_rules_priority_order(project_id)
    except qovery.ApiException as e:
        print("Exception when calling ProjectDeploymentRuleApi->update_deployment_rules_priority_order: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update deployment rules priority order
        api_instance.update_deployment_rules_priority_order(project_id, project_deployment_rules_priority_order_request=project_deployment_rules_priority_order_request)
    except qovery.ApiException as e:
        print("Exception when calling ProjectDeploymentRuleApi->update_deployment_rules_priority_order: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID |
 **project_deployment_rules_priority_order_request** | [**ProjectDeploymentRulesPriorityOrderRequest**](ProjectDeploymentRulesPriorityOrderRequest.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update deployment rules priority order |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

