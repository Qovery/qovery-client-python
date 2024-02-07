# DeployRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**git_commit_id** | **str** | Commit ID to deploy | 

## Example

```python
from qovery.models.deploy_request import DeployRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeployRequest from a JSON string
deploy_request_instance = DeployRequest.from_json(json)
# print the JSON string representation of the object
print DeployRequest.to_json()

# convert the object into a dict
deploy_request_dict = deploy_request_instance.to_dict()
# create an instance of DeployRequest from a dict
deploy_request_form_dict = deploy_request.from_dict(deploy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


