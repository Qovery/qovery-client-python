# DeploymentHistoryEnvironmentPaginatedResponseList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **float** |  | 
**page_size** | **float** |  | 
**results** | [**List[DeploymentHistoryEnvironment]**](DeploymentHistoryEnvironment.md) |  | [optional] 

## Example

```python
from qovery.models.deployment_history_environment_paginated_response_list import DeploymentHistoryEnvironmentPaginatedResponseList

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentHistoryEnvironmentPaginatedResponseList from a JSON string
deployment_history_environment_paginated_response_list_instance = DeploymentHistoryEnvironmentPaginatedResponseList.from_json(json)
# print the JSON string representation of the object
print DeploymentHistoryEnvironmentPaginatedResponseList.to_json()

# convert the object into a dict
deployment_history_environment_paginated_response_list_dict = deployment_history_environment_paginated_response_list_instance.to_dict()
# create an instance of DeploymentHistoryEnvironmentPaginatedResponseList from a dict
deployment_history_environment_paginated_response_list_form_dict = deployment_history_environment_paginated_response_list.from_dict(deployment_history_environment_paginated_response_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


