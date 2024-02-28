# EnvironmentServiceIdsAllRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_ids** | **List[str]** |  | [optional] 
**container_ids** | **List[str]** |  | [optional] 
**database_ids** | **List[str]** |  | [optional] 
**job_ids** | **List[str]** |  | [optional] 
**helm_ids** | **List[str]** |  | [optional] 

## Example

```python
from qovery.models.environment_service_ids_all_request import EnvironmentServiceIdsAllRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentServiceIdsAllRequest from a JSON string
environment_service_ids_all_request_instance = EnvironmentServiceIdsAllRequest.from_json(json)
# print the JSON string representation of the object
print EnvironmentServiceIdsAllRequest.to_json()

# convert the object into a dict
environment_service_ids_all_request_dict = environment_service_ids_all_request_instance.to_dict()
# create an instance of EnvironmentServiceIdsAllRequest from a dict
environment_service_ids_all_request_form_dict = environment_service_ids_all_request.from_dict(environment_service_ids_all_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


