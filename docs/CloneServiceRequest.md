# CloneServiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**environment_id** | **str** |  | 

## Example

```python
from qovery.models.clone_service_request import CloneServiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CloneServiceRequest from a JSON string
clone_service_request_instance = CloneServiceRequest.from_json(json)
# print the JSON string representation of the object
print CloneServiceRequest.to_json()

# convert the object into a dict
clone_service_request_dict = clone_service_request_instance.to_dict()
# create an instance of CloneServiceRequest from a dict
clone_service_request_form_dict = clone_service_request.from_dict(clone_service_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


