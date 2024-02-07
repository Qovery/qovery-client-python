# ReferenceObjectStatusResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[ReferenceObjectStatus]**](ReferenceObjectStatus.md) |  | [optional] 

## Example

```python
from qovery.models.reference_object_status_response_list import ReferenceObjectStatusResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of ReferenceObjectStatusResponseList from a JSON string
reference_object_status_response_list_instance = ReferenceObjectStatusResponseList.from_json(json)
# print the JSON string representation of the object
print ReferenceObjectStatusResponseList.to_json()

# convert the object into a dict
reference_object_status_response_list_dict = reference_object_status_response_list_instance.to_dict()
# create an instance of ReferenceObjectStatusResponseList from a dict
reference_object_status_response_list_form_dict = reference_object_status_response_list.from_dict(reference_object_status_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


