# HelmResponseAllOfValuesOverrideFile


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**raw** | [**HelmResponseAllOfValuesOverrideFileRaw**](HelmResponseAllOfValuesOverrideFileRaw.md) |  | [optional] 
**git** | [**HelmResponseAllOfValuesOverrideFileGit**](HelmResponseAllOfValuesOverrideFileGit.md) |  | [optional] 

## Example

```python
from qovery.models.helm_response_all_of_values_override_file import HelmResponseAllOfValuesOverrideFile

# TODO update the JSON string below
json = "{}"
# create an instance of HelmResponseAllOfValuesOverrideFile from a JSON string
helm_response_all_of_values_override_file_instance = HelmResponseAllOfValuesOverrideFile.from_json(json)
# print the JSON string representation of the object
print HelmResponseAllOfValuesOverrideFile.to_json()

# convert the object into a dict
helm_response_all_of_values_override_file_dict = helm_response_all_of_values_override_file_instance.to_dict()
# create an instance of HelmResponseAllOfValuesOverrideFile from a dict
helm_response_all_of_values_override_file_form_dict = helm_response_all_of_values_override_file.from_dict(helm_response_all_of_values_override_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


