# ApplicationNetworkRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sticky_session** | **bool** | Specify if the sticky session option (also called persistant session) is activated or not for this application. If activated, user will be redirected by the load balancer to the same instance each time he access to the application.   | [optional] [default to False]

## Example

```python
from qovery.models.application_network_request import ApplicationNetworkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationNetworkRequest from a JSON string
application_network_request_instance = ApplicationNetworkRequest.from_json(json)
# print the JSON string representation of the object
print ApplicationNetworkRequest.to_json()

# convert the object into a dict
application_network_request_dict = application_network_request_instance.to_dict()
# create an instance of ApplicationNetworkRequest from a dict
application_network_request_form_dict = application_network_request.from_dict(application_network_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


