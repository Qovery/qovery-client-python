# HelmRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name is case insensitive | 
**description** | **str** |  | [optional] 
**timeout_sec** | **int** | Maximum number of seconds allowed for helm to run before killing it and mark it as failed  | [optional]  if omitted the server will use the default value of 600
**auto_preview** | **bool, none_type** | Indicates if the &#39;environment preview option&#39; is enabled.   If enabled, a preview environment will be automatically cloned when &#x60;/preview&#x60; endpoint is called or when a new commit is updated. If not specified, it takes the value of the &#x60;auto_preview&#x60; property from the associated environment.  | [optional] 
**auto_deploy** | **bool** | Specify if the helm will be automatically updated after receiving a new image tag or a new commit according to the source type.   | [optional] 
**source** | [**HelmRequestAllOfSource**](HelmRequestAllOfSource.md) |  | [optional] 
**arguments** | **[str]** | The extra arguments to pass to helm | [optional] 
**allow_cluster_wide_resources** | **bool** | If we should allow the chart to deploy object outside his specified namespace. Setting this flag to true, requires special rights  | [optional]  if omitted the server will use the default value of False
**values_override** | [**HelmRequestAllOfValuesOverride**](HelmRequestAllOfValuesOverride.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


