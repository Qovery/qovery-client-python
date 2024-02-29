# Link


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**internal_port** | **int** | The port from which the service is reachable from within the cluster | [optional] 
**external_port** | **int** | The port from which the service is reachable from externally (i.e: 443 for HTTPS) | [optional] 
**is_qovery_domain** | **bool** | True if the domain is managed by Qovery, false if it belongs to the user | [optional] 
**is_default** | **bool** | Indicate if the link is using the root of the domain and not one derivated from port i.e: p8080.zxxxx.jvm.worl      &#x3D;&gt; is_default &#x3D; false, is_qovery &#x3D; true zxxxx.jvm.world           &#x3D;&gt; is_default &#x3D; true, is_qovery &#x3D; true p8080-my-super-domain.com &#x3D;&gt; is_default &#x3D; false, is_qovery &#x3D; false my-super-domain.com       &#x3D;&gt; is_default &#x3D; true, is_qovery &#x3D; false  | [optional] 

## Example

```python
from qovery.models.link import Link

# TODO update the JSON string below
json = "{}"
# create an instance of Link from a JSON string
link_instance = Link.from_json(json)
# print the JSON string representation of the object
print Link.to_json()

# convert the object into a dict
link_dict = link_instance.to_dict()
# create an instance of Link from a dict
link_form_dict = link.from_dict(link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


