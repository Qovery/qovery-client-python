# Cost


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_in_cents** | **int** |  | 
**total** | **float** |  | 
**currency_code** | **str** |  | 

## Example

```python
from qovery.models.cost import Cost

# TODO update the JSON string below
json = "{}"
# create an instance of Cost from a JSON string
cost_instance = Cost.from_json(json)
# print the JSON string representation of the object
print Cost.to_json()

# convert the object into a dict
cost_dict = cost_instance.to_dict()
# create an instance of Cost from a dict
cost_form_dict = cost.from_dict(cost_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


