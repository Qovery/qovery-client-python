# DeployAllRequestContainersInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id of the container to be updated. | 
**image_tag** | **str** | new tag for the container. Can be empty only if the service has been already deployed (in this case the service version won&#39;t be changed) | [optional] 

## Example

```python
from qovery.models.deploy_all_request_containers_inner import DeployAllRequestContainersInner

# TODO update the JSON string below
json = "{}"
# create an instance of DeployAllRequestContainersInner from a JSON string
deploy_all_request_containers_inner_instance = DeployAllRequestContainersInner.from_json(json)
# print the JSON string representation of the object
print DeployAllRequestContainersInner.to_json()

# convert the object into a dict
deploy_all_request_containers_inner_dict = deploy_all_request_containers_inner_instance.to_dict()
# create an instance of DeployAllRequestContainersInner from a dict
deploy_all_request_containers_inner_form_dict = deploy_all_request_containers_inner.from_dict(deploy_all_request_containers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


