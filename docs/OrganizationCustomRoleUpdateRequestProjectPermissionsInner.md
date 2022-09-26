# OrganizationCustomRoleUpdateRequestProjectPermissionsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | [optional] 
**is_admin** | **bool** | If &#x60;is_admin&#x60; is &#x60;true&#x60;, the user is: - automatically &#x60;MANAGER&#x60; for each environment type - allowed to manage project deployment rules - able to delete the project Note that &#x60;permissions&#x60; can then be ignored for this project  | [optional]  if omitted the server will use the default value of False
**permissions** | [**[OrganizationCustomRoleUpdateRequestProjectPermissionsInnerPermissionsInner]**](OrganizationCustomRoleUpdateRequestProjectPermissionsInnerPermissionsInner.md) | Mandatory if &#x60;is_admin&#x60; is &#x60;false&#x60;   Should contain an entry for every environment type: - &#x60;DEVELOPMENT&#x60; - &#x60;PREVIEW&#x60; - &#x60;STAGING&#x60; - &#x60;PRODUCTION&#x60;  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


