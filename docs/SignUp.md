# SignUp


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
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
**infrastructure_hosting** | **str** |  | [optional] 

## Example

```python
from qovery.models.sign_up import SignUp

# TODO update the JSON string below
json = "{}"
# create an instance of SignUp from a JSON string
sign_up_instance = SignUp.from_json(json)
# print the JSON string representation of the object
print SignUp.to_json()

# convert the object into a dict
sign_up_dict = sign_up_instance.to_dict()
# create an instance of SignUp from a dict
sign_up_form_dict = sign_up.from_dict(sign_up_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


