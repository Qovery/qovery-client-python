# HelmResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**environment** | [**ReferenceObject**](ReferenceObject.md) |  | 
**name** | **str** | name is case insensitive | 
**description** | **str** |  | [optional] 
**timeout_sec** | **int** | Maximum number of seconds allowed for helm to run before killing it and mark it as failed  | [optional] [default to 600]
**auto_preview** | **bool** | Indicates if the &#39;environment preview option&#39; is enabled.   If enabled, a preview environment will be automatically cloned when &#x60;/preview&#x60; endpoint is called.   If not specified, it takes the value of the &#x60;auto_preview&#x60; property from the associated environment.  | 
**auto_deploy** | **bool** | Specify if the service will be automatically updated after receiving a new image tag or a new commit according to the source type.  | 
**ports** | [**List[HelmResponseAllOfPorts]**](HelmResponseAllOfPorts.md) |  | [optional] 
**source** | [**HelmResponseAllOfSource**](HelmResponseAllOfSource.md) |  | 
**arguments** | **List[str]** | The extra arguments to pass to helm | 
**allow_cluster_wide_resources** | **bool** | If we should allow the chart to deploy object outside his specified namespace. Setting this flag to true, requires special rights  | [default to False]
**values_override** | [**HelmResponseAllOfValuesOverride**](HelmResponseAllOfValuesOverride.md) |  | 

## Example

```python
from qovery.models.helm_response import HelmResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HelmResponse from a JSON string
helm_response_instance = HelmResponse.from_json(json)
# print the JSON string representation of the object
print HelmResponse.to_json()

# convert the object into a dict
helm_response_dict = helm_response_instance.to_dict()
# create an instance of HelmResponse from a dict
helm_response_form_dict = helm_response.from_dict(helm_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


