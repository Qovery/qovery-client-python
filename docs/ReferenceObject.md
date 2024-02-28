# ReferenceObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 

## Example

```python
from qovery.models.reference_object import ReferenceObject

# TODO update the JSON string below
json = "{}"
# create an instance of ReferenceObject from a JSON string
reference_object_instance = ReferenceObject.from_json(json)
# print the JSON string representation of the object
print ReferenceObject.to_json()

# convert the object into a dict
reference_object_dict = reference_object_instance.to_dict()
# create an instance of ReferenceObject from a dict
reference_object_form_dict = reference_object.from_dict(reference_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


