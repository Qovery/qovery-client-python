# SignUpRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**user_email** | **str** |  | 
**type_of_use** | [**TypeOfUseEnum**](TypeOfUseEnum.md) |  | 
**qovery_usage** | **str** |  | 
**company_name** | **str** |  | [optional] 
**company_size** | [**CompanySizeEnum**](CompanySizeEnum.md) |  | [optional] 
**user_role** | **str** |  | [optional] 
**qovery_usage_other** | **str** |  | [optional] 
**user_questions** | **str** |  | [optional] 
**current_step** | **str** |  | [optional] 
**dx_auth** | **bool** |  | [optional] 

## Example

```python
from qovery.models.sign_up_request import SignUpRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SignUpRequest from a JSON string
sign_up_request_instance = SignUpRequest.from_json(json)
# print the JSON string representation of the object
print SignUpRequest.to_json()

# convert the object into a dict
sign_up_request_dict = sign_up_request_instance.to_dict()
# create an instance of SignUpRequest from a dict
sign_up_request_form_dict = sign_up_request.from_dict(sign_up_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


