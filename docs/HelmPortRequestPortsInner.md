# HelmPortRequestPortsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**internal_port** | **int** | The listening port of your service. | 
**external_port** | **int** | The exposed port for your service. This is optional. If not set a default port will be used. | [optional] 
**service_name** | **str** |  | 
**namespace** | **str** |  | [optional] 
**protocol** | [**HelmPortProtocolEnum**](HelmPortProtocolEnum.md) |  | [optional] 
**is_default** | **bool** | is the default port to use for domain | [optional] 

## Example

```python
from qovery.models.helm_port_request_ports_inner import HelmPortRequestPortsInner

# TODO update the JSON string below
json = "{}"
# create an instance of HelmPortRequestPortsInner from a JSON string
helm_port_request_ports_inner_instance = HelmPortRequestPortsInner.from_json(json)
# print the JSON string representation of the object
print HelmPortRequestPortsInner.to_json()

# convert the object into a dict
helm_port_request_ports_inner_dict = helm_port_request_ports_inner_instance.to_dict()
# create an instance of HelmPortRequestPortsInner from a dict
helm_port_request_ports_inner_form_dict = helm_port_request_ports_inner.from_dict(helm_port_request_ports_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


