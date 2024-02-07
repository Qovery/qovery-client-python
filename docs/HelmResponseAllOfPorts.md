# HelmResponseAllOfPorts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | [optional] 
**internal_port** | **int** | The listening port of your service. | 
**external_port** | **int** | The exposed port for your service. This is optional. If not set a default port will be used. | [optional] 
**service_name** | **str** |  | 
**namespace** | **str** |  | [optional] 
**protocol** | [**HelmPortProtocolEnum**](HelmPortProtocolEnum.md) |  | 
**is_default** | **bool** | is the default port to use for domain | [optional] 

## Example

```python
from qovery.models.helm_response_all_of_ports import HelmResponseAllOfPorts

# TODO update the JSON string below
json = "{}"
# create an instance of HelmResponseAllOfPorts from a JSON string
helm_response_all_of_ports_instance = HelmResponseAllOfPorts.from_json(json)
# print the JSON string representation of the object
print HelmResponseAllOfPorts.to_json()

# convert the object into a dict
helm_response_all_of_ports_dict = helm_response_all_of_ports_instance.to_dict()
# create an instance of HelmResponseAllOfPorts from a dict
helm_response_all_of_ports_form_dict = helm_response_all_of_ports.from_dict(helm_response_all_of_ports_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


