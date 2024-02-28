# HelmResponseList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[HelmResponse]**](HelmResponse.md) |  | [optional] 

## Example

```python
from qovery.models.helm_response_list import HelmResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of HelmResponseList from a JSON string
helm_response_list_instance = HelmResponseList.from_json(json)
# print the JSON string representation of the object
print HelmResponseList.to_json()

# convert the object into a dict
helm_response_list_dict = helm_response_list_instance.to_dict()
# create an instance of HelmResponseList from a dict
helm_response_list_form_dict = helm_response_list.from_dict(helm_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


