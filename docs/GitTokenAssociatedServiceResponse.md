# GitTokenAssociatedServiceResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | 
**project_name** | **str** |  | 
**environment_id** | **str** |  | 
**environment_name** | **str** |  | 
**service_id** | **str** |  | 
**service_name** | **str** |  | 
**service_type** | [**GitTokenAssociatedServiceType**](GitTokenAssociatedServiceType.md) |  | 

## Example

```python
from qovery.models.git_token_associated_service_response import GitTokenAssociatedServiceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GitTokenAssociatedServiceResponse from a JSON string
git_token_associated_service_response_instance = GitTokenAssociatedServiceResponse.from_json(json)
# print the JSON string representation of the object
print GitTokenAssociatedServiceResponse.to_json()

# convert the object into a dict
git_token_associated_service_response_dict = git_token_associated_service_response_instance.to_dict()
# create an instance of GitTokenAssociatedServiceResponse from a dict
git_token_associated_service_response_form_dict = git_token_associated_service_response.from_dict(git_token_associated_service_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


