# ServiceStepMetricNameEnum

The name of the deployment step at the service level: - REGISTRY_CREATE_REPOSITORY: The step to create the repository in the registry. - GIT_CLONE: The step to clone the source code repository.  - BUILD_QUEUEING: The queuing time preceding the actual building step. - BUILD: The step to build the source code. - DEPLOYMENT_QUEUEING: The queuing time preceding the actual deployment step. - DEPLOYMENT: The step to deploy the service.  - ROUTER_DEPLOYMENT: The step to deploy the router.  - MIRROR_IMAGE: The step to mirror the image to the private registry. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The name of the deployment step at the service level: - REGISTRY_CREATE_REPOSITORY: The step to create the repository in the registry. - GIT_CLONE: The step to clone the source code repository.  - BUILD_QUEUEING: The queuing time preceding the actual building step. - BUILD: The step to build the source code. - DEPLOYMENT_QUEUEING: The queuing time preceding the actual deployment step. - DEPLOYMENT: The step to deploy the service.  - ROUTER_DEPLOYMENT: The step to deploy the router.  - MIRROR_IMAGE: The step to mirror the image to the private registry.  |  must be one of ["REGISTRY_CREATE_REPOSITORY", "GIT_CLONE", "BUILD_QUEUEING", "BUILD", "DEPLOYMENT_QUEUEING", "DEPLOYMENT", "ROUTER_DEPLOYMENT", "MIRROR_IMAGE", ]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


