# RebootServicesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_ids** | **List[str]** |  | [optional] 
**database_ids** | **List[str]** |  | [optional] 
**container_ids** | **List[str]** |  | [optional] 

## Example

```python
from qovery.models.reboot_services_request import RebootServicesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RebootServicesRequest from a JSON string
reboot_services_request_instance = RebootServicesRequest.from_json(json)
# print the JSON string representation of the object
print RebootServicesRequest.to_json()

# convert the object into a dict
reboot_services_request_dict = reboot_services_request_instance.to_dict()
# create an instance of RebootServicesRequest from a dict
reboot_services_request_form_dict = reboot_services_request.from_dict(reboot_services_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


