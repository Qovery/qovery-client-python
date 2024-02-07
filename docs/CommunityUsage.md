# CommunityUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**projects** | [**List[ProjectCurrentCost]**](ProjectCurrentCost.md) |  | [optional] 

## Example

```python
from qovery.models.community_usage import CommunityUsage

# TODO update the JSON string below
json = "{}"
# create an instance of CommunityUsage from a JSON string
community_usage_instance = CommunityUsage.from_json(json)
# print the JSON string representation of the object
print CommunityUsage.to_json()

# convert the object into a dict
community_usage_dict = community_usage_instance.to_dict()
# create an instance of CommunityUsage from a dict
community_usage_form_dict = community_usage.from_dict(community_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


