# HelmPortRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ports** | [**List[HelmPortRequestPortsInner]**](HelmPortRequestPortsInner.md) |  | [optional] 

## Example

```python
from qovery.models.helm_port_request import HelmPortRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HelmPortRequest from a JSON string
helm_port_request_instance = HelmPortRequest.from_json(json)
# print the JSON string representation of the object
print HelmPortRequest.to_json()

# convert the object into a dict
helm_port_request_dict = helm_port_request_instance.to_dict()
# create an instance of HelmPortRequest from a dict
helm_port_request_form_dict = helm_port_request.from_dict(helm_port_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


