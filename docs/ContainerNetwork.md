# ContainerNetwork


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sticky_session** | **bool** | Specify if the sticky session option (also called persistant session) is activated or not for this container. If activated, user will be redirected by the load balancer to the same instance each time he access to the container.   | [optional] [default to False]

## Example

```python
from qovery.models.container_network import ContainerNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of ContainerNetwork from a JSON string
container_network_instance = ContainerNetwork.from_json(json)
# print the JSON string representation of the object
print ContainerNetwork.to_json()

# convert the object into a dict
container_network_dict = container_network_instance.to_dict()
# create an instance of ContainerNetwork from a dict
container_network_form_dict = container_network.from_dict(container_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


