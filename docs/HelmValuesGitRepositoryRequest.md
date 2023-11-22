# HelmValuesGitRepositoryRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | application git repository URL | 
**branch** | **str** | Name of the branch to use. This is optional If not specified, then the branch used is the &#x60;main&#x60; or &#x60;master&#x60; one  | 
**paths** | **[str]** | List of path inside your git repository to locate values file. Must start by a / | 
**git_token_id** | **str, none_type** | The git token id on Qovery side | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


