# ContainerNetworkRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sticky_session** | **bool** | Specify if the sticky session option (also called persistant session) is activated or not for this container. If activated, user will be redirected by the load balancer to the same instance each time he access to the container.   | [optional] [default to False]

## Example

```python
from qovery.models.container_network_request import ContainerNetworkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ContainerNetworkRequest from a JSON string
container_network_request_instance = ContainerNetworkRequest.from_json(json)
# print the JSON string representation of the object
print ContainerNetworkRequest.to_json()

# convert the object into a dict
container_network_request_dict = container_network_request_instance.to_dict()
# create an instance of ContainerNetworkRequest from a dict
container_network_request_form_dict = container_network_request.from_dict(container_network_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


