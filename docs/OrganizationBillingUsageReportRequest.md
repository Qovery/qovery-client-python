# OrganizationBillingUsageReportRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **datetime** | The start date of the report | 
**to** | **datetime** | The end date of the report | 
**report_expiration_in_seconds** | **int** | The number of seconds the report will be publicly available | 

## Example

```python
from qovery.models.organization_billing_usage_report_request import OrganizationBillingUsageReportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationBillingUsageReportRequest from a JSON string
organization_billing_usage_report_request_instance = OrganizationBillingUsageReportRequest.from_json(json)
# print the JSON string representation of the object
print OrganizationBillingUsageReportRequest.to_json()

# convert the object into a dict
organization_billing_usage_report_request_dict = organization_billing_usage_report_request_instance.to_dict()
# create an instance of OrganizationBillingUsageReportRequest from a dict
organization_billing_usage_report_request_form_dict = organization_billing_usage_report_request.from_dict(organization_billing_usage_report_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


