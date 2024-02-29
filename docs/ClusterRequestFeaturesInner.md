# ClusterRequestFeaturesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**value** | [**ClusterFeatureValue**](ClusterFeatureValue.md) |  | [optional] 

## Example

```python
from qovery.models.cluster_request_features_inner import ClusterRequestFeaturesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterRequestFeaturesInner from a JSON string
cluster_request_features_inner_instance = ClusterRequestFeaturesInner.from_json(json)
# print the JSON string representation of the object
print ClusterRequestFeaturesInner.to_json()

# convert the object into a dict
cluster_request_features_inner_dict = cluster_request_features_inner_instance.to_dict()
# create an instance of ClusterRequestFeaturesInner from a dict
cluster_request_features_inner_form_dict = cluster_request_features_inner.from_dict(cluster_request_features_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


