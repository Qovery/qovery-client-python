# ServicePort


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | [optional] 
**internal_port** | **int** | The listening port of your service. | 
**external_port** | **int** | The exposed port for your service. This is optional. If not set a default port will be used. | [optional] 
**publicly_accessible** | **bool** | Expose the port to the world | 
**is_default** | **bool** | is the default port to use for domain | [optional] 
**protocol** | [**PortProtocolEnum**](PortProtocolEnum.md) |  | 

## Example

```python
from qovery.models.service_port import ServicePort

# TODO update the JSON string below
json = "{}"
# create an instance of ServicePort from a JSON string
service_port_instance = ServicePort.from_json(json)
# print the JSON string representation of the object
print ServicePort.to_json()

# convert the object into a dict
service_port_dict = service_port_instance.to_dict()
# create an instance of ServicePort from a dict
service_port_form_dict = service_port.from_dict(service_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


