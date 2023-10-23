# HelmResponseAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | [**ReferenceObject**](ReferenceObject.md) |  | 
**name** | **str** | name is case insensitive | 
**auto_preview** | **bool** | Indicates if the &#39;environment preview option&#39; is enabled.   If enabled, a preview environment will be automatically cloned when &#x60;/preview&#x60; endpoint is called.   If not specified, it takes the value of the &#x60;auto_preview&#x60; property from the associated environment.  | 
**auto_deploy** | **bool** | Specify if the service will be automatically updated after receiving a new image tag or a new commit according to the source type.   | 
**source** | [**HelmRequestAllOfSource**](HelmRequestAllOfSource.md) |  | 
**description** | **str** |  | [optional] 
**arguments** | **[str]** | The extra arguments to pass to helm | [optional] 
**allow_cluster_wide_resources** | **bool** | If we should allow the chart to deploy object outside his specified namespace. Setting this flag to true, requires special rights  | [optional]  if omitted the server will use the default value of False
**values_override** | [**HelmRequestAllOfValuesOverride**](HelmRequestAllOfValuesOverride.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


