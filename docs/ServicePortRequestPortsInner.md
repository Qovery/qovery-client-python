# ServicePortRequestPortsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal_port** | **int** | The listening port of your service. | 
**publicly_accessible** | **bool** | Expose the port to the world | 
**name** | **str** |  | [optional] 
**external_port** | **int** | The exposed port for your service. This is optional. If not set a default port will be used. | [optional] 
**is_default** | **bool** | is the default port to use for domain &amp; probes check | [optional] 
**protocol** | [**PortProtocolEnum**](PortProtocolEnum.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


