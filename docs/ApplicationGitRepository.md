# ApplicationGitRepository


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | [**GitProviderEnum**](GitProviderEnum.md) |  | 
**owner** | **str** |  | 
**url** | **str** |  | 
**name** | **str** | repository name | 
**has_access** | **bool** |  | [optional] 
**branch** | **str** |  | [optional] 
**root_path** | **str** |  | [optional] 
**deployed_commit_id** | **str** | Git commit ID corresponding to the deployed version of the app | [optional] 
**deployed_commit_date** | **datetime** | Git commit date corresponding to the deployed version of the app | [optional] [readonly] 
**deployed_commit_contributor** | **str** | Git commit user corresponding to the deployed version of the app | [optional] 
**deployed_commit_tag** | **str** |  | [optional] 
**git_token_id** | **str, none_type** |  | [optional] 
**git_token_name** | **str, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


