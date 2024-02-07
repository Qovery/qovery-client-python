# AvailableContainerRegistryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | [**ContainerRegistryKindEnum**](ContainerRegistryKindEnum.md) |  | 
**required_config** | **Dict[str, object]** |  | 
**is_mandatory** | **bool** |  | 

## Example

```python
from qovery.models.available_container_registry_response import AvailableContainerRegistryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableContainerRegistryResponse from a JSON string
available_container_registry_response_instance = AvailableContainerRegistryResponse.from_json(json)
# print the JSON string representation of the object
print AvailableContainerRegistryResponse.to_json()

# convert the object into a dict
available_container_registry_response_dict = available_container_registry_response_instance.to_dict()
# create an instance of AvailableContainerRegistryResponse from a dict
available_container_registry_response_form_dict = available_container_registry_response.from_dict(available_container_registry_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


