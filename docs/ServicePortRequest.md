# ServicePortRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ports** | [**List[ServicePortRequestPortsInner]**](ServicePortRequestPortsInner.md) |  | [optional] 

## Example

```python
from qovery.models.service_port_request import ServicePortRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServicePortRequest from a JSON string
service_port_request_instance = ServicePortRequest.from_json(json)
# print the JSON string representation of the object
print ServicePortRequest.to_json()

# convert the object into a dict
service_port_request_dict = service_port_request_instance.to_dict()
# create an instance of ServicePortRequest from a dict
service_port_request_form_dict = service_port_request.from_dict(service_port_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


