# DeployAllRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applications** | [**List[DeployAllRequestApplicationsInner]**](DeployAllRequestApplicationsInner.md) |  | [optional] 
**databases** | **List[str]** |  | [optional] 
**containers** | [**List[DeployAllRequestContainersInner]**](DeployAllRequestContainersInner.md) |  | [optional] 
**jobs** | [**List[DeployAllRequestJobsInner]**](DeployAllRequestJobsInner.md) |  | [optional] 
**helms** | [**List[DeployAllRequestHelmsInner]**](DeployAllRequestHelmsInner.md) |  | [optional] 

## Example

```python
from qovery.models.deploy_all_request import DeployAllRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeployAllRequest from a JSON string
deploy_all_request_instance = DeployAllRequest.from_json(json)
# print the JSON string representation of the object
print DeployAllRequest.to_json()

# convert the object into a dict
deploy_all_request_dict = deploy_all_request_instance.to_dict()
# create an instance of DeployAllRequest from a dict
deploy_all_request_form_dict = deploy_all_request.from_dict(deploy_all_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


