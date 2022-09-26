# OrganizationCustomRoleProjectPermission

Indicates the permission for a target project and a given environment type, from the lowest to the highest: - `NO_ACCESS` user has no access - `VIEWER` user can access the environment (and applications / containers / databases / variables) - `DEPLOYER` user can deploy the environment (dependent on the required cluster permission `ENV_CREATOR`) - `MANAGER` user can create an environment (and applications / containers / databases / variables) 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Indicates the permission for a target project and a given environment type, from the lowest to the highest: - &#x60;NO_ACCESS&#x60; user has no access - &#x60;VIEWER&#x60; user can access the environment (and applications / containers / databases / variables) - &#x60;DEPLOYER&#x60; user can deploy the environment (dependent on the required cluster permission &#x60;ENV_CREATOR&#x60;) - &#x60;MANAGER&#x60; user can create an environment (and applications / containers / databases / variables)  |  must be one of ["NO_ACCESS", "VIEWER", "DEPLOYER", "MANAGER", ]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


