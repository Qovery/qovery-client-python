# ApplicationPortResponsePorts


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal_port** | **int** | The listening port of your application | 
**publicly_accessible** | **bool** | Expose the port to the world | 
**id** | **str** |  | [optional] 
**name** | **str, none_type** |  | [optional] 
**external_port** | **int** | The exposed port for your application. This is optional. If not set a default port will be used. | [optional] 
**protocol** | **str** |  | [optional]  if omitted the server will use the default value of "HTTP"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


