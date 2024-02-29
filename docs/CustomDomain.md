# CustomDomain


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [readonly] 
**created_at** | **datetime** |  | [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**domain** | **str** | your custom domain | 
**generate_certificate** | **bool** | to control if a certificate has to be generated for this custom domain by Qovery. The default value is &#x60;true&#x60;. This flag should be set to &#x60;false&#x60; if a CDN or other entities are managing the certificate for the specified domain and the traffic is proxied by the CDN to Qovery. | 
**validation_domain** | **str** | URL provided by Qovery. You must create a CNAME on your DNS provider using that URL | [optional] 
**status** | [**CustomDomainStatusEnum**](CustomDomainStatusEnum.md) |  | [optional] 

## Example

```python
from qovery.models.custom_domain import CustomDomain

# TODO update the JSON string below
json = "{}"
# create an instance of CustomDomain from a JSON string
custom_domain_instance = CustomDomain.from_json(json)
# print the JSON string representation of the object
print CustomDomain.to_json()

# convert the object into a dict
custom_domain_dict = custom_domain_instance.to_dict()
# create an instance of CustomDomain from a dict
custom_domain_form_dict = custom_domain.from_dict(custom_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


