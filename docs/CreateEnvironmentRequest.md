# CreateEnvironmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name is case insensitive | 
**cluster** | **str** |  | [optional] 
**mode** | [**CreateEnvironmentModeEnum**](CreateEnvironmentModeEnum.md) |  | [optional] 

## Example

```python
from qovery.models.create_environment_request import CreateEnvironmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEnvironmentRequest from a JSON string
create_environment_request_instance = CreateEnvironmentRequest.from_json(json)
# print the JSON string representation of the object
print CreateEnvironmentRequest.to_json()

# convert the object into a dict
create_environment_request_dict = create_environment_request_instance.to_dict()
# create an instance of CreateEnvironmentRequest from a dict
create_environment_request_form_dict = create_environment_request.from_dict(create_environment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


