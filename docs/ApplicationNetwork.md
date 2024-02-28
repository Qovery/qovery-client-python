# ApplicationNetwork


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sticky_session** | **bool** | Specify if the sticky session option (also called persistant session) is activated or not for this application. If activated, user will be redirected by the load balancer to the same instance each time he access to the application.   | [optional] [default to False]

## Example

```python
from qovery.models.application_network import ApplicationNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationNetwork from a JSON string
application_network_instance = ApplicationNetwork.from_json(json)
# print the JSON string representation of the object
print ApplicationNetwork.to_json()

# convert the object into a dict
application_network_dict = application_network_instance.to_dict()
# create an instance of ApplicationNetwork from a dict
application_network_form_dict = application_network.from_dict(application_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


