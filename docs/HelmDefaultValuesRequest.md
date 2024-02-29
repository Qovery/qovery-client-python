# HelmDefaultValuesRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**HelmRequestAllOfSource**](HelmRequestAllOfSource.md) |  | 

## Example

```python
from qovery.models.helm_default_values_request import HelmDefaultValuesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HelmDefaultValuesRequest from a JSON string
helm_default_values_request_instance = HelmDefaultValuesRequest.from_json(json)
# print the JSON string representation of the object
print HelmDefaultValuesRequest.to_json()

# convert the object into a dict
helm_default_values_request_dict = helm_default_values_request_instance.to_dict()
# create an instance of HelmDefaultValuesRequest from a dict
helm_default_values_request_form_dict = helm_default_values_request.from_dict(helm_default_values_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


