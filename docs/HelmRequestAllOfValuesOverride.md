# HelmRequestAllOfValuesOverride

Specify helm values you want to set or override 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **List[List[str]]** | The input is in json array format: [ [$KEY,$VALUE], [...] ] | [optional] 
**set_string** | **List[List[str]]** | The input is in json array format: [ [$KEY,$VALUE], [...] ] | [optional] 
**set_json** | **List[List[str]]** | The input is in json array format: [ [$KEY,$VALUE], [...] ] | [optional] 
**file** | [**HelmRequestAllOfValuesOverrideFile**](HelmRequestAllOfValuesOverrideFile.md) |  | [optional] 

## Example

```python
from qovery.models.helm_request_all_of_values_override import HelmRequestAllOfValuesOverride

# TODO update the JSON string below
json = "{}"
# create an instance of HelmRequestAllOfValuesOverride from a JSON string
helm_request_all_of_values_override_instance = HelmRequestAllOfValuesOverride.from_json(json)
# print the JSON string representation of the object
print HelmRequestAllOfValuesOverride.to_json()

# convert the object into a dict
helm_request_all_of_values_override_dict = helm_request_all_of_values_override_instance.to_dict()
# create an instance of HelmRequestAllOfValuesOverride from a dict
helm_request_all_of_values_override_form_dict = helm_request_all_of_values_override.from_dict(helm_request_all_of_values_override_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


