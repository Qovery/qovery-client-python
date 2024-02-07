# HelmResponseAllOfValuesOverride

Specify helm values you want to set or override 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **List[List[str]]** | The input is in json array format: [ [$KEY,$VALUE], [...] ] | [optional] 
**set_string** | **List[List[str]]** | The input is in json array format: [ [$KEY,$VALUE], [...] ] | [optional] 
**set_json** | **List[List[str]]** | The input is in json array format: [ [$KEY,$VALUE], [...] ] | [optional] 
**file** | [**HelmResponseAllOfValuesOverrideFile**](HelmResponseAllOfValuesOverrideFile.md) |  | [optional] 

## Example

```python
from qovery.models.helm_response_all_of_values_override import HelmResponseAllOfValuesOverride

# TODO update the JSON string below
json = "{}"
# create an instance of HelmResponseAllOfValuesOverride from a JSON string
helm_response_all_of_values_override_instance = HelmResponseAllOfValuesOverride.from_json(json)
# print the JSON string representation of the object
print HelmResponseAllOfValuesOverride.to_json()

# convert the object into a dict
helm_response_all_of_values_override_dict = helm_response_all_of_values_override_instance.to_dict()
# create an instance of HelmResponseAllOfValuesOverride from a dict
helm_response_all_of_values_override_form_dict = helm_response_all_of_values_override.from_dict(helm_response_all_of_values_override_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


