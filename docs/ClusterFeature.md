# ClusterFeature


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**cost_per_month_in_cents** | **int** |  | [optional] 
**cost_per_month** | **float** |  | [optional] 
**currency_code** | **str** |  | [optional] 
**value_type** | **str** |  | [optional] 
**value** | [**ClusterFeatureValue**](ClusterFeatureValue.md) |  | [optional] 
**is_value_updatable** | **bool** |  | [optional] [default to False]
**accepted_values** | [**List[ClusterFeatureAcceptedValuesInner]**](ClusterFeatureAcceptedValuesInner.md) |  | [optional] 

## Example

```python
from qovery.models.cluster_feature import ClusterFeature

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterFeature from a JSON string
cluster_feature_instance = ClusterFeature.from_json(json)
# print the JSON string representation of the object
print ClusterFeature.to_json()

# convert the object into a dict
cluster_feature_dict = cluster_feature_instance.to_dict()
# create an instance of ClusterFeature from a dict
cluster_feature_form_dict = cluster_feature.from_dict(cluster_feature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


