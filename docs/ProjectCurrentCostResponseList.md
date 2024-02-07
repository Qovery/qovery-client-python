# ProjectCurrentCostResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**projects** | [**List[ProjectCurrentCost]**](ProjectCurrentCost.md) |  | [optional] 

## Example

```python
from qovery.models.project_current_cost_response_list import ProjectCurrentCostResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectCurrentCostResponseList from a JSON string
project_current_cost_response_list_instance = ProjectCurrentCostResponseList.from_json(json)
# print the JSON string representation of the object
print ProjectCurrentCostResponseList.to_json()

# convert the object into a dict
project_current_cost_response_list_dict = project_current_cost_response_list_instance.to_dict()
# create an instance of ProjectCurrentCostResponseList from a dict
project_current_cost_response_list_form_dict = project_current_cost_response_list.from_dict(project_current_cost_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


