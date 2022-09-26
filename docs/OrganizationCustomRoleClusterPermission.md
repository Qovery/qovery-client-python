# OrganizationCustomRoleClusterPermission

Indicates the permission for a target cluster, from the lowest to the highest: - `VIEWER` user has only read access on target cluster - `ENV_CREATOR` user can deploy on the cluster - `ADMIN` user can modify the cluster settings 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Indicates the permission for a target cluster, from the lowest to the highest: - &#x60;VIEWER&#x60; user has only read access on target cluster - &#x60;ENV_CREATOR&#x60; user can deploy on the cluster - &#x60;ADMIN&#x60; user can modify the cluster settings  |  must be one of ["VIEWER", "ENV_CREATOR", "ADMIN", ]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


