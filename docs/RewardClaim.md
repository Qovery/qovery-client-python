# RewardClaim


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**code** | **str** |  | [optional] 

## Example

```python
from qovery.models.reward_claim import RewardClaim

# TODO update the JSON string below
json = "{}"
# create an instance of RewardClaim from a JSON string
reward_claim_instance = RewardClaim.from_json(json)
# print the JSON string representation of the object
print RewardClaim.to_json()

# convert the object into a dict
reward_claim_dict = reward_claim_instance.to_dict()
# create an instance of RewardClaim from a dict
reward_claim_form_dict = reward_claim.from_dict(reward_claim_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


