# DeployAllRequestHelmsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id of the helm to be updated. | [optional] 
**chart_version** | **str** | The new chart version for the Helm source. Use this only if the helm has a Helm repository source. | [optional] 
**git_commit_id** | **str** | The commit Id to deploy. Use this only if the helm has a Git repository source. | [optional] 
**values_override_git_commit_id** | **str** | The commit Id of the override values to deploy. Use only if the helm has a Git override values repository. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


