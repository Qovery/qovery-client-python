# Base


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from qovery.models.base import Base

# TODO update the JSON string below
json = "{}"
# create an instance of Base from a JSON string
base_instance = Base.from_json(json)
# print the JSON string representation of the object
print Base.to_json()

# convert the object into a dict
base_dict = base_instance.to_dict()
# create an instance of Base from a dict
base_form_dict = base.from_dict(base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


