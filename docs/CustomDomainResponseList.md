# CustomDomainResponseList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[CustomDomain]**](CustomDomain.md) |  | [optional] 

## Example

```python
from qovery.models.custom_domain_response_list import CustomDomainResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of CustomDomainResponseList from a JSON string
custom_domain_response_list_instance = CustomDomainResponseList.from_json(json)
# print the JSON string representation of the object
print CustomDomainResponseList.to_json()

# convert the object into a dict
custom_domain_response_list_dict = custom_domain_response_list_instance.to_dict()
# create an instance of CustomDomainResponseList from a dict
custom_domain_response_list_form_dict = custom_domain_response_list.from_dict(custom_domain_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


