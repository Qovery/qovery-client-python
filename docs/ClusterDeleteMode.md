# ClusterDeleteMode

Indicates the mode to apply on cluster deletion   **\"hard delete\"** means that we delete directly from our database, this is different from a **\"trigger delete\"** that cleans the resource - `DEFAULT`: this is the normal way, trigger delete the cluster only if no environment linked to this cluster remains - `DELETE_CLUSTER_AND_QOVERY_CONFIG`: hard delete environments linked to this cluster then trigger delete the cluster - `DELETE_QOVERY_CONFIG`: ⚠️ ⚠️ ⚠️ hard delete environments linked to this cluster then hard delete the cluster - whole cluster ressources **are not deleted** on our side and must be deleted on your side 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


