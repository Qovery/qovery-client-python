# ProbeTypeTcp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port** | **int** |  | [optional] 
**host** | **str** |  | [optional] 

## Example

```python
from qovery.models.probe_type_tcp import ProbeTypeTcp

# TODO update the JSON string below
json = "{}"
# create an instance of ProbeTypeTcp from a JSON string
probe_type_tcp_instance = ProbeTypeTcp.from_json(json)
# print the JSON string representation of the object
print ProbeTypeTcp.to_json()

# convert the object into a dict
probe_type_tcp_dict = probe_type_tcp_instance.to_dict()
# create an instance of ProbeTypeTcp from a dict
probe_type_tcp_form_dict = probe_type_tcp.from_dict(probe_type_tcp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


