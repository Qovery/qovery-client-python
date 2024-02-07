# Referral


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_invited** | **int** |  | [optional] 
**invitation_link** | **str** |  | [optional] 

## Example

```python
from qovery.models.referral import Referral

# TODO update the JSON string below
json = "{}"
# create an instance of Referral from a JSON string
referral_instance = Referral.from_json(json)
# print the JSON string representation of the object
print Referral.to_json()

# convert the object into a dict
referral_dict = referral_instance.to_dict()
# create an instance of Referral from a dict
referral_form_dict = referral.from_dict(referral_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


