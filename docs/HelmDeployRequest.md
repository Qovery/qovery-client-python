# HelmDeployRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chart_version** | **str** | version of the chart to deploy. Cannot be set if &#x60;git_commit_id&#x60; is defined  | [optional] 
**git_commit_id** | **str** | Commit to deploy for chart source. Cannot be set if &#x60;version&#x60; is defined  | [optional] 
**values_override_git_commit_id** | **str** | Commit to deploy for values override  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


