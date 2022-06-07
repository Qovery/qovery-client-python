# qovery.ReferralRewardsApi

All URIs are relative to *https://api.qovery.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_referral**](ReferralRewardsApi.md#get_account_referral) | **GET** /account/referral | Get your referral information
[**post_account_reward_claim**](ReferralRewardsApi.md#post_account_reward_claim) | **POST** /account/rewardClaim | Claim a reward


# **get_account_referral**
> Referral get_account_referral()

Get your referral information

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import referral_rewards_api
from qovery.model.referral import Referral
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
    api_instance = referral_rewards_api.ReferralRewardsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get your referral information
        api_response = api_instance.get_account_referral()
        pprint(api_response)
    except qovery.ApiException as e:
        print("Exception when calling ReferralRewardsApi->get_account_referral: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**Referral**](Referral.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get referral info |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_account_reward_claim**
> post_account_reward_claim()

Claim a reward

A same code can be claimed only 3 times at max

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import time
import qovery
from qovery.api import referral_rewards_api
from qovery.model.reward_claim import RewardClaim
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
    api_instance = referral_rewards_api.ReferralRewardsApi(api_client)
    reward_claim = RewardClaim(
        type="INVITATION",
        code="xDowkWEl",
    ) # RewardClaim |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Claim a reward
        api_instance.post_account_reward_claim(reward_claim=reward_claim)
    except qovery.ApiException as e:
        print("Exception when calling ReferralRewardsApi->post_account_reward_claim: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reward_claim** | [**RewardClaim**](RewardClaim.md)|  | [optional]

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
**200** | Claim reward |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

