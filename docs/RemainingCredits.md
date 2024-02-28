# RemainingCredits


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_in_cents** | **int** |  | 
**total** | **float** |  | 
**currency_code** | **str** |  | 

## Example

```python
from qovery.models.remaining_credits import RemainingCredits

# TODO update the JSON string below
json = "{}"
# create an instance of RemainingCredits from a JSON string
remaining_credits_instance = RemainingCredits.from_json(json)
# print the JSON string representation of the object
print RemainingCredits.to_json()

# convert the object into a dict
remaining_credits_dict = remaining_credits_instance.to_dict()
# create an instance of RemainingCredits from a dict
remaining_credits_form_dict = remaining_credits.from_dict(remaining_credits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


