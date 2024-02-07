# HelmRequestAllOfValuesOverrideFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**git** | [**HelmRequestAllOfValuesOverrideFileGit**](HelmRequestAllOfValuesOverrideFileGit.md) |  | [optional] 
**raw** | [**HelmRequestAllOfValuesOverrideFileRaw**](HelmRequestAllOfValuesOverrideFileRaw.md) |  | [optional] 

## Example

```python
from qovery.models.helm_request_all_of_values_override_file import HelmRequestAllOfValuesOverrideFile

# TODO update the JSON string below
json = "{}"
# create an instance of HelmRequestAllOfValuesOverrideFile from a JSON string
helm_request_all_of_values_override_file_instance = HelmRequestAllOfValuesOverrideFile.from_json(json)
# print the JSON string representation of the object
print HelmRequestAllOfValuesOverrideFile.to_json()

# convert the object into a dict
helm_request_all_of_values_override_file_dict = helm_request_all_of_values_override_file_instance.to_dict()
# create an instance of HelmRequestAllOfValuesOverrideFile from a dict
helm_request_all_of_values_override_file_form_dict = helm_request_all_of_values_override_file.from_dict(helm_request_all_of_values_override_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


