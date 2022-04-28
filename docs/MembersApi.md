# qovery.MembersApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_invite_member**](MembersApi.md#delete_invite_member) | **DELETE** /organization/{organizationId}/inviteMember/{inviteId} | Remove an invited member
[**delete_member**](MembersApi.md#delete_member) | **DELETE** /organization/{organizationId}/member/{userId} | Remove a member
[**get_organization_invited_members**](MembersApi.md#get_organization_invited_members) | **GET** /organization/{organizationId}/inviteMember | Get invited members
[**get_organization_members**](MembersApi.md#get_organization_members) | **GET** /organization/{organizationId}/member | Get organization members
[**post_accept_invite_member**](MembersApi.md#post_accept_invite_member) | **POST** /organization/{organizationId}/inviteMember/{inviteId} | Accept Invite in the organization
[**post_invite_member**](MembersApi.md#post_invite_member) | **POST** /organization/{organizationId}/inviteMember | Invite someone in the organization
[**post_organization_transfer_ownership**](MembersApi.md#post_organization_transfer_ownership) | **POST** /organization/{organizationId}/transferOwnership | Transfer organization ownership to another user


# **delete_invite_member**
> delete_invite_member(organization_id)

Remove an invited member

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import members_api
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
    api_instance = members_api.MembersApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID

    # example passing only required values which don't have defaults set
    try:
        # Remove an invited member
        api_instance.delete_invite_member(organization_id)
    except qovery.ApiException as e:
        print("Exception when calling MembersApi->delete_invite_member: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

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

# **delete_member**
> delete_member(organization_id, user_id)

Remove a member

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import members_api
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
    api_instance = members_api.MembersApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    user_id = "userId_example" # str | User ID

    # example passing only required values which don't have defaults set
    try:
        # Remove a member
        api_instance.delete_member(organization_id, user_id)
    except qovery.ApiException as e:
        print("Exception when calling MembersApi->delete_member: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **user_id** | **str**| User ID |

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

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

# **get_organization_invited_members**
> InviteMemberResponseList get_organization_invited_members(organization_id)

Get invited members

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import members_api
from qovery.model.invite_member_response_list import InviteMemberResponseList
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
    api_instance = members_api.MembersApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID

    # example passing only required values which don't have defaults set
    try:
        # Get invited members
        api_response = api_instance.get_organization_invited_members(organization_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling MembersApi->get_organization_invited_members: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |

### Return type

[**InviteMemberResponseList**](InviteMemberResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get invited members |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_members**
> MemberResponseList get_organization_members(organization_id)

Get organization members

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import members_api
from qovery.model.member_response_list import MemberResponseList
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
    api_instance = members_api.MembersApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID

    # example passing only required values which don't have defaults set
    try:
        # Get organization members
        api_response = api_instance.get_organization_members(organization_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling MembersApi->get_organization_members: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |

### Return type

[**MemberResponseList**](MemberResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get members |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_accept_invite_member**
> InviteMember post_accept_invite_member(organization_id, invite_id)

Accept Invite in the organization

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import members_api
from qovery.model.invite_member import InviteMember
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
    api_instance = members_api.MembersApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    invite_id = "inviteId_example" # str | Invite ID

    # example passing only required values which don't have defaults set
    try:
        # Accept Invite in the organization
        api_response = api_instance.post_accept_invite_member(organization_id, invite_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling MembersApi->post_accept_invite_member: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **invite_id** | **str**| Invite ID |

### Return type

[**InviteMember**](InviteMember.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | User invited |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | User already invited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_invite_member**
> InviteMember post_invite_member(organization_id)

Invite someone in the organization

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import members_api
from qovery.model.invite_member_request import InviteMemberRequest
from qovery.model.invite_member import InviteMember
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
    api_instance = members_api.MembersApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    invite_member_request = InviteMemberRequest(
        email="email_example",
        role=InviteMemberRoleEnum("ADMIN"),
    ) # InviteMemberRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Invite someone in the organization
        api_response = api_instance.post_invite_member(organization_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling MembersApi->post_invite_member: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Invite someone in the organization
        api_response = api_instance.post_invite_member(organization_id, invite_member_request=invite_member_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling MembersApi->post_invite_member: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **invite_member_request** | [**InviteMemberRequest**](InviteMemberRequest.md)|  | [optional]

### Return type

[**InviteMember**](InviteMember.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | User invited |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |
**409** | User already invited |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_organization_transfer_ownership**
> post_organization_transfer_ownership(organization_id)

Transfer organization ownership to another user

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import members_api
from qovery.model.transfer_ownership_request import TransferOwnershipRequest
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
    api_instance = members_api.MembersApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    transfer_ownership_request = TransferOwnershipRequest(
        user_id="user_id_example",
    ) # TransferOwnershipRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Transfer organization ownership to another user
        api_instance.post_organization_transfer_ownership(organization_id)
    except qovery.ApiException as e:
        print("Exception when calling MembersApi->post_organization_transfer_ownership: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Transfer organization ownership to another user
        api_instance.post_organization_transfer_ownership(organization_id, transfer_ownership_request=transfer_ownership_request)
    except qovery.ApiException as e:
        print("Exception when calling MembersApi->post_organization_transfer_ownership: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **transfer_ownership_request** | [**TransferOwnershipRequest**](TransferOwnershipRequest.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | no content |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

