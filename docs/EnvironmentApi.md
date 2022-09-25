# qovery.EnvironmentApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deploy_all_applications**](EnvironmentApi.md#deploy_all_applications) | **POST** /environment/{environmentId}/application/deploy | Deploy applications


# **deploy_all_applications**
> Status deploy_all_applications(environment_id)

Deploy applications

Start a deployment of the environment. Any of the services within the chosen environment based on the following rule: a service is deployed only if a new version is specified in the payload for that application/container or if there was a change in its configuration that needs to be applied (vCPU,RAM etc..)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import environment_api
from qovery.model.deploy_all_request import DeployAllRequest
from qovery.model.status import Status
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
    api_instance = environment_api.EnvironmentApi(api_client)
    environment_id = "environmentId_example" # str | Environment ID
    deploy_all_request = DeployAllRequest(
        applications=[
            DeployAllRequestApplicationsInner(
                application_id="application_id_example",
                git_commit_id="git_commit_id_example",
            ),
        ],
        containers=[
            DeployAllRequestContainersInner(
                id="id_example",
                image_tag="image_tag_example",
            ),
        ],
    ) # DeployAllRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Deploy applications
        api_response = api_instance.deploy_all_applications(environment_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling EnvironmentApi->deploy_all_applications: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Deploy applications
        api_response = api_instance.deploy_all_applications(environment_id, deploy_all_request=deploy_all_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling EnvironmentApi->deploy_all_applications: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **environment_id** | **str**| Environment ID |
 **deploy_all_request** | [**DeployAllRequest**](DeployAllRequest.md)|  | [optional]

### Return type

[**Status**](Status.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Deployed applications |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | Operation is in progress |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

