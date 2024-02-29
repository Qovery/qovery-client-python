# JobRequestAllOfSourceImage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_name** | **str** | The image name pattern differs according to chosen container registry provider:   * &#x60;ECR&#x60;: &#x60;repository&#x60; * &#x60;SCALEWAY_CR&#x60;: &#x60;namespace/image&#x60; * &#x60;DOCKER_HUB&#x60;: &#x60;image&#x60; or &#x60;repository/image&#x60; * &#x60;PUBLIC_ECR&#x60;: &#x60;registry_alias/repository&#x60;  | [optional] 
**tag** | **str** | tag of the image container | [optional] 
**registry_id** | **str** | tag of the image container | [optional] 

## Example

```python
from qovery.models.job_request_all_of_source_image import JobRequestAllOfSourceImage

# TODO update the JSON string below
json = "{}"
# create an instance of JobRequestAllOfSourceImage from a JSON string
job_request_all_of_source_image_instance = JobRequestAllOfSourceImage.from_json(json)
# print the JSON string representation of the object
print JobRequestAllOfSourceImage.to_json()

# convert the object into a dict
job_request_all_of_source_image_dict = job_request_all_of_source_image_instance.to_dict()
# create an instance of JobRequestAllOfSourceImage from a dict
job_request_all_of_source_image_form_dict = job_request_all_of_source_image.from_dict(job_request_all_of_source_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


