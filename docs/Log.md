# Log


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_at** | **datetime** |  | 
**message** | **str** |  | 
**pod_name** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from qovery.models.log import Log

# TODO update the JSON string below
json = "{}"
# create an instance of Log from a JSON string
log_instance = Log.from_json(json)
# print the JSON string representation of the object
print Log.to_json()

# convert the object into a dict
log_dict = log_instance.to_dict()
# create an instance of Log from a dict
log_form_dict = log.from_dict(log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


