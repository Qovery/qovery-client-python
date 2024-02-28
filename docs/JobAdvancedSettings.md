# JobAdvancedSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build_timeout_max_sec** | **int** | define the max timeout for the build | [optional] 
**build_cpu_max_in_milli** | **int** | define the max cpu resources (in milli) | [optional] 
**build_ram_max_in_gib** | **int** | define the max ram resources (in gib) | [optional] 
**deployment_termination_grace_period_seconds** | **int** | define how long in seconds an application is supposed to be stopped gracefully | [optional] 
**deployment_affinity_node_required** | **Dict[str, str]** | Set pod placement on specific Kubernetes nodes labels | [optional] 
**job_delete_ttl_seconds_after_finished** | **int** |  | [optional] 
**cronjob_concurrency_policy** | **str** |  | [optional] 
**cronjob_failed_jobs_history_limit** | **int** |  | [optional] 
**cronjob_success_jobs_history_limit** | **int** |  | [optional] 
**security_service_account_name** | **str** | Allows you to set an existing Kubernetes service account name  | [optional] 
**security_read_only_root_filesystem** | **bool** | Mounts the container&#39;s root filesystem as read-only  | [optional] 

## Example

```python
from qovery.models.job_advanced_settings import JobAdvancedSettings

# TODO update the JSON string below
json = "{}"
# create an instance of JobAdvancedSettings from a JSON string
job_advanced_settings_instance = JobAdvancedSettings.from_json(json)
# print the JSON string representation of the object
print JobAdvancedSettings.to_json()

# convert the object into a dict
job_advanced_settings_dict = job_advanced_settings_instance.to_dict()
# create an instance of JobAdvancedSettings from a dict
job_advanced_settings_form_dict = job_advanced_settings.from_dict(job_advanced_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


