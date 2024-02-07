# ProjectResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[Project]**](Project.md) |  | [optional] 

## Example

```python
from qovery.models.project_response_list import ProjectResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectResponseList from a JSON string
project_response_list_instance = ProjectResponseList.from_json(json)
# print the JSON string representation of the object
print ProjectResponseList.to_json()

# convert the object into a dict
project_response_list_dict = project_response_list_instance.to_dict()
# create an instance of ProjectResponseList from a dict
project_response_list_form_dict = project_response_list.from_dict(project_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


