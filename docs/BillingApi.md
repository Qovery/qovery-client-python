# qovery.BillingApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_credit_card**](BillingApi.md#add_credit_card) | **POST** /organization/{organizationId}/creditCard | Add credit card
[**add_credit_code**](BillingApi.md#add_credit_code) | **POST** /organization/{organizationId}/creditCode | Add credit code
[**edit_organization_billing_info**](BillingApi.md#edit_organization_billing_info) | **PUT** /organization/{organizationId}/billingInfo | Edit Organization Billing Info
[**get_cluster_current_cost**](BillingApi.md#get_cluster_current_cost) | **GET** /organization/{organizationId}/cluster/{clusterId}/currentCost | Get cluster current cost
[**get_organization_billing_info**](BillingApi.md#get_organization_billing_info) | **GET** /organization/{organizationId}/billingInfo | Get organization billing info
[**get_organization_billing_status**](BillingApi.md#get_organization_billing_status) | **GET** /organization/{organizationId}/billingStatus | Get organization billing status
[**get_organization_current_cost**](BillingApi.md#get_organization_current_cost) | **GET** /organization/{organizationId}/currentCost | Get organization current cost
[**get_organization_invoice**](BillingApi.md#get_organization_invoice) | **GET** /organization/{organizationId}/invoice/{invoiceId} | Get organization invoice
[**get_organization_invoice_pdf**](BillingApi.md#get_organization_invoice_pdf) | **GET** /organization/{organizationId}/invoice/{invoiceId}/download | Get invoice link
[**list_organization_credit_cards**](BillingApi.md#list_organization_credit_cards) | **GET** /organization/{organizationId}/creditCard | List organization credit cards
[**list_organization_invoice**](BillingApi.md#list_organization_invoice) | **GET** /organization/{organizationId}/invoice | List organization invoices
[**organization_download_all_invoices**](BillingApi.md#organization_download_all_invoices) | **POST** /organization/{organizationId}/downloadInvoices | Download all invoices
[**organization_organization_id_credit_card_credit_card_id_delete**](BillingApi.md#organization_organization_id_credit_card_credit_card_id_delete) | **DELETE** /organization/{organizationId}/creditCard/{creditCardId} | Delete credit card


# **add_credit_card**
> CreditCardResponse add_credit_card(organization_id)

Add credit card

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import billing_api
from qovery.model.credit_card_response import CreditCardResponse
from qovery.model.credit_card_request import CreditCardRequest
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
    api_instance = billing_api.BillingApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    credit_card_request = CreditCardRequest(
        number="number_example",
        cvv="cvv_example",
        expiry_month=6,
        expiry_year=2025,
    ) # CreditCardRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add credit card
        api_response = api_instance.add_credit_card(organization_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling BillingApi->add_credit_card: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add credit card
        api_response = api_instance.add_credit_card(organization_id, credit_card_request=credit_card_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling BillingApi->add_credit_card: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **credit_card_request** | [**CreditCardRequest**](CreditCardRequest.md)|  | [optional]

### Return type

[**CreditCardResponse**](CreditCardResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Add credit card |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_credit_code**
> add_credit_code(organization_id)

Add credit code

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import billing_api
from qovery.model.organization_credit_code_request import OrganizationCreditCodeRequest
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
    api_instance = billing_api.BillingApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    organization_credit_code_request = OrganizationCreditCodeRequest(
        code="code_example",
    ) # OrganizationCreditCodeRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add credit code
        api_instance.add_credit_code(organization_id)
    except qovery.ApiException as e:
        print("Exception when calling BillingApi->add_credit_code: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add credit code
        api_instance.add_credit_code(organization_id, organization_credit_code_request=organization_credit_code_request)
    except qovery.ApiException as e:
        print("Exception when calling BillingApi->add_credit_code: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **organization_credit_code_request** | [**OrganizationCreditCodeRequest**](OrganizationCreditCodeRequest.md)|  | [optional]

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
**200** | add credit code |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_organization_billing_info**
> BillingInfoResponse edit_organization_billing_info(organization_id)

Edit Organization Billing Info

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import billing_api
from qovery.model.billing_info_request import BillingInfoRequest
from qovery.model.billing_info_response import BillingInfoResponse
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
    api_instance = billing_api.BillingApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    billing_info_request = BillingInfoRequest(
        first_name="Forrest",
        last_name="Gump",
        email="forrest@gump.com",
        address="21 Jenny Street",
        city="Greenbow",
        zip="36744",
        state="Alabama",
        country_code="US",
        company="company_example",
        vat_number="vat_number_example",
    ) # BillingInfoRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Edit Organization Billing Info
        api_response = api_instance.edit_organization_billing_info(organization_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling BillingApi->edit_organization_billing_info: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Edit Organization Billing Info
        api_response = api_instance.edit_organization_billing_info(organization_id, billing_info_request=billing_info_request)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling BillingApi->edit_organization_billing_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **billing_info_request** | [**BillingInfoRequest**](BillingInfoRequest.md)|  | [optional]

### Return type

[**BillingInfoResponse**](BillingInfoResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Edit billing info |  -  |
**400** | Bad request |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_current_cost**
> CostRangeResponse get_cluster_current_cost(organization_id, cluster_id)

Get cluster current cost

Get your cluster cost range. We are unable to give a precise cost of your infrastructure at the moment. But Qovery guarantees that the cost of your cluster will not exceed the max range. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import billing_api
from qovery.model.cost_range_response import CostRangeResponse
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
    api_instance = billing_api.BillingApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    cluster_id = "clusterId_example" # str | Cluster ID

    # example passing only required values which don't have defaults set
    try:
        # Get cluster current cost
        api_response = api_instance.get_cluster_current_cost(organization_id, cluster_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling BillingApi->get_cluster_current_cost: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **cluster_id** | **str**| Cluster ID |

### Return type

[**CostRangeResponse**](CostRangeResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get cluster cost |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_billing_info**
> BillingInfoResponse get_organization_billing_info(organization_id)

Get organization billing info

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import billing_api
from qovery.model.billing_info_response import BillingInfoResponse
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
    api_instance = billing_api.BillingApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID

    # example passing only required values which don't have defaults set
    try:
        # Get organization billing info
        api_response = api_instance.get_organization_billing_info(organization_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling BillingApi->get_organization_billing_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |

### Return type

[**BillingInfoResponse**](BillingInfoResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Billing Info |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_billing_status**
> BillingStatus get_organization_billing_status(organization_id)

Get organization billing status

This endpoint returns a \"is_valid\" boolean field reflecting the billing status of the organization: - If true, the organization billing is valid - For Startup organization, it returns false if there is at least 1 invoice unpaid since 1 week - For Community organization, it returns false if there is no credit left 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import billing_api
from qovery.model.billing_status import BillingStatus
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
    api_instance = billing_api.BillingApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID

    # example passing only required values which don't have defaults set
    try:
        # Get organization billing status
        api_response = api_instance.get_organization_billing_status(organization_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling BillingApi->get_organization_billing_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |

### Return type

[**BillingStatus**](BillingStatus.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Billing Status |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_current_cost**
> OrganizationCurrentCostResponse get_organization_current_cost(organization_id)

Get organization current cost

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import billing_api
from qovery.model.organization_current_cost_response import OrganizationCurrentCostResponse
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
    api_instance = billing_api.BillingApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID

    # example passing only required values which don't have defaults set
    try:
        # Get organization current cost
        api_response = api_instance.get_organization_current_cost(organization_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling BillingApi->get_organization_current_cost: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |

### Return type

[**OrganizationCurrentCostResponse**](OrganizationCurrentCostResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Cost |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_invoice**
> InvoiceResponse get_organization_invoice(organization_id, invoice_id)

Get organization invoice

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import billing_api
from qovery.model.invoice_response import InvoiceResponse
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
    api_instance = billing_api.BillingApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    invoice_id = "invoiceId_example" # str | Invoice ID

    # example passing only required values which don't have defaults set
    try:
        # Get organization invoice
        api_response = api_instance.get_organization_invoice(organization_id, invoice_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling BillingApi->get_organization_invoice: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **invoice_id** | **str**| Invoice ID |

### Return type

[**InvoiceResponse**](InvoiceResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Invoice |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_invoice_pdf**
> LinkResponse get_organization_invoice_pdf(organization_id, invoice_id)

Get invoice link

This will return URL of the invoice PDF

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import billing_api
from qovery.model.link_response import LinkResponse
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
    api_instance = billing_api.BillingApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    invoice_id = "invoiceId_example" # str | Invoice ID

    # example passing only required values which don't have defaults set
    try:
        # Get invoice link
        api_response = api_instance.get_organization_invoice_pdf(organization_id, invoice_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling BillingApi->get_organization_invoice_pdf: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **invoice_id** | **str**| Invoice ID |

### Return type

[**LinkResponse**](LinkResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get invoice PDF |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_organization_credit_cards**
> CreditCardResponseList list_organization_credit_cards(organization_id)

List organization credit cards

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import billing_api
from qovery.model.credit_card_response_list import CreditCardResponseList
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
    api_instance = billing_api.BillingApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID

    # example passing only required values which don't have defaults set
    try:
        # List organization credit cards
        api_response = api_instance.list_organization_credit_cards(organization_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling BillingApi->list_organization_credit_cards: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |

### Return type

[**CreditCardResponseList**](CreditCardResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List cfredit cards |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_organization_invoice**
> InvoiceResponseList list_organization_invoice(organization_id)

List organization invoices

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import billing_api
from qovery.model.invoice_response_list import InvoiceResponseList
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
    api_instance = billing_api.BillingApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID

    # example passing only required values which don't have defaults set
    try:
        # List organization invoices
        api_response = api_instance.list_organization_invoice(organization_id)
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling BillingApi->list_organization_invoice: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |

### Return type

[**InvoiceResponseList**](InvoiceResponseList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List Invoices |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_download_all_invoices**
> organization_download_all_invoices(organization_id)

Download all invoices

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import billing_api
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
    api_instance = billing_api.BillingApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID

    # example passing only required values which don't have defaults set
    try:
        # Download all invoices
        api_instance.organization_download_all_invoices(organization_id)
    except qovery.ApiException as e:
        print("Exception when calling BillingApi->organization_download_all_invoices: %s\n" % e)
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
**202** | You will receive an email containing your invoices |  -  |
**401** | Access token is missing or invalid |  -  |
**403** | Access forbidden |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **organization_organization_id_credit_card_credit_card_id_delete**
> organization_organization_id_credit_card_credit_card_id_delete(organization_id, credit_card_id)

Delete credit card

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import billing_api
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
    api_instance = billing_api.BillingApi(api_client)
    organization_id = "organizationId_example" # str | Organization ID
    credit_card_id = "creditCardId_example" # str | Credit Card ID

    # example passing only required values which don't have defaults set
    try:
        # Delete credit card
        api_instance.organization_organization_id_credit_card_credit_card_id_delete(organization_id, credit_card_id)
    except qovery.ApiException as e:
        print("Exception when calling BillingApi->organization_organization_id_credit_card_credit_card_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**| Organization ID |
 **credit_card_id** | **str**| Credit Card ID |

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

