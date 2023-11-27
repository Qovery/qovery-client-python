# HelmResponseAllOfPorts


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**internal_port** | **int** | The listening port of your service. | 
**service_name** | **str** |  | 
**protocol** | [**HelmPortProtocolEnum**](HelmPortProtocolEnum.md) |  | 
**name** | **str** |  | [optional] 
**external_port** | **int** | The exposed port for your service. This is optional. If not set a default port will be used. | [optional] 
**namespace** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

