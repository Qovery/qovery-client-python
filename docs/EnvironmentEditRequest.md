# EnvironmentEditRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**mode** | [**CreateEnvironmentModeEnum**](CreateEnvironmentModeEnum.md) |  | [optional] 

## Example

```python
from qovery.models.environment_edit_request import EnvironmentEditRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentEditRequest from a JSON string
environment_edit_request_instance = EnvironmentEditRequest.from_json(json)
# print the JSON string representation of the object
print EnvironmentEditRequest.to_json()

# convert the object into a dict
environment_edit_request_dict = environment_edit_request_instance.to_dict()
# create an instance of EnvironmentEditRequest from a dict
environment_edit_request_form_dict = environment_edit_request.from_dict(environment_edit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


