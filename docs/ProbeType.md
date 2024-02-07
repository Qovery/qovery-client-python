# ProbeType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tcp** | [**ProbeTypeTcp**](ProbeTypeTcp.md) |  | [optional] 
**http** | [**ProbeTypeHttp**](ProbeTypeHttp.md) |  | [optional] 
**var_exec** | [**ProbeTypeExec**](ProbeTypeExec.md) |  | [optional] 
**grpc** | [**ProbeTypeGrpc**](ProbeTypeGrpc.md) |  | [optional] 

## Example

```python
from qovery.models.probe_type import ProbeType

# TODO update the JSON string below
json = "{}"
# create an instance of ProbeType from a JSON string
probe_type_instance = ProbeType.from_json(json)
# print the JSON string representation of the object
print ProbeType.to_json()

# convert the object into a dict
probe_type_dict = probe_type_instance.to_dict()
# create an instance of ProbeType from a dict
probe_type_form_dict = probe_type.from_dict(probe_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


