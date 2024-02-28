# CloneEnvironmentRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name is case insensitive | 
**cluster_id** | **str** |  | [optional] 
**mode** | [**EnvironmentModeEnum**](EnvironmentModeEnum.md) |  | [optional] 
**apply_deployment_rule** | **bool** |  | [optional] [default to False]

## Example

```python
from qovery.models.clone_environment_request import CloneEnvironmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CloneEnvironmentRequest from a JSON string
clone_environment_request_instance = CloneEnvironmentRequest.from_json(json)
# print the JSON string representation of the object
print CloneEnvironmentRequest.to_json()

# convert the object into a dict
clone_environment_request_dict = clone_environment_request_instance.to_dict()
# create an instance of CloneEnvironmentRequest from a dict
clone_environment_request_form_dict = clone_environment_request.from_dict(clone_environment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


