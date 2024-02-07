# HelmAdvancedSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_custom_domain_check_enabled** | **bool** | disable custom domain check when deploying a helm | [optional] 
**network_ingress_proxy_body_size_mb** | **int** |  | [optional] 
**network_ingress_enable_cors** | **bool** |  | [optional] 
**network_ingress_cors_allow_origin** | **str** |  | [optional] 
**network_ingress_cors_allow_methods** | **str** |  | [optional] 
**network_ingress_cors_allow_headers** | **str** |  | [optional] 
**network_ingress_proxy_buffer_size_kb** | **int** | header buffer size used while reading response header from upstream | [optional] 
**network_ingress_keepalive_time_seconds** | **int** | Limits the maximum time (in seconds) during which requests can be processed through one keepalive connection | [optional] 
**network_ingress_keepalive_timeout_seconds** | **int** | Sets a timeout (in seconds) during which an idle keepalive connection to an upstream server will stay open. | [optional] 
**network_ingress_send_timeout_seconds** | **int** | Sets a timeout (in seconds) for transmitting a response to the client | [optional] 
**network_ingress_proxy_connect_timeout_seconds** | **int** | Sets a timeout (in seconds) for establishing a connection to a proxied server | [optional] 
**network_ingress_proxy_send_timeout_seconds** | **int** | Sets a timeout (in seconds) for transmitting a request to the proxied server | [optional] 
**network_ingress_proxy_read_timeout_seconds** | **int** | Sets a timeout (in seconds) for reading a response from the proxied server | [optional] 
**network_ingress_proxy_buffering** | **str** | Allows to enable or disable nginx &#x60;proxy-buffering&#x60; | [optional] 
**network_ingress_proxy_request_buffering** | **str** | Allows to enable or disable nginx &#x60;proxy-request-buffering&#x60; | [optional] 
**network_ingress_grpc_send_timeout_seconds** | **int** | Sets a timeout (in seconds) for transmitting a request to the grpc server | [optional] 
**network_ingress_grpc_read_timeout_seconds** | **int** | Sets a timeout (in seconds) for transmitting a request to the grpc server | [optional] 
**network_ingress_whitelist_source_range** | **str** | list of source ranges to allow access to ingress proxy.  This property can be used to whitelist source IP ranges for ingress proxy. The value is a comma separated list of CIDRs, e.g. 10.0.0.0/24,172.10.0.1 To allow all source ranges, set 0.0.0.0/0.  | [optional] 
**network_ingress_denylist_source_range** | **str** | list of source ranges to deny access to ingress proxy.  This property can be used to blacklist source IP ranges for ingress proxy. The value is a comma separated list of CIDRs, e.g. 10.0.0.0/24,172.10.0.1  | [optional] 
**network_ingress_extra_headers** | **str** | Allows to define response headers | [optional] 
**network_ingress_basic_auth_env_var** | **str** | Set the name of an environment variable to use as a basic authentication (&#x60;login:crypted_password&#x60;) from &#x60;htpasswd&#x60; command. You can add multiples comma separated values.  | [optional] 
**network_ingress_enable_sticky_session** | **bool** | Enable the load balancer to bind a user&#39;s session to a specific target. This ensures that all requests from the user during the session are sent to the same target  | [optional] 

## Example

```python
from qovery.models.helm_advanced_settings import HelmAdvancedSettings

# TODO update the JSON string below
json = "{}"
# create an instance of HelmAdvancedSettings from a JSON string
helm_advanced_settings_instance = HelmAdvancedSettings.from_json(json)
# print the JSON string representation of the object
print HelmAdvancedSettings.to_json()

# convert the object into a dict
helm_advanced_settings_dict = helm_advanced_settings_instance.to_dict()
# create an instance of HelmAdvancedSettings from a dict
helm_advanced_settings_form_dict = helm_advanced_settings.from_dict(helm_advanced_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


