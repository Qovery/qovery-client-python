# ProbeTypeHttp


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** |  | [optional] [default to '/']
**scheme** | **str** |  | [optional] [default to 'HTTP']
**port** | **int** |  | [optional] 

## Example

```python
from qovery.models.probe_type_http import ProbeTypeHttp

# TODO update the JSON string below
json = "{}"
# create an instance of ProbeTypeHttp from a JSON string
probe_type_http_instance = ProbeTypeHttp.from_json(json)
# print the JSON string representation of the object
print ProbeTypeHttp.to_json()

# convert the object into a dict
probe_type_http_dict = probe_type_http_instance.to_dict()
# create an instance of ProbeTypeHttp from a dict
probe_type_http_form_dict = probe_type_http.from_dict(probe_type_http_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


