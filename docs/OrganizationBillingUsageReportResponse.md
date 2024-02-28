# OrganizationBillingUsageReportResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_url** | **str** | The URL of the report | [optional] 
**delete_report_url** | **str** | The URL to delete the report. Use this URL to pro-actively delete the report before it expires | [optional] 

## Example

```python
from qovery.models.organization_billing_usage_report_response import OrganizationBillingUsageReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationBillingUsageReportResponse from a JSON string
organization_billing_usage_report_response_instance = OrganizationBillingUsageReportResponse.from_json(json)
# print the JSON string representation of the object
print OrganizationBillingUsageReportResponse.to_json()

# convert the object into a dict
organization_billing_usage_report_response_dict = organization_billing_usage_report_response_instance.to_dict()
# create an instance of OrganizationBillingUsageReportResponse from a dict
organization_billing_usage_report_response_form_dict = organization_billing_usage_report_response.from_dict(organization_billing_usage_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


