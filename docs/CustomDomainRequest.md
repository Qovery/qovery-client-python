# CustomDomainRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | your custom domain | 
**generate_certificate** | **bool** | to control if a certificate has to be generated for this custom domain by Qovery. The default value is &#x60;true&#x60;. This flag should be set to &#x60;false&#x60; if a CDN or other entities are managing the certificate for the specified domain and the traffic is proxied by the CDN to Qovery. | 

## Example

```python
from qovery.models.custom_domain_request import CustomDomainRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomDomainRequest from a JSON string
custom_domain_request_instance = CustomDomainRequest.from_json(json)
# print the JSON string representation of the object
print CustomDomainRequest.to_json()

# convert the object into a dict
custom_domain_request_dict = custom_domain_request_instance.to_dict()
# create an instance of CustomDomainRequest from a dict
custom_domain_request_form_dict = custom_domain_request.from_dict(custom_domain_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


