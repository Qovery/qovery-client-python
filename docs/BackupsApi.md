# qovery.BackupsApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_backup_database**](BackupsApi.md#add_backup_database) | **POST** /database/{databaseId}/backup | Add a backup to the Database 
[**list_database_backup**](BackupsApi.md#list_database_backup) | **GET** /database/{databaseId}/backup | List database  backups
[**remove_database_backup**](BackupsApi.md#remove_database_backup) | **DELETE** /database/{databaseId}/backup/{backupId} | Remove database  backup


# **add_backup_database**
> BackupResponse add_backup_database(database_id)

Add a backup to the Database 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import backups_api
from qovery.model.backup_request import BackupRequest
from qovery.model.backup_response import BackupResponse
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
    api_instance = backups_api.BackupsApi(api_client)
    database_id = "databaseId_example" # str | Database ID
    backup_request = BackupRequest(
        name="name_example",
        message="message_example",
    ) # BackupRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add a backup to the Database 
        api_response = api_instance.add_backup_database(database_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling BackupsApi->add_backup_database: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add a backup to the Database 
        api_response = api_instance.add_backup_database(database_id, backup_request=backup_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling BackupsApi->add_backup_database: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_id** | **str**| Database ID |
 **backup_request** | [**BackupRequest**](BackupRequest.md)|  | [optional]

### Return type

[**BackupResponse**](BackupResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Added backup |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_database_backup**
> BackupPaginatedResponseList list_database_backup(database_id)

List database  backups

By default it returns the 20 last results. The response is paginated. In order to request the next page, you can use the startId query parameter

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import backups_api
from qovery.model.backup_paginated_response_list import BackupPaginatedResponseList
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
    api_instance = backups_api.BackupsApi(api_client)
    database_id = "databaseId_example" # str | Database ID
    start_id = "startId_example" # str | Starting point after which to return results (optional)

    # example passing only required values which don't have defaults set
    try:
        # List database  backups
        api_response = api_instance.list_database_backup(database_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling BackupsApi->list_database_backup: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List database  backups
        api_response = api_instance.list_database_backup(database_id, start_id=start_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling BackupsApi->list_database_backup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_id** | **str**| Database ID |
 **start_id** | **str**| Starting point after which to return results | [optional]

### Return type

[**BackupPaginatedResponseList**](BackupPaginatedResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List backups |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_database_backup**
> remove_database_backup(database_id, backup_id)

Remove database  backup

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import backups_api
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
    api_instance = backups_api.BackupsApi(api_client)
    database_id = "databaseId_example" # str | Database ID
    backup_id = "backupId_example" # str | Database Backup ID

    # example passing only required values which don't have defaults set
    try:
        # Remove database  backup
        api_instance.remove_database_backup(database_id, backup_id)
    except qovery.ApiException as e:
        print("Exception when calling BackupsApi->remove_database_backup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **database_id** | **str**| Database ID |
 **backup_id** | **str**| Database Backup ID |

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
**204** | no content |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

